#!/bin/python3

from pathlib import Path

from git.repo import Repo

ASSETS_DIR = Path(Repo(__file__, search_parent_directories=True).git.rev_parse('--show-toplevel')) / '.assets'

# EOF
