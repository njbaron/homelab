from pathlib import Path
import argparse
import sys
from enum import Enum, auto
import shutil


def is_file(argument):
    path = Path(argument)
    if path.parent.exists() and not path.exists():
        path.touch()
    if not path.is_file():
        raise argparse.ArgumentError(f"{argument} is not a file")
    return path


def parse_args():
    parser = argparse.ArgumentParser(description="List fish in aquarium.")
    parser.add_argument("file_path", type=is_file, help="the path to the file to modify")
    parser.add_argument("argument", type=str, help="the argument to search for")
    parser.add_argument("value", type=str, help="the argument value you want")
    parser.add_argument("--backup", action="store_true", help="backup the file if modifying")
    return parser.parse_args()


class SearchState(Enum):
    NEEDS_UPDATE = auto()
    OK = auto()


def main():
    args = parse_args()

    file_path: Path = args.file_path

    file_content: str = file_path.read_text().strip()
    file_split = file_content.split()

    state = SearchState.NEEDS_UPDATE
    new_content = []
    for item in file_split:
        item_split = item.split("=")
        if args.argument not in item_split[0]:
            new_content.append(item)
            continue

        if len(item_split) != 2:
            raise Exception(f"Len of {item_split} is not 2")
        if args.value == item_split[-1]:
            state = SearchState.OK
            continue
        state = SearchState.NEEDS_UPDATE

    if state == SearchState.NEEDS_UPDATE:
        if args.backup:
            shutil.copyfile(file_path, file_path.parent / f"{file_path.name}.bu")
        new_content.append(f"{args.argument}={args.value}")
        file_path.write_text(" ".join(new_content))
        print("changed")
    else:
        print("ok")


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("error")
        print(ex, file=sys.stderr)
        exit(1)
