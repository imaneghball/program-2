def sort(List1,List2):
    sortList1=sorted(List1)
    sortList2=sorted(List2)
    result=set()
    for i in range(len(sortList1)):
        for j in range(len(sortList2)):
            if sortList1[i]==sortList2[j]:
                result.add(sortList1[i])
                break
    print(list(result))

def sort2(a,b):
    sortA=sorted(a)
    sortB=sorted(b)
    pointA=0
    pointB=0
    result=[]
    while pointA<len(sortA) and pointB<len(sortB):
        if sortA[pointA]==sortB[pointB]:
            result.append(sortB[pointB])
            pointB+=1
            pointA+=1
        elif sortA[pointA] > sortB[pointB]:
            pointB+=1
        else:
            pointA+=1
    print(result)

sort2([0,1,2,3,6],[1,3,4,5,6,0,9])
