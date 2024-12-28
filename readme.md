# Table of Contents

1.  [Project](#org515ed3c)
2.  [Usage](#orge699002)
3.  [Automation](#orgc2a0ae9)
    1.  [Pre-commit Hook](#orgaddbb07)
    2.  [Github Actions on Push and Pull Request](#org7425e90)
4.  [Testing](#orge12b0b1)

# Project

URL: <https://roadmap.sh/projects/task-tracker>

# Usage

```bash
    # Adding a new task
    task-cli add "Buy groceries"
    # Output: Task added successfully (ID: 1)

    # Updating and deleting tasks
    task-cli update 1 "Buy groceries and cook dinner"
    task-cli delete 1

    # Marking a task as in progress or done
    task-cli mark-in-progress 1
    task-cli mark-done 1

    # Listing all tasks
    task-cli list

    # Listing tasks by status
    task-cli list done
    task-cli list todo
    task-cli list in-progress
```

# Automation

## Pre-commit Hook

-   Check YAML
-   Fix end of file
-   Remove trailing-whitespace
-   Check format with black according to pyproject.toml
-   Lint with Ruff

## Github Actions on Push and Pull Request

-   Setup Python
-   Installs Dependencies
-   Lint with Ruff
-   Check format with Black
-   Run unit tests with pytest

# Testing

```bash

pytest

```
