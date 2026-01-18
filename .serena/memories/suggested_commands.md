# Suggested Commands

## Repository
- GitHub: tonuonu/MyLevel1Peregrine
- Use GitHub MCP API tools for all Git operations (not CLI)

## GitHub API (MCP tools)
- `github:create_branch` - create feature branch
- `github:push_files` - push file changes  
- `github:create_pull_request` - create PR
- `github:list_pull_requests` - view PRs
- `github:get_pull_request` - PR details
- `github:get_file_contents` - read files

## MkDocs Commands
```bash
# Install dependencies
pip install mkdocs-material

# Serve locally (http://127.0.0.1:8000)
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## File System (Darwin/macOS)
```bash
ls -la
find . -name "*.md"
grep -r "pattern" docs/
```