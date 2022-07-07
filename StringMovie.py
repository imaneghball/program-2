
start="i am iman"
start=start.split()
start.reverse()
print(start)
def retur(satz):
    #return "-_".join(reversed(satz.split()))
    return "*".join(satz.split()[::-1])
print(retur("i am iman"))