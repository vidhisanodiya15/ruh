#print(i)

def count(listofnum):
    even=0
    odd=0

    for i in listofnum:
        if i % 2 ==0:
            even+=1
        else:
            odd +=1
    return even,odd
    
listofnum=[32,21,64,100,13]
even,odd =count(listofnum)
print(even)
print(odd)


