def rotation(List1,List2):# evry Nummber are same

    if range(len(List1))!=range(len(List2)):
        return False
    for i in range(len(List1)):
        result = len(List2)
        for j in range(len(List2)):
            if List1[i]!=List2[j]:
                result-=1
        if result!=1:
            return False
            break
    return True

def rotation2(List1,List2):#[a,b,c,d,e,f][e,f,a,b,c,d] that have to be same Number with same potition
    if len(List1)!=len(List2):
        return False
    FiresElem=List1[0]
    indexPos=0
    for i in range(len(List2)):
        if FiresElem==List2[i]:
            indexPos=i
            break
    for j in range(len(List1)):
        newIndex=(j+indexPos)%len(List1)
        if List1[j]!=List2[newIndex]:
            return False
            break
    return True



#print(rotation([1,2,3,4],[3,2,1,4,6]))
print(rotation2([1,2,3,4,5],[5,4,1,2,3]))