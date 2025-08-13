x=int(input("Enter a Number: "))
s=0
while x!=0:
    r=x%10
    s=(s*10)+r
    x=x//10
    
print(f"reverse Number is {s}")   
    