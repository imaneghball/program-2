import sys
n=10
data=[]
for i in range(n):
    a=len(data)
    b=sys.getsizeof(data)
    #print("Lendgh : {0:3d};   Size: {1:4d}".format(a,b))
    #print(f"lenght: {a}   Size: {b}")
    print(i)
    data.append(i)
