import subprocess
import sys

from fastcs_kds_legato import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "fastcs_kds_legato", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
