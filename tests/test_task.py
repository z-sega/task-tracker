from task import add_task, update_task, delete_task
from task import filter_tasks_by_status
from task import mark_in_progress_task, mark_done_task
from task import DONE, IN_PROGRESS, TODO, ALL

from utils import task_in_database

EMPTY_DB = {}
DB = {
    "1": {
        "id": 1,
        "created": "2024-12-27T13:23:25.041855",
        "updated": "2024-12-27T13:23:25.041855",
        "status": "done",
        "description": "wake up",
    },
    "2": {
        "id": 2,
        "created": "2024-12-27T13:23:25.041855",
        "updated": "2024-12-27T13:23:25.041855",
        "status": "in-progress",
        "description": "brush teeth",
    },
    "3": {
        "id": 3,
        "created": "2024-12-27T13:23:25.041855",
        "updated": "2024-12-27T13:23:25.041855",
        "status": "todo",
        "description": "shower",
    },
}


def test_add_task():
    # add to empty database
    new_task = "wake up"
    assert task_in_database(new_task, add_task({}, new_task))

    # add to non-empty database
    new_task = "brush teeth"
    assert task_in_database(new_task, add_task(add_task({}, "wake up"), new_task))


def test_update_task():
    # update empty database
    new_task = "wake up again"
    assert task_in_database(new_task, update_task({}, "1", description=new_task))

    # update non-empty database
    updated_db = update_task(
        add_task(add_task({}, "wake up"), "brush teeth"), "1", description=new_task
    )
    assert task_in_database(new_task, updated_db)
    assert len(updated_db) == 2
    assert "1" in updated_db
    assert updated_db["1"]["description"] == new_task


def test_delete_task():
    # delete from empty database
    before = {}
    after = delete_task({}, "1")
    assert before == after

    # delete from non-empty database
    before = add_task({}, "wake up")
    after = delete_task(before, "1")
    assert after == dict()


def test_filter_tasks_by_status():
    expected_done = [DB["1"]]
    expected_in_progress = [DB["2"]]
    expected_todo = [DB["3"]]
    expected_all = [DB["1"], DB["2"], DB["3"]]

    assert expected_done == filter_tasks_by_status(DB, DONE)
    assert expected_in_progress == filter_tasks_by_status(DB, IN_PROGRESS)
    assert expected_todo == filter_tasks_by_status(DB, TODO)
    assert expected_all == filter_tasks_by_status(DB, ALL)


def test_mark_in_progress_task():
    # empty | no-task-by-id
    updated_empty_db = mark_in_progress_task({}, "1")
    updated_db = mark_in_progress_task(DB, "50")
    assert updated_empty_db == {}
    assert updated_db == DB

    # non-empty
    updated_db = mark_in_progress_task(DB, "1")
    assert updated_db["1"]["status"] == IN_PROGRESS


def test_mark_done_task():
    # empty | no-task-by-id
    updated_empty_db = mark_done_task({}, "1")
    updated_db = mark_done_task(DB, "50")
    assert updated_empty_db == {}
    assert updated_db == DB

    # non-emtpy
    updated_db = mark_done_task(DB, "1")
    assert updated_db["1"]["status"] == DONE
