from re import A, T
from tkinter import N


T=int(input())
for i in range (0,T):
    N=int(input())
    A=list(map(int,input().split()))
    l=len(A)
    strenght=0
    for j in range(l):
        if(A[j]>0):
            strenght+=A[j]
    while(strenght>=1 and strenght%2==0):
        strenght=int(strenght/2)
    if(strenght==1):
        print("Yes")
    else:
        print("No")



