from test1 import Add

def func():
    a=Add(1,3)
    with open("a.txt", "w") as f:
        f.write(str(a))
    print(a)

if __name__=="__main__":
    func()