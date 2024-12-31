from typing import Literal, List
import json

from utils import get_current_datetime

DATABASE_PATH = "data.json"

# task status choices
TODO = "todo"
IN_PROGRESS = "in-progress"
DONE = "done"
ALL = "all"

# display
SPACE = " \t "


# database management
def load_database(path: str) -> dict[str, dict]:
    "Load database from PATH."
    try:
        with open(path, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = {}
    except FileNotFoundError:
        data = {}

    return data


def save_database(database: dict[str, dict], path: str) -> None:
    "Save DATABASE to PATH."
    with open(path, "w") as file:
        json.dump(database, file, indent=4)


# task management
def add_task(database: dict[str, dict], description: str) -> dict[str, dict]:
    "Add task DESCRIPTION to DATABASE."

    def new_task(id):
        now = get_current_datetime()
        return {
            "id": id,
            "created": now,
            "updated": now,
            "status": "todo",
            "description": description,
        }

    if database:
        next_id = len(database) + 1
        database[f"{next_id}"] = new_task(next_id)
        return database
    else:
        next_id = 1
        return {f"{next_id}": new_task(next_id)}


def delete_task(database: dict[str, dict], id: str) -> dict[str, dict]:
    "Delete task by ID from DATABASE."
    if id in database:
        del database[f"{id}"]

    return database


def update_task(database: dict[str, dict], id: str, **kwargs) -> dict[str, dict]:
    "Update task DESCRIPTION by ID in DATABASE."
    if id in database:
        task_data = database[f"{id}"]
        database[f"{id}"] = task_data | {
            **kwargs,
            "updated": get_current_datetime(),
        }
        return database
    else:
        return add_task(database, kwargs["description"])


# filter
def filter_tasks_by_status(
    database: dict[str, dict], status: Literal["all", "done", "in-progress", "todo"] = "all"
) -> List[dict]:
    "Filter tasks by STATUS"
    if status == ALL:
        return list(database.values())
    return list(filter(lambda t: t["status"] == status, database.values()))


def list_tasks(
    database: dict[str, dict],
    status: Literal["all", "done", "in-progress", "todo"] = "all",
) -> None:
    "List tasks in DATABASE matching STATUS."

    display_headers = ["id", "description", "status", "created", "updated"]
    status = status or "all"
    tasks = filter_tasks_by_status(database, status)

    def print_headers():
        for h in display_headers:
            print(h.upper(), end=SPACE)

        print()

    def print_tasks():
        def print_task(t):
            for h in display_headers:
                print(t[h], end=SPACE)

        for task in tasks:
            print_task(task)
            print()

    print_headers()
    print_tasks()


def mark_in_progress_task(database: dict[str, dict], id: str) -> dict[str, dict]:
    "Mark task by ID in DATABASE as 'in-progress'."
    if id in database:
        return update_task(
            database, id, **{"status": IN_PROGRESS, "updated": get_current_datetime()}
        )

    return database


def mark_done_task(database: dict[str, dict], id: str) -> dict[str, dict]:
    "Mark task by ID in DATABASE as 'done'."
    if id in database:
        return update_task(database, id, **{"status": DONE, "updated": get_current_datetime()})

    return database
