import numpy as np
import math
key = input("enter the key\n")
plain_text=input("enter the cipher text\n")

# print(len(key))
# print(len(plain_text))

matrix=[]
for i in range(0,(len(key))):
    matrix.append(key[i])

for i in range(0,(len(plain_text))):
    matrix.append(plain_text[i])

#
# print(key_array)
# if math.ceil(len(matrix)/len(key))*len(key)>len(matrix)
row=math.ceil(len(matrix)/len(key))
column=len(key)
if row*column>len(matrix):
    for i in range(0,(row*column)-len(matrix)):
        matrix.append(" ")

key_array=np.array(matrix)


key_array=key_array.reshape(row,column)
print(key_array)


key_list=[]
for i in range(0,len(key)):
    key_list.append(key[i])
key_list.sort()
# print(key_list)
cipher_text=[]
tracker=[]
for i in range(0,len(key)):
    for j in range(0,len(key)):
        if key_list[i]==key_array[0,j] and j not in tracker:
            for k in range(1,row):
                
                cipher_text.append(key_array[k,j])
                tracker.append(j)

            break
        

# print(cipher_text)
cipher_string="".join(cipher_text)
print(cipher_string)
print(len(plain_text), len(cipher_string))
