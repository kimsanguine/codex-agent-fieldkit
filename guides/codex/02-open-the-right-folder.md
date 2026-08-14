# 02. Open The Right Folder

Most early Codex failures are folder failures.

## Good Folder

A good folder has:

- one project goal
- local instructions
- runnable commands
- test or validation files
- no private dumps

## Bad Folder

A bad folder has:

- many unrelated projects
- copied private exports
- hidden dependencies
- no README
- no validation path

## Prompt

```text
Confirm the current working directory.
List the files that define the project contract.
If this is not the right project folder, stop and tell me.
```

## Check

From a terminal:

```bash
pwd
find . -maxdepth 2 -type f | sort
```
