from test1 import Add

a=Add(1,2)

with open("a.txt", "w") as f:
    f.write(str(a))
print(a)