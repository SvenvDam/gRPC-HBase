from typing import Iterator
import pandas as pd
from hbase_pb2 import Cell


class Result:
    def __init__(self, cells: Iterator[Cell]):
        self._cells = cells

    def raw(self) -> Iterator[Cell]:
        return self._cells

    def get_cell_df(self) -> pd.DataFrame:
        """
        Create a DataFrame containing values from all received cells.

        row     | family    | qualifier | value     | timestamp |
        --------|-----------|-----------|-----------|-----------|
        key1    | cf1       | col1      | b'val0'   | 1         |
        key1    | cf1       | col1      | b'val1'   | 2         |
        key1    | cf1       | col2      | b'val2'   | 2         |
        key1    | cf2       | col3      | b'val3'   | 2         |
        key2    | cf1       | col2      | b'val4'   | 2         |
        key2    | cf2       | col3      | b'val5'   | 2         |
        """
        return pd.DataFrame([self._cell_to_dict(c) for c in self._cells])

    def get_row_df(self) -> pd.DataFrame:
        """
        Get the latest value per user/column and pivot on the columns.
        This results in a DataFrame more suited for most operations.
        Missing values are imputed with NaN

        row     | cf1:col1  | cf1:col2  | cf2:col3  |
        --------|-----------|-----------|-----------|
        key1    | b'val1'   | b'val2'   | b'val3'   |
        key2    | NaN       | b'val4'   | b'val5'   |
        """
        cell_df = self.get_cell_df()

        # filters out cells which are no the most recent value
        idx = cell_df.groupby(["row", "column"])["timestamp"].transform(max) == cell_df["timestamp"]

        return cell_df[idx].pivot(index="row", columns="column", values="value")

    @staticmethod
    def _cell_to_dict(cell: Cell) -> dict:
        return {
            "row": cell.row,
            "column": cell.family + ":" + cell.qualifier,
            "value": cell.value,
            "timestamp": cell.timestamp
        }

