import numpy as np
import math

key = input("enter the key\n")
cipher=input("enter the cipher text\n")

print(len(key))
print(len(cipher))
cipher_text=[]
for i in range(0,len(cipher)):
    cipher_text.append(cipher[i])
matrix=[]
for i in range(0,(len(key))):
    matrix.append(key[i])

amount=math.ceil((len(cipher_text)+len(key))/len(key))
# print(amount)
# print(len(key))
if len(key)*(amount-1)>len(cipher_text):
    for i in range(0,len(key)*(amount-1)-len(cipher_text)):
        cipher_text.append(" ")
    # print("heloooo")
print(cipher_text)
print(len(cipher_text))
mat_size=amount*len(key)
for i in range(0,mat_size-len(key)):
    matrix.append(" ")

print(matrix)
key_array=np.array(matrix)
key_array=key_array.reshape(amount,len(key))
print(key_array)

keylist=[]
for i in range(len(key)):
    keylist.append(key[i])
keylist.sort()
print(keylist)
tracker=[]
pointer=0
for i in range(0,len(keylist)):
    for j in range(0,len(key)):
        if keylist[i]==key_array[0][j]  and j not in tracker:
            for m in range(1,amount):
                key_array[m][j]=cipher_text[pointer]
                pointer=pointer+1
                tracker.append(j)
            print(key_array)
       
plain_text=[]           
print(key_array)
for i in range(1,amount):
    for j in range(0,len(key)):
        plain_text.append(key_array[i][j])
plain_string="".join(plain_text)
print(plain_string)




