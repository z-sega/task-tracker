#!/usr/bin/env python3
import argparse

from task import (
    load_database,
    save_database,
    list_tasks,
    add_task,
    update_task,
    delete_task,
    mark_in_progress_task,
    mark_done_task,
    DATABASE_PATH,
)


def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI for tracking tasks.", prog="task-cli"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List all tasks (should support filters: maybe use options)
    parser_list_all = subparsers.add_parser("list", help="List all tasks")
    parser_list_all.add_argument("optional_status", nargs="?", help="Filter task by status")

    # Add a task
    parser_add = subparsers.add_parser("add", help="Add new task")
    parser_add.add_argument("description", help="Description of task")

    # Update a task
    parser_update = subparsers.add_parser("update", help="Update existing task")
    parser_update.add_argument("id", help="ID of task")
    parser_update.add_argument("description", help="Description of task")

    # Delete a task
    parser_delete = subparsers.add_parser("delete", help="Delete task")
    parser_delete.add_argument("id", help="ID of task")

    # Mark task as done
    parser_mark_done = subparsers.add_parser("mark_done", help="Mark task as done")
    parser_mark_done.add_argument("id", help="ID of task")

    # Mark task as in-progress
    parser_mark_in_progress = subparsers.add_parser(
        "mark_in_progress", help="Mark task as in-progress"
    )
    parser_mark_in_progress.add_argument("id", help="ID of task")

    args = parser.parse_args()

    match args.command:
        case "list":
            database = load_database(DATABASE_PATH)
            list_tasks(database, args.optional_status)
        case "add":
            db = load_database(DATABASE_PATH)
            updated_db = add_task(db, args.description)
            save_database(updated_db, DATABASE_PATH)
            print(f"Task added successfully (ID: {len(updated_db)})")
        case "update":
            database = load_database(DATABASE_PATH)
            updated_db = update_task(database, args.id, **{"description": args.description})
            save_database(updated_db, DATABASE_PATH)
        case "delete":
            database = load_database(DATABASE_PATH)
            updated_db = delete_task(database, args.id)
            save_database(updated_db, DATABASE_PATH)
        case "mark_in_progress":
            database = load_database(DATABASE_PATH)
            updated_db = mark_in_progress_task(database, args.id)
            save_database(updated_db, DATABASE_PATH)
        case "mark_done":
            database = load_database(DATABASE_PATH)
            updated_db = mark_done_task(database, args.id)
            save_database(updated_db, DATABASE_PATH)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
