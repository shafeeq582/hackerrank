arr=list(map(int,input().split()))
n=arr[0]
d=arr[1]
jac=list(map(int,input().split()))
jac.sort(reverse='True')
m=sum(jac[:d])
print(m)
