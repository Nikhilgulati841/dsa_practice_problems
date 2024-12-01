from datetime import datetime

# a=datetime.now()
def natural_sum(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    
    return total

# user=int(input("\nEnter the number for which you wish their natural sum: "))
print(natural_sum(11))

# b=datetime.now()
# print(b-a)

# a=[1,2,3,4,5,6,7,8,9,10]
# print(sum(a))