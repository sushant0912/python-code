from ast import For
from re import I
from sqlite3 import Row
from tkinter.tix import COLUMN


print("(horizontal)row-wise printing")
for i in range(1, 6):
    print("*", end="")

print("\n(vertival)")



#print("2-D printing for row and column are same ")
# for i in range(1, 6):
#     print("*" * 5)


Row = int(input(" enter row count ="))
COLUMN = int(input("enter column count="))
for i in range(Row):
    for j in range(COLUMN):
       # print("*", end="")
       # print(i, end="")
        # print(j, end="")
        print(i )
    print()

print("Left incremental triangle")
Row = int(input(" enter row count ="))
COLUMN = int(input("enter column count="))
for i in range(Row):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("Left incremental triangle")
Row = int(input(" enter row count ="))
for   i in range(Row):
   for j in range(Row - i):
    print("*", end=" ")
    print()

    print("Right incremental triangle")
    Row = int(input(" enter row count ="))
    for   i in range(Row):
       for j in range(i + 1):
            print("*", end=" ")

    for j in range(i + i):
        print("*", end=" ")

        print()
       
    print("Pyramid------------")
    Row = int(input("enter row count"))
    for i in range(Row):
        for j in range(row - i):
            print(" ", end=" ")
        for k in range(i + 1):
            print("*", end=" ")
        print()0

print("Pyramid(Hill decremental)----------")
Row = int(input("enter row count="))
for i in range (Row, 0, -1):
    for j in range(i):
        print(" ", end=" ")
    for k in range(Row - i + 1):
        print("*", end=" ")
    print()
