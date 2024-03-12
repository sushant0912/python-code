# print("2D same x and y")
# for i in range(1,6):
#     print(""*5)

print("2D same x and y")
row=int(input("Enter row:"))
column=int(input("Enter column:"))
for i in  range(1,row+1):
    for j in range(1,column+1):
        print("*",end="")
    print()
