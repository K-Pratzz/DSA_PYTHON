arr=[10,5,2,7,1,9]
k=15
def maxSubArraySum(arr,k):
    left =0
    right=0
    maxlength=0
    currSum=0

    while right<len(arr):
        currSum+=arr[right]
        if currSum>k and left<=right:
            currSum-=arr[left]
            left+=1
        if currSum==k:
            maxlength=max(maxlength,right-left+1)
        right+=1
    return maxlength
print(maxSubArraySum(arr,k))