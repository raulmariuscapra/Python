start= int(input("Startul "))
final = int(input("Finalul "))
for i in range(start,final+1):
    out=''
    if(i%3==0):
        out+='Fizz'
    if(i%5==0):
        out+='Buzz'
    print(out or i)