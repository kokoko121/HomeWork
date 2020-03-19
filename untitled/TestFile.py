str=[]
str+="djfhgpeqytu=504hj5pohj42=-95gy459g0-48935489ghoit4b2jm-98g5um4v-9g2u4y59gm2hj5tvmsdk;gmhjvetgrmh250ug-295y7ut98r,mhgowehmgpwmtirghwrtslkdjfhgyuiopppoiuy"
maxCount=0
maxCountC=0
for i in range(1,len(str)-1):
    count = 0
    for j in range(1,i+1):
        if(i+j>=len(str) or i-j<0):
            if(count>maxCount):
                maxCount=count
                break
            else:
                break
        if(str[i-j]==str[i+j]):
            count+=1
        else:
            if(count>maxCount):
                maxCount=count
            break
    count=0
    for j in range(1,i+1):
        if(i+j>len(str) or i-j<0):
            if(count>maxCountC):
                maxCountC=count
                break
            else:
                break
        if(count==0):
            if(str[i]==str[i-j]):
                count+=1
            else:
                if(count>maxCountC):
                    maxCountC=count
                break
        else:
            if (str[i+j-1] == str[i - j]):
                count += 1
            else:
                if (count > maxCountC):
                    maxCountC = count
                break

maxCountC*=2
maxCount=2*maxCount+1
if(maxCount>maxCountC):
    print(maxCount)
else:
    print(maxCountC)
