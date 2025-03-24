import subprocess
from rich import print
from rich.panel import Panel
from typing import Optional
from rich.console import Console

console = Console()

def git_add(path: str = ".") -> bool:
    result = subprocess.run(["git", "add", path], capture_output=True, text=True)
    if result.returncode == 0:
        console.print(f"[bold green]✅ Added changes:[/bold green] {path} or all")
        # print(f"[bold green]✅ Added changes:[/bold green] {path or 'all'}")
        return True
    # print(f"[bold red]Error adding files:[/bold red]\n{result.stderr}")
    console.print(f"[bold red]Error adding files:[/bold red]\n{result.stderr}")
    return False

def git_commit(
        message: str, 
        emoji_type: str,
        emoji_map: Optional[dict] = None
) -> bool:
    emoji_map = emoji_map or {}
    emoji = emoji_map.get(emoji_type, "🔧")
    cmd = f'git commit -m "{emoji} {emoji_type}: {message}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        console.print(Panel.fit(
            f"[bold green]{emoji} Committed:[/bold green] {message}",
            title="Commit Success",
            border_style="green"
        ))
        return True
    console.print(f"[bold red]Commit failed:[/bold red]\n{result.stderr}")
    return False

def git_push(branch: Optional[str] = None) -> bool:
    branch = branch or subprocess.getoutput("git branch --show-current")
    cmd = ["git", "push", "origin", branch]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        console.print(f"[bold green]🚀 Pushed to [cyan]{branch}[/cyan][/bold green]")
        return True
    console.print(f"[bold red]Push failed:[/bold red]\n{result.stderr}")
    return False