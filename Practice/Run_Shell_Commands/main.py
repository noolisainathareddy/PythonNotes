import subprocess

def run_command(cmd: list[str]) -> str:
    results = subprocess.run(cmd, capture_output=True, text=True)
    if results.returncode !=0:
        raise RuntimeError(
            f'Command {cmd}, Error message:   {results.stderr.strip()}'
        )

    return results.stdout.strip()

output = run_command(["df", "-h", "/"])

print(output)


