from typing import Mapping, List, Optional

import grpc
from google.protobuf.wrappers_pb2 import Int32Value, StringValue, Int64Value
from hbase_pb2 import Get, Columns, Table, Scan
from hbase_pb2_grpc import HBaseServiceStub
from result import Result


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
            columns: Mapping[str, List[str]] = None,
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

        query = Get(
            table=Table(name=table_name, namespace=table_namespace),
            row=row,
            columns={f: Columns(columns=c) for f, c in columns.items()},
            max_versions=_max_versions,
            min_time=_min_time,
            max_time=_max_time
        )

        return Result(self._client.get(query))

    def scan(
            self,
            table_name: str,
            table_namespace: str = "default",
            start_row: Optional[str] = None,
            stop_row: Optional[str] = None,
            prefix: Optional[str] = None,
            columns: Mapping[str, List[str]] = None,
            min_time: Optional[int] = None,
            max_time: Optional[int] = None,
            max_versions: Optional[int] = None
    ) -> 'Result':

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

        if max_versions is not None:
            _max_versions = Int32Value(value=max_versions)
        else:
            _max_versions = None

        query = Scan(
            table=Table(name=table_name, namespace=table_namespace),
            start_row=_start_row,
            stop_row=_stop_row,
            prefix=_prefix,
            columns={f: Columns(columns=c) for f, c in columns.items()},
            min_time=_min_time,
            max_time=_max_time,
            max_versions=_max_versions
        )

        return Result(self._client.scan(query))
