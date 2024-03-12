# def function01 (*data):
#     print("my data",data)
#     print("first element",data[0])
#     print("last element",data[-1])

# function01("h1",123,"h3", True, 6j)


# --------len()
# print(len("welcome"))
# print(len("98989"))
# print(len([9, 8, 9, 8, 9]))
# print(len({9, 8, 9, 8, 9}))
# print(len((9, 8, 9, 8, 9)))
# print(len({1: 1, 2: 4, 3: 9}))
# print(len(range(5)))
# print(len(list(range(5))))

# ---------min() and max() and sum()
print(min("welcome", "a", "z"))
# print(min(0, 34, "welcome", "a", "z")) #type error
print(min("98989", "5", "0"))
print(min([9, 8, 9, 8, 9]))
print(min({9, 8, 9, 8, 9}))
print(max((9, 8, 9, 8, 9)))
print(sum((9, 8, 9, 8, 9)))
print(max({1: 1, 2: 4, 3: 9}))
print(sum({1: 1, 2: 4, 3: 9}))

# ---------chr() and ord() and bin()
print(chr(65))
print(ord("A"))
print(bin(1))
print(hex(1))
print(oct(1))

# --------------- id() ,type(),print(),input()