# Understanding the Git Workflow

## The Basic Workflow

The Git workflow covered in Day 1 consists of five stages:

**Edit → Check → Stage → Commit → Push**

### 1. Edit

Write new code or modify existing files.

### 2. Check

Use:

```bash
git status
```

This displays the current state of the working directory and staging area.

### 3. Stage

Use:

```bash
git add solution.py
```

This selects the changes to include in the next commit.

### 4. Commit

Use:

```bash
git commit -m "Add calculation function"
```

This records the staged changes in the local repository history.

### 5. Push

Use:

```bash
git push
```

This sends local commits to the configured remote repository.

## Important Git Commands

| Command | Purpose |
|---|---|
| `git --version` | Checks Git installation |
| `git status` | Checks repository status |
| `git add filename` | Stages file changes |
| `git add .` | Stages changes in the current directory |
| `git commit -m "message"` | Records staged changes |
| `git log` | Displays commit history |
| `git push` | Sends commits to remote |
| `git pull` | Fetches and integrates remote changes |

## Important Notes

- Saving a file is different from committing it.
- Staging prepares changes for a commit.
- Committing saves a snapshot locally.
- Pushing sends commits to a remote repository.

## Conclusion

Understanding this workflow helps developers manage their code and maintain an organized project history.
