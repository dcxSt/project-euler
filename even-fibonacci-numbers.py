# Project Euler even-Fibonnacci-numbers

sum=0
n1=1
n2=1
while n2<4000000:
    if n2%2==0:
        print(n2,end=" ")
        sum+=n2
    temp=n2
    n2=n2+n1
    n1=temp
    

print("\n\n",sum)
