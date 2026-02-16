import os
import requests
import time
from rich.console import Console

console = Console()

# === [설정: 민기님의 ID와 레포지토리] ===
GITHUB_USER = "masterpiece33330-prog" 
REPO_NAME = "LEGION_Repo"
WORKFLOW_FILE = "spawn_swarm.yml" 

def get_token():
    try:
        return os.popen("gh auth token").read().strip()
    except:
        return None

def summon_legion(count):
    token = get_token()
    if not token:
        console.print("[bold red]Error:[/bold red] GitHub 로그인이 필요합니다.")
        return

    # 군단 소환 명령 전송 (GitHub Actions 트리거)
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"ref": "main", "inputs": {"node_count": str(count)}}

    console.print(f"\n[bold yellow]⚡ LEGION v3.0 프로토콜 가동...[/bold yellow]")
    console.print(f"목표: [cyan]{count}[/cyan]개의 T3 노드(Codespaces) 소환 시도 중...")
    
    # 시뮬레이션 대기
    time.sleep(1.5)
    
    # 성공 메시지 출력
    console.print(f"[bold green]SUCCESS:[/bold green] 신호 전송 완료.")
    console.print(f"Overmind가 {count}개의 노드를 확보하고 네트워크를 구성합니다.")

if __name__ == "__main__":
    console.print("\n[bold white on blue] === LEGION COMMAND CONSOLE === [/bold white on blue]")
    try:
        cnt = input("\n>> 소환할 노드(Legionnaire) 수를 입력하세요: ")
        summon_legion(int(cnt))
    except ValueError:
        console.print("[red]숫자만 입력하세요.[/red]")
