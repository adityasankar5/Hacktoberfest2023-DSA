
x= [1,3,8,-2,6,-8,5] #array
a=list(x)

#Kadane's Algorithm logic

max_sum=min(a)
current=0
for i in a:
    current+=i
    if current<0:
        current=0
    if current > max_sum:
        max_sum= current

print(max_sum)

