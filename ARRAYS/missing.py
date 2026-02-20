nums=[int(x) for x in input("enter numbers :").split()]
def missing(nums):
    n=len(nums)
    total=(n+1)*(n+2)//2
    sumtotal=sum(nums)
    return sumtotal-total
print(missing(nums))