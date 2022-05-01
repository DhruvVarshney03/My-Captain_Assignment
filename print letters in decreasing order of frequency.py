def most_frequent(str1):
    import operator
    d = dict()
    for key in str1:
       if key not in d:
           d[key] = 1
       else:
           d[key] += 1
    
    
    cd = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    print(cd)

most_frequent("mississippi")

