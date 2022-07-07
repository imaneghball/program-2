# def detNtFit(n):
#     if n==0:
#         return 0
#     if n<=3:
#         return 1
#     print(detNtFit(n - 1) + detNtFit(n - 2))
# detNtFit(20)

def largesLeng(Array):
    left=right=0
    numbers={x:0 for x in Array}
    for number in Array:
        if numbers[number]==0:
            left_Number=number-1
            right_Number=number+1

            while left_Number in numbers:
                numbers[left_Number]=1
                left_Number-=1
            left_Number+=1
            while right_Number in numbers:
                numbers[right_Number]=1
                right_Number+=1
            right_Number-=1
            if (right-left)<=(right_Number-left_Number):
                right=right_Number
                left=left_Number
    return [left,right]
def khodam(Array):
    nums={}
    count=0
    bestArray=[]
    print(Array)
    for num in Array:
        nums[num]=True
        print(nums)
        if not nums[num]:
            continue
        nums[num]=False
        countAdd=1
        left=num-1
        righ=num+1
        while left in Array:
            nums[left]=False
            left=left-1
            countAdd+=1
        while righ in Array:
            nums[righ]=False
            righ=righ+1
            countAdd+=1
        if count<countAdd:
            count=countAdd
            bestArray=[(left+1,righ-1)]
    print(bestArray)










A=[7,2,1,6,8,9,20]
# (left,right)=largesLeng(A)
# print((left,right))
khodam(A)