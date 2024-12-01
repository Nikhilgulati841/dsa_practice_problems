from datetime import datetime

a=datetime.now()

def natural_sum(num):
    total=0
    for i in range(1,num+1):
        # total=total+i
        total+=i

    return total

# def natural_sum(num):  #without actually summing the actual natural numbers
#     total=0
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             total=total+1

#     return total

print(natural_sum(11))

b=datetime.now()
print(b-a)