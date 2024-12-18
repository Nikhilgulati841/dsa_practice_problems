n=7


print("\nPattern 1\n")
for i in range(0,n):
    for j in range(0,n):
        print(f"* ",end="")

    print()

print("\nPattern 2\n")

for i in range(1,n+1):
    ch=65
    for j in range(1,n+1):
        print(f"{chr(ch)}",end="")
        ch+=1
    print()


print("\nPattern 3\n")
num=65   #assign num=1 outside of the loop so that the value of num does not resets back to num=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{chr(num)} ",end="")
        num+=1
    print()

print(num) #as the num will increament by 1 after the loop ends so, if n=3, it will print till 9 and not print 10 as the loop ends but teh valie of num will be 10

        
print("\nPattern 4\n")
for i in range(1,n+1):
    for j in range(i):      # we can do this with 1 loop, then multiplying * (i)times.
        print("*",end="")   # but to better understand nested loops, using two loops for rows and columns

    print()

print("\nPattern 5\n")
for i in range(1,n+1):
    for j in range(1,i+1):  #using i*i will print the same using 1 loop
        print(f"{i}",end="")

    print()

print("\nPattern 6\n")
ch=65
for i in range(1,n+1):
    for j in range(1,i+1):  #using i*i will print the same using 1 loop
        print(f"{chr(ch)}",end="")
        
    ch+=1
    print()

print("\nPattern 7\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{j}",end="")

    print()

print("\nPattern 8\n")
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(f"{j}",end="")

    print()

print("\nPattern 9\n")
number=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{number} ",end="")
        number+=1

    print()

print("\nPattern 9 [Orientation of a 1 digit number]\n")
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if len(list(str(num)))==1:
            print(f" {num} ",end="")
            num+=1
        else:
            print(f"{num} ",end="")
            num+=1
    print()


print("\nPattern 10\n")

for i in range(1,n+1):
    alpha=64
    for j in range(i,0,-1):
        print(f"{chr(alpha+j)} ",end="")
        
    

    print()

print("\nPattern 11\n")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")

    for j in range(1,n-i+2):
        print(f"{i}",end="")

    print()



for i in range(1,n+1):
    print(" "*i,end="")
    for j in range(n+1-i,0,-1):
        print(f"{i}",end="")
    print()


for i in range(n,0,-1):
    print(" "*(n-i)+f"{i}"*i)
print()

print("\nPattern 12\n")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(f"{j}",end="")
        
    for j in range(i-1,0,-1):
        print(f"{j}",end="")
    print()
    

print("\nPattern 13\n")
