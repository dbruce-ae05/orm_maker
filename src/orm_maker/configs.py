from pathlib import Path
from typing import Any

import yaml

from orm_maker.library import get_nested_item, set_nested_item


def get_configs_path() -> Path:
    return Path(__file__).parent.joinpath("configs.yaml")


def get_configs() -> dict:
    configs: dict
    with open(get_configs_path(), "r") as file:
        configs = yaml.safe_load(file)

    return configs


def set_config(keys: list, value: str) -> bool:
    configs: dict = get_configs()

    configs = set_nested_item(configs, keys, value)

    with open(get_configs_path(), "w") as file:
        yaml.dump(configs, file)
        return True

    return False


def get_config(keys: list) -> Any:
    return get_nested_item(get_configs(), keys)
