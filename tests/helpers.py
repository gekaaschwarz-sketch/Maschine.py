import os
import shutil
import sqlite3
import subprocess
from pathlib import Path
from typing import Tuple, List


def repo_root() -> Path:
    """Return repository root (one level up from tests/helpers.py)."""
    return Path(__file__).resolve().parents[1]


def copy_script(script_relpath: str, dst_dir: str) -> str:
    """Copy a script from the repo into dst_dir and return the dest filename."""
    src = repo_root() / script_relpath
    dst = Path(dst_dir) / Path(script_relpath).name
    shutil.copy2(src, dst)
    return str(dst.name)


def create_test_db(dst_path: str) -> str:
    """
    Create a fresh test DB at dst_path with a fleet_trucks table and deterministic test rows.
    Returns the dst_path string.
    """
    dst = Path(dst_path)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    conn = sqlite3.connect(str(dst))
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE fleet_trucks (id TEXT, fahrer_in TEXT, last INTEGER, payload_tons INTEGER DEFAULT 12)"
    )
    rows = [
        ("HH-99", "Maren", 5000, 12),
        ("HH-03", "Stefan", 4500, 12),
        ("HH-04", "Hannes", 3500, 12),
        ("HH-05", "Thomas", 6000, 12),
    ]
    cur.executemany("INSERT INTO fleet_trucks (id, fahrer_in, last, payload_tons) VALUES (?, ?, ?, ?)", rows)
    conn.commit()
    conn.close()
    return str(dst)


def run_script_in_cwd(script_name: str, cwd: str, inputs: str = None) -> subprocess.CompletedProcess:
    """
    Run a python script (present in cwd) via subprocess in the given cwd.
    Returns CompletedProcess with stdout/stderr/returncode.
    """
    cp = subprocess.run(
        ["python3", script_name],
        cwd=cwd,
        input=inputs,
        text=True,
        capture_output=True,
    )
    return cp


def query_count(db_path: str, table: str) -> int:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table};")
    c = cur.fetchone()[0]
    conn.close()
    return c


def fetch_all(db_path: str, query: str, params=()) -> List[Tuple]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows
