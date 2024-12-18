from datetime import datetime, timedelta

def formula():
    
    a=datetime.strptime(date1,"%d/%m/%Y")
    b=timedelta(days=1)
    output=a
    for i in range(1,10):
        print(f"Todays Task Code {i}: ",output.strftime("#%Y%d%m"),"\n")
        output=output+b

print("\n")
date1=input("Starting date Format[xx/xx/xxxx]: ")
print("\n")
formula()
