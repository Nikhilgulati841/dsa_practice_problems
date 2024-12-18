n=7

print("\nPattern 1\n")
for i in range(1,n+1):
    print("*"*i+" "*(n-i))

print("\nPattern 2\n")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

print("\nPattern 3\n")
for i in range(1,n+1):
    print("*"*i+" "*(n-i))  #blunt
for i in range(n,0,-1):
    print("*"*i+" "*(n-i))

print("\nPattern 4\n")
for i in range(1,n+1):
    print("*"*i+" "*(n-i))   #sharp
for i in range(n-1,0,-1):
    print("*"*i+" "*(n-i))

print("\nPattern 5\n")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)

print("\nPattern 6\n")
for i in range(1,n+1):              #range(1,n) will give a space between two triangles
    print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)

print("\nPattern 7\n")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

print("\nPattern 8\n")
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)    
for i in range(n,0,-1):       # range(n-1 ) in the second loop to print n=6 rows not n=7
    print(" "*(n-i)+"* "*i)

print("\nPattern 9\n")
for i in range(1,n+1):
    print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)
for i in range(n,0,-1):
    print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)

print("\nPattern 10\n")
for i in range(1,n+1):
    print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)
for i in range(n-1,0,-1):
    print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)

print("\nPattern 11\n")
for i in range(1,n+1):
    if i>4:
        print("*"*(n*2))
    else:
        print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)
for i in range(n,0,-1):
    if i>4:
        print("*"*(n*2))
    else:
        print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)

print("\nPattern 12\n")
for i in range(1,n+1):
    print(f"{i} "*i)

print("\nPattern 13\n")
for i in range(1,n+1):
    print(" "*(n-i)+f"{i} "*i)

print("\nPattern 14\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")

    print()

print("\nPattern 15\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(f"{j} ",end="")

    print()

print("\nPattern 16\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(f"{chr(64+j)}",end="")

    print()

print("\nPattern 17\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(f"{chr(64+j)} ",end="")

    print()

print("\nPattern 18\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" "*(n-i)+f"{j} "*i)

print("\nPattern 19\n")
for i in range(1,n+1):
    if i==1:
        print(" "*(n-i)+f"{i}"*n)
        print(" "*(n-i)+f"{i}"*n)
        print(" "*(n-i)+f"{i}"*n)
    for j in range(1,n+1):
        print(" "*(n-i)+f"{j}E"*i)


print("\nPattern 20\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(" "*(n-i)+f"{j}"*j)

print("\nPattern 21\n")
for row in range(n):
        for col in range(n):
            if col == 0 or col == n - 1 or col == row:
                print('* ', end='')
            else:
                print('  ', end='')
        print()


