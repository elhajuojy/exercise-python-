a=int(input("Entre an intuger number please a :"))
b=int(input("Entre an intuger number please b :"))


if a*b<0 :
    a,b=b,a
    
else:
    sum=a+b
    product=a*b
    a=sum
    b=product
print("a = ",a) 
print("b = ", b)




