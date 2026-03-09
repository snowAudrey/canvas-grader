# Git Commands Quick Reference

## Saving Progress and Pushing to GitHub

### 1. Check what files changed
```bash
git status
```

### 2. Stage all changes
```bash
git add .
```

Or stage a specific file:
```bash
git add filename.py
```

### 3. Verify .env is NOT being committed (optional safety check)
```bash
git status
```
Look for `.env` in the green list - it should NOT appear there.

### 4. Commit with a message
```bash
git commit -m "Description of what you changed"
```

### 5. Push to GitHub
```bash
git push
```

---

## Common Git Commands

### See commit history
```bash
git log
```
Press `q` to exit the log view.

### Check which files Git is tracking
```bash
git ls-files
```

### Undo changes to a file (before committing)
```bash
git checkout -- filename.py
```

### See what remote repository you're connected to
```bash
git remote -v
```

---

## Tips

- Commit often with clear messages
- Always check `git status` before committing
- `.env` should NEVER appear in `git status` output
- Write commit messages that describe WHAT changed, not just "update" or "changes"

## Good Commit Message Examples

- "Add assignment filtering logic"
- "Fix bug in grading function"
- "Add documentation to README"
- "Implement dry run mode for testing"