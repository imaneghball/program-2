def gleichResult(s1,r):
    gibt={}
    a=1
    result=set()

    for k in s1:
        gibt[k]=1


    for k in range(len(s1)-1):
        if gibt[s1[k]]==1:
            target=r-s1[k]
            if gibt[target] in gibt:
                result.add((min(target,s1[k]),max(target,s1[k])))
                gibt[target]=0

    print(result)
    ############################

    # seen=set()
    # output=set()
    # for num in s1:
    #     target=r-num
    #     if target not in seen:
    #         seen.add(num)
    #     else:
    #         output.add((target,num))
    # print(output)




gleichResult([1,3,2,2,4,0,2,2],4)