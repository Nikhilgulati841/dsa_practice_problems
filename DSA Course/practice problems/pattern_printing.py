n=7

print("\nPattern 1")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)


print("\nPattern 2")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)

print("\nPattern 3")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)






# hfhffnh
print("\nPattern 4")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)

print("\nPattern 5")
for i in range(1,n+1):
    print("*"*i+" "*(n-i))
for i in range(n-1,0,-1):
    print("*"*i+" "*(n-i))

print("\nPattern 5 alternative")
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)



print("\nPattern 6")
for i in range(1,n+1):
    print(" "*(n-i)+f"{i} "*(i))



print("\nPattern 7")
# for i in range(1,n+1):
    


print("\nPattern 8")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" "*(n-i)+f"{j} "*i)


# -----------------------------------


# print()
# for i in range(1,n+1):
#     if i==6:
#         print("*"*(i+1)+" "*(n-i-1)+" "*(n-i-1)+"*"*(i+1))
        
#     else:
#         print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)
    
    
# for i in range(n-1,0,-1):
#     if i==6:
#         print("*"*(i+1)+" "*(n-i-1)+" "*(n-i-1)+"*"*(i+1))
#     else:
#         print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)
        
# print()
# for i in range(1,n+1):
#     print("*"*i+" "*(n-i)+" "+" "*(n-i)+"*"*i)
    
# for i in range(n-1,0,-1):
#     print("*"*i+" "*(n-i)+" "+" "*(n-i)+"*"*i)
print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(f"{j} ",end="")
        
    print()
    
print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(f"{chr(65+j)} ",end="")
        
    print()
# print(chr(65)) -- A
    
    

print()
for i in range(1,n+1):
    print(" "*(n-i)+f"{i} "*i)

print()

for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
print()

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
  