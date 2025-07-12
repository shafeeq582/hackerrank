num=int(input())
d=list(map(int,input().split()))
n=list(map(int,input().split()))
t=int(input())
d.sort()
n.sort(reverse='True')
ep=0

for i in range(num):
    if d[i]+n[i]>t:
        ep=ep+((d[i]+n[i]-t))*100
print(ep)        
        
