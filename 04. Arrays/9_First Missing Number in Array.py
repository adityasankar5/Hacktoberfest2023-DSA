n=5 # size of array
array= [1,2,3,5]
# code to find the first missing number in an array
full_range= set(range(1,n+1))
output=full_range-set(array)
print(output)
            