def quicksort(a):
    if len(a)<=1:
        return a
    b=[]
    c=a[0]
    d=[]
    for i in a[1:]:
        if i<c:
            b.append(i)
        if i>=c:
            d.append(i)
    return quicksort(b)+[c]+quicksort(d)
