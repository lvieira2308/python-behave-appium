import time
import os
import shutil
import sys
from pathlib import Path
import loguru
from paver.easy import *
from paver.setuputils import setup

setup(
    name="behave-appium",
    version="1.0",
    author=["Luis Vieira"],
    author_email="",
    description="Behave integration with Appium",
    license="MIT",
    packages=['features']
)

def run_behave(platform):
    sh(f"pkill -f 4725 || true")
    sh(f"appium -p 4725 --use-plugins=images,appium-reporter-plugin --log-no-colors --log-timestamp --command-timeout 60 > appium.log 2>&1 &")
    time.sleep(5)

    try:

        sh(f"behave -D PLATFORM={platform.lower()}")
    except Exception as e:
        print("Error")
        print(e)
        ""

    sh(f"pkill -f 4725 || true")

@task
@consume_nargs(1)
def run_tests(args):
  run_behave(args[0])
