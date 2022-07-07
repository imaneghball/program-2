def Mac_sum(Array):
    result=set()
    a=len(Array)-1
    count=1
    for k in range(len(Array)-1):
        for j in range(a):
            j+=count
            result.add(Array[k]+Array[j])
        count+=1
        a-=1
    return max(result)

def Max_sum2(Array):
    result = set()
    count = 1
    for k in Array[0:]:
        for j in Array[count:]:
            result.add(k + j)
        count += 1
    return max(result)
def All_Max(Array):
    sum=0
    for num in Array[0:]:
        if num>0:
            sum=sum+num
    return sum
print(Mac_sum([-1,2,3,5]))
print(Max_sum2([-1,2,3,5]))
print(All_Max([-1,2,3,5,-30,5]))