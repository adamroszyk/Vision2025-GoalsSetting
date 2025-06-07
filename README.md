# Vision2025-GoalsSetting

This repository acts as a lightweight project OS. Use it to organise all your projects, track tasks and store context for future AI analysis.

## Directory layout

```
projects/
  <project>/
    project.yaml    # project metadata and tasks
    context/        # screenshots, analytics and other files
scripts/
  projectos.py      # command line tool
```

### Example project file
`projects/sample_project/project.yaml` shows the format used for storing data.

## CLI usage

Run the helper script to manage your projects:

```bash
python scripts/projectos.py add-project MyApp "Awesome mobile app"
python scripts/projectos.py add-task MyApp "Implement login"
python scripts/projectos.py update-task MyApp 1 InProgress
python scripts/projectos.py list-tasks MyApp
python scripts/projectos.py add-context MyApp ~/Desktop/screenshot.png
```

Tasks can represent features, experiments or ad campaigns. Update their `status` field (`TODO`, `InProgress`, `Done`, etc.) as you progress.

Use the `context` directory within each project to keep any relevant files such as screenshots, App Store analytics or advertising assets. This structure makes it simple for AI tools to read your data and provide insights on future improvements and marketing strategies.
