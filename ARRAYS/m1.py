#largest element in an array
nums=[int(x) for x in input("enter numbers : ").split()]
currlargest=nums[0]
largest=0
for i in range(1,len(nums)):
    largest=max(currlargest,largest)
    currlargest=nums[i]
#print(largest)

    
#better
maxno=nums[0]
for x in nums:
    if x>maxno:
        maxno=x
#print(maxno)


#second largest element in an array.. -1 if not exists
if len(nums)==1:
    second=-1
lg=-1
slg=-1
for x  in nums:
    if x>lg:
        slg=lg
        lg=x
    elif x >slg and x!=lg:
        slg=x
print(slg)

#second smallest 
sm=float('inf') #positive infinity
ssm=float('inf')
for x in nums:
    if x <sm:
        ssm=sm
        sm=x
    elif x <ssm and x!=sm:
        ssm=x
print(ssm)



