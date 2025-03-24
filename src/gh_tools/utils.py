import json
from rich import print
from rich.table import Table
from rich.syntax import Syntax
from subprocess import getoutput

def show_git_status():
    status_output = getoutput("git status -s")
    print("[bold]Git Status:[/bold]")
    
    table = Table(show_header=False, box=None)
    table.add_column("Status", style="cyan", width=4)
    table.add_column("File", style="magenta")
    
    for line in status_output.split('\n'):
        if line.strip():
            status, filename = line.split(maxsplit=1)
            table.add_row(status.strip(), filename.strip())
    
    print(table)

def show_git_log():
    log_output = getoutput(
        "git log --pretty=format:'%C(auto)%h %C(blue)%ad %C(green)%an%C(auto)%d %s' --date=short -10"
    )
    print(Syntax(log_output, "bash", theme="monokai", line_numbers=False))


def read_gitmoji_map():
    with open("gh_tools/src/gh_tools/gitmoji.json", "r",  encoding='utf-8') as f:
        return json.load(f)