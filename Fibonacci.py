n=int(input("Cate numere se vor genera "))
while(n<1):
    n=int(input("Introduceti un numar valabil "))
print("1")
if(n>=2):
    print("1")
if(n>2):
    n1=1
    n2=1
    for i in range(3,n+1):
        print(n1+n2)
        r=n2
        n2=n1+n2
        n1=r
