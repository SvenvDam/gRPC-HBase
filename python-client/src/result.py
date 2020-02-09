from typing import Iterator
import pandas as pd
from hbase_pb2 import Cell


class Result:
    def __init__(self, cells: Iterator[Cell]):
        self._cells = cells

    def raw(self) -> Iterator[Cell]:
        return self._cells

    def get_cell_df(self) -> pd.DataFrame:
        return pd.DataFrame([self._cell_to_dict(c) for c in self._cells])

    def get_row_df(self) -> pd.DataFrame:
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

