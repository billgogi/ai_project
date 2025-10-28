import subprocess
import  sys
from pathlib import Path

def run_python_file(working_directory, file_path, args=[]):
    workdir = Path(working_directory).resolve()
    target = (workdir / file_path).resolve()

    try:
        target.relative_to(workdir)
    except ValueError:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not target.is_file():
        return f'Error: File "{file_path}" not found.'
    
    if target.suffix != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed = subprocess.run(
        [sys.executable, str(target), *args],
        cwd=str(workdir),
        capture_output=True,
        text=True,
        timeout=30,
    )
        
        out, err, code = completed.stdout, completed.stderr, completed.returncode

        if out == "" and err == "":
            return "No output produced."

        result = f"STDOUT: {out}\nSTDERR: {err}"
        if code != 0:
            result += f"\nProcess exited with code {code}"
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"