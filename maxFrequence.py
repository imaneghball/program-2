def max_Frequence(list):
    dic={}
    max=0
    result=None
    for i in list:

        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
        if dic[i]>=max:
            max=dic[i]
            result=i
    print(result)

max_Frequence([1,1,1,2,2,2,1,3,2])