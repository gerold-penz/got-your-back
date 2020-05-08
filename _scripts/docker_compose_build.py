#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import subprocess

THISDIR = os.path.dirname(os.path.realpath(__file__))
DOCKERDIR = os.path.abspath(os.path.join(THISDIR, "..", "docker"))


def main():
    print("Docker-Compose RUN\n")

    try:
        returncode = subprocess.call(
            ["docker-compose", "build"],
            cwd=DOCKERDIR,
            env=os.environ,
            shell=sys.platform.startswith("win")
        )
        if returncode != 0:
            input("Press ENTER to continue...")
    except KeyboardInterrupt:
        pass

    print("Fertig!")
    print()


if __name__ == "__main__":
    main()
