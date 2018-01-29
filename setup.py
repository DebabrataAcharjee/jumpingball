import cx_Freeze
import sys
import os

executables=[cx_Freeze.Executable("gameagain.py")]

cx_Freeze.setup(
    name="Dino",
    options={ "build_exe":{"packages":"pygame"}},
        description="Dino game",
    executables=executables
)