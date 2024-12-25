from typing import Literal, Callable


def main() -> None:
    pass


# database management
def load_database(path: str) -> dict[str, dict]:
    "Load database from PATH."
    pass


def save_database(database: dict[str, dict], path: str) -> None:
    "Save DATABASE to PATH."
    pass


# query management
def get_supported_queries() -> dict[str, dict]:
    "Dict of supported queries."
    pass


def get_querie(supported_queries: dict[str, dict]) -> tuple[Callable, dict]:
    pass


# task management
def add_task(database: dict[str, dict], description: str) -> None:
    "Add task DESCRIPTION to DATABASE."
    pass


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
    pass


def mark_in_progress_task(database: dict[str, dict], id: str) -> None:
    "Mark task by ID in DATABASE as 'in-progress'."
    pass


def mark_done_task(database: dict[str, dict], id: str) -> None:
    "Mark task by ID in DATABASE as 'done'."
    pass
