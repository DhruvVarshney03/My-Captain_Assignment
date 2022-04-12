lst1=eval(input("Enter a list: "))
lst2=[]
for i in lst1:
    if int(i)>=0:
        lst2.append(i)
    else:
        continue
print(lst2)
