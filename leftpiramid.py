print("left-incremental triangle") 
row=int(input("Enter row count:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")   
    print()

print("left-incremental triangle") #rever triangle
row=int(input("Enter row count:"))
for i in range(1,row+1):
    for j in range(row,i-1,-1):
        print("*",end="")   
    print()

