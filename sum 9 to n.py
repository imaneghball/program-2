def sum():
    print("what is n: ")
    n=int(input())
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
print(sum())