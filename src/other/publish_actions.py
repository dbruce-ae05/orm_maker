import json

from orm_maker.info import APP_NAME_PATH, LOGGING_CONFIGURATION_PATH, PROJECT_ROOT, PYPROJECT, VERSION_PATH
from orm_maker.make_orm import make_orm_helper


def sync_version():
    version = PYPROJECT["project"]["version"]
    message = f'__version__ = "{version}"'
    with open(VERSION_PATH, "w") as f:
        f.write(message)
    return message


def sync_logging_level() -> str:
    log_level = PYPROJECT["tool"]["orm_maker"]["logging_level"]
    message = f"LOGGING_LEVEL = {log_level}"
    with open(LOGGING_CONFIGURATION_PATH, "r") as f:
        config = json.load(f)

    config["loggers"]["root"]["level"] = f"{log_level}"

    with open(LOGGING_CONFIGURATION_PATH, "w") as f:
        json.dump(config, f, indent=4)

    return message


def sync_application_name() -> str:
    app_name = PYPROJECT["project"]["name"]
    message = f'APP_NAME = "{app_name}"'
    with open(APP_NAME_PATH, "w") as f:
        f.write(message)
    return message


def sync_with_pyproject() -> list:
    results = list()
    results.append(sync_version())
    # results.append(sync_logging_level())
    results.append(sync_application_name())
    return results


def make_example() -> None:
    input = PROJECT_ROOT.joinpath("example").joinpath("example.csv")
    output = PROJECT_ROOT.joinpath("example").joinpath("example.py")
    make_orm_helper(input, output, accept_changes=True, write_changes=False, overwrite=True)
