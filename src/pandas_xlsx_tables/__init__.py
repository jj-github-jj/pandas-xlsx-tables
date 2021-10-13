import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "pandas-xlsx-tables"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

from .from_xlsx_tables import xlsx_table_to_df, xlsx_tables_to_dfs
from .to_xlsx_table import df_to_xlsx_table, dfs_to_xlsx_tables

__all__ = [
    "df_to_xlsx_table",
    "dfs_to_xlsx_tables",
    "xlsx_table_to_df",
    "xlsx_tables_to_dfs",
]