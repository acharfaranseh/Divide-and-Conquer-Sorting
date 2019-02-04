def merge(a,b):
    k=[]
    while len(a)>0 and len(b)>0:
        if a[0]<b[0]:
            k.append(a[0])
            a=a[1:]
        else:
          k.append(b[0])
          b=b[1:]
    k=k+a+b
    return(k)


def mergesort(k):
    n=int(len(k)/2)
    if len(k)==2:
        return merge([k[0]],[k[1]])
    return merge(mergesort(k[0:n]),mergesort(k[n:]))
