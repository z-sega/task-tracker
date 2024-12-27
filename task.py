from typing import Literal, Callable
from datetime import datetime
import json

DATABASE_PATH = "data.json"


def main() -> None:
    pass


# database management
def load_database(path: str) -> dict[str, dict]:
    "Load database from PATH."
    try:
        with open(path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    return data


def save_database(database: dict[str, dict], path: str) -> None:
    "Save DATABASE to PATH."
    with open(path, "w") as file:
        json.dump(database, file, indent=4)


# query management
def get_supported_queries() -> dict[str, dict]:
    "Dict of supported queries."
    pass


def get_querie(supported_queries: dict[str, dict]) -> tuple[Callable, dict]:
    pass


# task management
def add_task(database: dict[str, dict], description: str) -> None:
    "Add task DESCRIPTION to DATABASE."

    def new_task(id):
        now = datetime.now().isoformat()
        return {
            "id": id,
            "created": now,
            "updated": now,
            "status": "todo",
            "description": description,
        }

    if database:
        next_id = len(database) + 1
        save_database(database.update({f"{next_id}": new_task(next_id)}), DATABASE_PATH)
    else:
        next_id = 1
        save_database({}.update({f"{next_id}": new_task(next_id)}), DATABASE_PATH)


def delete_task(database: dict[str, dict], id: str) -> None:
    "Delete task by ID from DATABASE."
    pass


def update_task(database: dict[str, dict], id: str, description: str) -> None:
    "Update task DESCRIPTION by ID in DATABASE."
    pass


def list_task(
    database: dict[str, dict],
    status: Literal["all", "done", "in-progress", "todo"] = "all",
) -> None:
    "List tasks in DATABASE matching STATUS."
    match status:
        case "done":
            print("list-done")
        case "in-progress":
            print("list-in-progress")
        case "todo":
            print("list-todo")
        case _:
            print("list-all")


def mark_in_progress_task(database: dict[str, dict], id: str) -> None:
    "Mark task by ID in DATABASE as 'in-progress'."
    pass


def mark_done_task(database: dict[str, dict], id: str) -> None:
    "Mark task by ID in DATABASE as 'done'."
    pass
