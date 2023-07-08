"""
This script makes the same incremental or decremental adjustments to all ComboPosition and ScorePosition.
The script does not perform position out-of-bounds checks.
"""
import re
import sys
from os import system

while True:
    try:
        c = int(
            input(
                "Please enter your desired increment of ScorePosition and ComboPosition, for example: -10: \n请输入你想要的 ScorePosition & ComboPosition 增量, 例如: -10:\n"
            )
        )
        break
    except ValueError:
        print("Please enter a number")

try:
    with open("skin.ini", "r") as fin:
        s = fin.read()
except FileNotFoundError:
    print("FileNotFound")
    system("pause")
    sys.exit(0)

s = re.sub(
    "ScorePosition:\s(\d+)",
    lambda match: "ScorePosition: " + str(int(match.group(1)) + c),
    s,
)
s = re.sub(
    "ComboPosition:\s(\d+)",
    lambda match: "ComboPosition: " + str(int(match.group(1)) + c),
    s,
)

with open("skin.ini", "w") as fout:
    fout.write(s)
print("adjust position success.")
system("pause")
