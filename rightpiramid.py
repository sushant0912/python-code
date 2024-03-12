print("right-incremental triangle") 
column=int(input("Enter column count:"))
for i in range(1,column-1):
    for j in range(column,i-1,1):
        print("*",end="")   
    print()