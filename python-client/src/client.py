from typing import Mapping, List, Optional, Iterator

import grpc
from google.protobuf.wrappers_pb2 import Int32Value, StringValue, Int64Value
from hbase_pb2 import ScanRequest, Table, GetRequest, ColumnQuery, Column, Result
from hbase_pb2_grpc import HBaseServiceStub


class Client:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self._channel = grpc.insecure_channel(host + ":" + str(port))
        self._client = HBaseServiceStub(self._channel)

    def get(
            self,
            row: str,
            table_name: str,
            table_namespace: str = "default",
            columns: Optional[Mapping[str, List[str]]] = None,
            min_time: Optional[int] = None,
            max_time: Optional[int] = None,
            max_versions: Optional[int] = None
    ) -> 'Result':
        if min_time is not None:
            _min_time = Int64Value(value=min_time)
        else:
            _min_time = Int64Value()

        if max_time is not None:
            _max_time = Int64Value(value=max_time)
        else:
            _max_time = Int64Value()

        if max_versions is not None:
            _max_versions = Int32Value(value=max_versions)
        else:
            _max_versions = Int32Value()

        if columns is not None:
            _columns = self._convert_columns(columns)
        else:
            _columns = []

        query = GetRequest(
            table=Table(name=table_name, namespace=table_namespace),
            row=row,
            columns=_columns,
            max_versions=_max_versions,
            min_time=_min_time,
            max_time=_max_time
        )

        return self._client.Get(query)

    def scan(
            self,
            table_name: str,
            table_namespace: str = "default",
            start_row: Optional[str] = None,
            stop_row: Optional[str] = None,
            prefix: Optional[str] = None,
            columns: Optional[Mapping[str, List[str]]] = None,
            min_time: Optional[int] = None,
            max_time: Optional[int] = None,
            max_versions: Optional[int] = None
    ) -> Iterator[Result]:

        if start_row is not None:
            _start_row = StringValue(value=start_row)
        else:
            _start_row = None

        if stop_row is not None:
            _stop_row = StringValue(value=stop_row)
        else:
            _stop_row = None

        if prefix is not None:
            _prefix = StringValue(value=prefix)
        else:
            _prefix = None

        if min_time is not None:
            _min_time = Int64Value(value=min_time)
        else:
            _min_time = None

        if max_time is not None:
            _max_time = Int64Value(value=max_time)
        else:
            _max_time = None

        if columns is not None:
            _columns = self._convert_columns(columns)
        else:
            _columns = []

        if max_versions is not None:
            _max_versions = Int32Value(value=max_versions)
        else:
            _max_versions = None

        query = ScanRequest(
            table=Table(name=table_name, namespace=table_namespace),
            start_row=_start_row,
            stop_row=_stop_row,
            prefix=_prefix,
            columns=_columns,
            min_time=_min_time,
            max_time=_max_time,
            max_versions=_max_versions
        )

        return self._client.Scan(query)

    def _convert_columns(self, columns: Mapping[str, List[str]]) -> List[ColumnQuery]:
        return [q for fam, quals in columns.items() for q in self._get_column_queries(fam, quals)]

    def _get_column_queries(self, family: str, qualifiers: List[str]) -> List[ColumnQuery]:
        if not qualifiers:
            return [self._get_column_query(family, None)]
        else:
            return [self._get_column_query(family, q) for q in qualifiers]

    @staticmethod
    def _get_column_query(family: str, qualifier: Optional[str]) -> ColumnQuery:
        query = ColumnQuery()
        if qualifier:
            query.column = Column(family=family, qualifier=qualifier)
        else:
            query.family = family

        return query
