#n=int(input("enter number "))
'''def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
#print(fact(n))
    
#fibonaci  0 1 1 2 3 
def fibonaci(n):
    if n<=1:
        return n
    else:
        return fibonaci(n-1)+fibonaci(n-2)


for i in range(n):
    print(fibonaci(i),end=' ')'''

n=input("enter number : ")
sum=0

#for x in number:
    #sum+=int(x)
#print(sum)

while(n>0):
    digit=n%10
    sum+=digit
    n=n//10
print(sum)


        
