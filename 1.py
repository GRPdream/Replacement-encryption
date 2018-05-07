x = input("请输入明文(字母)：")
key = input("请输入密钥（字母）：")
x_list = list(x)
temp = len(x)//len(key)
xList = [[0] * len(key) for i in range(temp+1)]
count = 0
for i in range(0,temp+1):
    for j in range(0,len(key)):
    	if count == len(x_list):
    		break
    	else:
            xList[i][j] = x_list[count]
            count += 1
aList = list(key)
bList = sorted(aList)
for t in bList:
	for s in range(temp+1):
		if xList[s][key.find(t)] != 0:
		    print(xList[s][key.find(t)],end='')
		else:
			continue
print(" ")
input("Press <enter>")

















