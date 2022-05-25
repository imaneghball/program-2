def anagran(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)
print(anagran("Hi wie","eiwiö"))# If two sentences have the same words, it goes back to True
def anagran2(s1,s2):
    s1=s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) !=len(s2):
        return False
    count={}
    for letter in s1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1
    for letter in s2:
        if letter in count:
            count[letter]-=1
        else:
            count[letter]=1
    for k in count:
        if count[k]!=0:
            print(f"{k} is not Same")
    print(count)
    return True


anagran2("hi byee t","hi byee k")

