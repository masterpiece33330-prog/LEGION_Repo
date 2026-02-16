import os
import json
import platform
import time
import uuid

# LEGION v3.0 Node Logic
# T3 Tier: Ephemeral Node (GitHub Actions Runner)

def get_hardware_specs():
    """서버의 하드웨어를 탈탈 털어서 스펙을 확인합니다."""
    specs = {
        "node_id": str(uuid.uuid4()),
        "os": platform.system(),
        "cpu_cores": os.cpu_count(),
        "architecture": platform.machine(),
        # 무료 티어라 GPU는 없지만, 있는 척 스캔은 시도합니다.
        "gpu_available": False 
    }
    return specs

def connect_to_overmind(specs):
    """가상의 제어 서버(Overmind)에 접속을 시도합니다."""
    print(f"\n[SYSTEM] LEGION T3 Node ({specs['node_id']}) Booting...")
    print(f"[HARDWARE] CPU: {specs['cpu_cores']} Cores | Arch: {specs['architecture']}")

    # 실제 연산 부하 테스트 (행렬 곱셈 시뮬레이션)
    print("[COMPUTE] Performing Benchmark (Matrix Multiplication)...")
    start_time = time.time()
    # CPU를 실제로 달구는 연산 (가짜가 아님을 증명)
    j = 0
    for i in range(10000000):
        j += i
    duration = time.time() - start_time

    print(f"[BENCHMARK] Score: {duration:.4f}s (Lower is better)")
    print(f"[NETWORK] Cloudflare Tunnel: Attempting handshake...")
    time.sleep(1) # 연결 시뮬레이션
    print(f"[STATUS] READY. Waiting for task blocks via Water-Filling Algo.")

if __name__ == "__main__":
    specs = get_hardware_specs()
    connect_to_overmind(specs)

