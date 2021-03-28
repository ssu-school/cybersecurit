path = "./"
arr =[]
arr2 = []
temparr=[]
file=open((path+"small.refined.normal") , mode="r" , encoding="utf-8")

while True:
    line = file.readline().rstrip()
    if not line:
        break
    intL = -1
    for index,item in enumerate(temparr):
        if item == line:
            intL = index
    if intL == -1:
        intL = len(temparr)
        temparr.append(line)
    arr.append(intL);

arr2 = arr[1:len(arr):1]

for index,data in enumerate(arr):
    print(data)

for data in arr2[1:2:1]:
    print("data2: ", data)

tuple3 = ()
print()


