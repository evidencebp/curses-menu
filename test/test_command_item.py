import pathlib
import sys

import pytest

from cursesmenu.items import CommandItem

pytestmark = pytest.mark.usefixtures(
    "mock_cursesmenu_curses",
    "mock_clear",
    "mock_externalitem_curses",
)

test_file_path = pathlib.Path("test.txt")


@pytest.fixture
def create_item():
    if sys.platform.startswith("win"):  # pragma: no cover
        return CommandItem(
            "create_item",
            "echo",
            arguments=["hello"],
            stdout_filepath=test_file_path,
        )
    else:
        return CommandItem("create_item", "echo hello", stdout_filepath=test_file_path)


@pytest.fixture
def delete_item():
    if sys.platform.startswith("win"):  # pragma: no cover
        return CommandItem("delete_item", "del", arguments=[f"{str(test_file_path)}"])
    else:
        return CommandItem("delete_item", f"rm {str(test_file_path)}", ["-f"])


@pytest.fixture
def exit_item():
    if sys.platform.startswith("win"):  # pragma: no cover
        return CommandItem("return_command_item", "exit", arguments=["42"])
    else:
        return CommandItem("return_command_item", "exit 42")


def test_return(exit_item: CommandItem):
    exit_item.action()

    assert exit_item.get_return() == 42


def test_create(create_item: CommandItem, delete_item: CommandItem):
    create_item.action()
    assert create_item.get_return() == 0
    assert test_file_path.is_file()
    with open(test_file_path, "r") as f:
        assert f.read().strip() == "hello"
    delete_item.action()
    assert delete_item.get_return() == 0
    assert not test_file_path.exists()
