#!/usr/bin/env python3
"""Simple Project OS for managing projects and tasks."""
import argparse
import yaml
from pathlib import Path
from datetime import date
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent / "projects"
BASE_DIR.mkdir(exist_ok=True)

def load_project(name):
    path = BASE_DIR / name / "project.yaml"
    if not path.exists():
        return {"name": name, "description": "", "status": "planning", "tasks": []}
    with open(path) as f:
        return yaml.safe_load(f)

def save_project(name, data):
    path = BASE_DIR / name / "project.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.safe_dump(data, f)

def add_project(args):
    data = load_project(args.name)
    if args.description:
        data["description"] = args.description
    save_project(args.name, data)
    print(f"Project '{args.name}' added/updated.")


def add_task(args):
    data = load_project(args.project)
    task = {
        "id": len(data.get("tasks", [])) + 1,
        "description": args.description,
        "status": "TODO",
        "created": str(date.today()),
    }
    data.setdefault("tasks", []).append(task)
    save_project(args.project, data)
    print(f"Task added to '{args.project}': {task}")


def update_task(args):
    data = load_project(args.project)
    for task in data.get("tasks", []):
        if task["id"] == args.id:
            task["status"] = args.status
            break
    else:
        print("Task not found")
        return
    save_project(args.project, data)
    print(f"Task {args.id} updated to {args.status}")


def list_tasks(args):
    data = load_project(args.project)
    for task in data.get("tasks", []):
        print(f"[{task['id']}] {task['status']} - {task['description']}")


def add_context(args):
    project_dir = BASE_DIR / args.project / "context"
    project_dir.mkdir(parents=True, exist_ok=True)
    dest = project_dir / Path(args.file).name
    shutil.copy(args.file, dest)
    print(f"Context file copied to {dest}")


def main():
    parser = argparse.ArgumentParser(description="Project OS")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("add-project", help="Create or update a project")
    p.add_argument("name")
    p.add_argument("description", nargs="?")
    p.set_defaults(func=add_project)

    p = sub.add_parser("add-task", help="Add a task to a project")
    p.add_argument("project")
    p.add_argument("description")
    p.set_defaults(func=add_task)

    p = sub.add_parser("update-task", help="Update task status")
    p.add_argument("project")
    p.add_argument("id", type=int)
    p.add_argument("status")
    p.set_defaults(func=update_task)

    p = sub.add_parser("list-tasks", help="List tasks in a project")
    p.add_argument("project")
    p.set_defaults(func=list_tasks)

    p = sub.add_parser("add-context", help="Add context file to a project")
    p.add_argument("project")
    p.add_argument("file")
    p.set_defaults(func=add_context)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
