def dublicates(arr):
    global freq_dict
    global result
    freq_dict={}
    result=[]

    for i in arr:
        freq_dict[i]=freq_dict.get(i,0)+1
        print(freq_dict)
    print("\n")

    for key, value in freq_dict.items():
        if value>1:
            result.append(key)

    if not result:
        result.append("No Dubplictes..")

    result.sort()



    print("\n")

    return result
    
a=[]
i=0

while True:
    i+=1
    ask=input(f"Enter element {i}: ")
    if ask.lower()!="stop":
        a.append(ask)
    elif ask.lower()=="stop":
        print("Stopped taking input.\n")
        break

dublicate_finder=dublicates(a)
print("Dublicates Displaying...",end=" ")

for e in dublicate_finder:
    print(e,end=" ")
print("\n")

if not result:
    print(" ")
else:   
    for j in result:
        print(f"{j} *[{freq_dict.get(j)}] times")

