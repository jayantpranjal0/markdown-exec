import sys
import warnings
from contextlib import suppress
from io import StringIO
from runpy import run_module

old_argv = list(sys.argv)
sys.argv = ["mkdocs"]
old_stderr = sys.stderr
sys.stderr = StringIO()
warnings.filterwarnings("ignore", category=RuntimeWarning)
with suppress(SystemExit):
    run_module("mkdocs", run_name="__main__")
output = sys.stderr.getvalue()
sys.stderr = old_stderr
sys.argv = old_argv

print(f"```\n{output}\n```")
