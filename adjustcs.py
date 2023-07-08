# 仅改变4,5,6,7k的columnstart
import sys
from math import floor
from os import system

s = ""


def get_after(start=0):
    end = s.find("\n", start)
    end2 = s.find("//", start)
    if end2 != -1:
        temp = min(end, end2)
    else:
        temp = end
    return s[start:temp].replace("ColumnStart:", "").replace("ColumnWidth:", "")


try:
    with open("skin.ini", "r") as fin:
        s = fin.read()
except FileNotFoundError:
    print("FileNotFound")
    system("pause")
    sys.exit(0)
maniastart = s.find("[Mania]")
kstart = maniastart
for k in range(4, 8):
    kstart = s.find("Keys: " + str(k), kstart + 2)
    replace_tag1 = s.find("ColumnStart:", kstart)
    replace_tag2 = s.find("ColumnWidth:", kstart)
    columnstart = int(get_after(replace_tag1).strip())
    width = sum(map(int, get_after(replace_tag2).strip().split(",")))
    if k == 4:
        print("当前中线为: The current middle position is: ", columnstart + width / 2)
        cin = int(input("你需要设置的中线为: The middle position you need to set is: "))
    start2 = int(floor(cin - width / 2))
    if start2 < 0:
        print(
            f"{str(k)}k的初始位置小于0！不进行调整. \nThe initial position of {str(k)}k is less than 0! No adjustment will be made."
        )
        continue
    s = s[:replace_tag1] + s[replace_tag1:].replace(str(columnstart), str(start2), 1)
    print(
        f"{str(k)}k 的 ColumnStart 已替换为 {start2}. \nThe ColumnStart of {str(k)}k has been replaced with {start2}."
    )

with open("skin.ini", "w") as fout:
    fout.write(s)
system("pause")
