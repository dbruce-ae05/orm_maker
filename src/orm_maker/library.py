from pathlib import Path
from typing import Any

import click
import polars


def get_next_file_name(path: Path) -> Path:
    """Get Next File Name"""

    if not path.exists():
        return path

    parent = path.parent
    stem = path.stem
    suffix = path.suffix
    counter = 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_path = parent.joinpath(new_name)

        if not new_path.exists():
            return new_path
        counter += 1


def get_nested_item(data: dict, keys: list) -> Any:
    current = data

    for key in keys:
        try:
            current = current[key]
        except (KeyError, TypeError):
            return None
        return current


def set_nested_item(data: dict, keys: list, value: Any) -> dict:
    if not keys:
        return value
    if len(keys) == 1:
        data[keys[0]] = value
        return data
    if keys[0] not in data:
        data[keys[0]] = {}

    data[keys[0]] = set_nested_item(data[keys[0]], keys[1:], value)
    return data


def replace_chars(target: str, find: str = r" !@#$%^&*()_+-=[]\{}|;':\",./<>?", replace: str = "_") -> str:
    result = str(target)
    for c in find:
        result = result.replace(c, replace)
    return result


def click_secho_dataframe(df: polars.DataFrame):
    with polars.Config(
        tbl_cols=-1,
        tbl_rows=-1,
        tbl_hide_dataframe_shape=True,
        tbl_width_chars=1000,
        fmt_str_lengths=1000,
        tbl_hide_column_data_types=True,
    ):
        click.secho(df)
