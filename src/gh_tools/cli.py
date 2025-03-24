# import yaml
import typer
import subprocess
from rich.console import Console
from .github_api import git_add, git_commit, git_push
from .utils import show_git_status, show_git_log, read_gitmoji_map

app = typer.Typer()
console = Console()

@app.command()
def add(path: str = typer.Argument(".", help="Files to add")):
    """Stage changes with git add"""
    git_add(path)

@app.command()
def commit(
    message: str = typer.Argument(..., help="Commit message"),
    type: str = typer.Option("chore", "--type", "-t", help="Commit type (feat|fix|docs...)"),
    cz: bool = typer.Option(False, help="Use commitizen interactive mode")
):
    """Commit changes with gitmoji"""
    if cz:
        subprocess.run(["cz", "commit"], shell=True)
    else:
        gitmoji_map = read_gitmoji_map()
        git_commit(message, type, gitmoji_map)

@app.command()
def push(
    branch: str = typer.Option(None, "--branch", "-b", help="Target branch"),
    force: bool = typer.Option(False, "--force", "-f", help="Force push")
):
    """Push to remote with visual feedback"""
    cmd = "git push --force" if force else None
    git_push(branch if not force else None)

@app.command()
def status():
    """Show rich-formatted git status"""
    show_git_status()

@app.command()
def log():
    """Display commit history with rich"""
    show_git_log()



if __name__ == "__main__":
    app()