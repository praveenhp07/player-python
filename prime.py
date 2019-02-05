st1, st2 = raw_input().split()
a=int(st1)
b=int(st2)
x=0
for num in range(a,b + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           x=x+1
print(x)  
