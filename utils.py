from datetime import datetime


def get_current_datetime():
    "Current datetime."
    return datetime.now().isoformat()


def task_in_database(s, ds):
    "True if S describes any task in DS."

    def task_is_entry(s, d):
        "True if S describes task D."
        return s == d["description"]

    return any(list(map(lambda d: task_is_entry(s, d), ds.values())))
