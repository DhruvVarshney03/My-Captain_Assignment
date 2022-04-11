a=input("Enter file name:")
d={"py":"Python","cc":"C++","c":"C","java":"Java","js":"JavaScript"}
f=a.split(".")
x=f[-1]

print("Extension of file is",x)

for i in d:
    if x==i:
        print("Extension name is",d[i])
        break
    else:
        continue

