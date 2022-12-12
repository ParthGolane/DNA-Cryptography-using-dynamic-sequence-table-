from collections import deque


def get_key(my_dict,val):
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

def remove_chucks(Arr):
    A=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
    B=""
    i=0
    for j in range(len(A)):
        B+=Arr[i]
        i=i+A[j]
        i+=1
        if i>len(Arr):
            break
    return(B)

def convertdnatobinary(ci):
    output=[]
    for i in ci:
        string=""
        for j in i:
            if j=="A":
                string+="00"
            elif j=="C":
                string+="01"
            elif j=="G":
                string+="10"
            else:
                string+="11"
        output.append(string)
    return(output)
    
       

def rsa_algo(p: int,q: int, msg: str,Bool):
    n = p * q
    z = (p-1)*(q-1)

    e = find_e(z)
    d = find_d(e, z)

    cypher_text = ''

    for ch in msg:
        # convert the Character to ascii (ord)
        ch = ord(ch)

        # convert the calculated value to Characters(chr)
        cypher_text += chr((ch ** e) % n)
    if Bool==0:
        return(cypher_text,d,n)

    # Convert Plain Text -> Cypher Text
    plain_text = ''
    # P = (C ^ d) % n
    for ch in cypher_text:
        # convert it to ascii
        ch = ord(ch)
        # decrypt the char and add to plain text
        # convert the calculated value to Characters(chr)
        plain_text += chr((ch ** d) % n)
    if Bool==1:
        return plain_text

def find_e(z: int):
    # e -> gcd(e,z)==1      ; 1 < e < z
    e = 2
    while e < z:
        # check if this is the required `e` value
        if gcd(e, z)==1:
            return e
        # else : increment and continue
        e += 1

def find_d(e: int, z: int):
    # d -> ed = 1(mod z)        ; 1 < d < z
    d = 2
    while d < z:
        # check if this is the required `d` value
        if ((d*e) % z)==1:
            return d
        # else : increment and continue
        d += 1

def gcd(x: int, y: int):
    # GCD by Euclidean method
    small,large = (x,y) if x<y else (y,x)

    while small != 0:
        temp = large % small
        large = small
        small = temp

    return large


def dnaencoding(g):
    fibonacci=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
    key1 = ""
    for i in range(100000):
        temp = str(random.randint(0, 1))
        key1 += temp   
    ldna=binarytodna(key1)
#    print(ldna)
    finalcipher=""
    res=[]
    for split in fibonacci:
        temp=ldna[:split]
        ldna=ldna[split:]
        res.append(temp)
    j=0
    for i in range(0,len(g)-1,2):
        finalcipher+=g[i]+res[j]+g[i+1]
        j+=1
    return(finalcipher,res)
        
 
#generate dna bases
import random
b=[]
def toString(List):
	return ''.join(List)
def allLexicographicRecur (string, data, last, index):
    length = len(string)
    for i in range(length):
        data[index] = string[i]
        if index==last:
            global b
            b.append(toString(data))
            (toString(data))
        else:
            allLexicographicRecur(string, data, last, index+1)
def allLexicographic(string):
	length = len(string)

	data = [""] * (length+1)
	string = sorted(string)
	allLexicographicRecur(string, data, length-1, 0)
string = "ATGC"
#print ("All permutations with repetition of " + string + " are:")
allLexicographic(string)

#print(b) #printing dna bases



#generate ascii values
c = list(map(chr, range(0, 256)))
#print(c)  #printing ascii values
        
def dividestring(str, K, ch):  #divide string into equal chunks
    N = len(str)
    j, i = 0, 0
    result = []
    res = ""
    while (j < N):
        res += str[j]
        if (len(res) == K):
            result.append((res))
            res = ""
        j += 1
    if (res != ""):
        while (len(res) < K):
            res += ch
        result.append((res))
    return result


        
def generatednatable(inp):
    dnaseqtable={}
    for i in range(256):
        random_item_from_list = random.choice(b)
        b.remove(random_item_from_list)
        dnaseqtable[c[i]]=random_item_from_list
    
    print("initial dna sequnce table",dnaseqtable) #INTIAL TABLE
    initialdnatable=dnaseqtable
    #now generate fibonacci series
    fibo=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
    Bool=-1
    value_of_fibo=3  #index position
    q=inp   #initial character of plain text
    for i in q:
    #    r=dnaseqtable.get(i)
        if (ord(i))%2!=0:
            Bool=1
            r=dnaseqtable.get(i)
            if i in dnaseqtable:
                index = list(dnaseqtable).index(i)
            print("postion of first character in initial table",index)
            t=int((index+fibo[value_of_fibo])%256)
            print("rotate dna bases ",t," times in forward")
            values_deque = deque(dnaseqtable.values())
            values_deque.rotate(t)
            dnaseqtable=(dict(zip(dnaseqtable.keys(), values_deque)))
            value_of_fibo+=1
            
        else:
            Bool=0
#            r=dnaseqtable.get(i)
            if i in dnaseqtable:
                index = list(dnaseqtable).index(i)
            print("postion of first character in initial table",index)
            result=int((index-fibo[value_of_fibo])%256)
            if result<=0:
                result+=256
            t=0-result
            print(t)
            print("rotate dna bases ",t," times in backwards")
            values_deque = deque(dnaseqtable.values())
            values_deque.rotate(t)
            dnaseqtable=(dict(zip(dnaseqtable.keys(), values_deque)))
            value_of_fibo+=1
    
    return(dnaseqtable,Bool,t,initialdnatable) 
#        
def binarytodna(p):
    o=[]
    ba=""
    for i in range(0,len(p),2):
        o.append((p[i]+p[i+1]))
    for i in o:
        if i=="00":
            ba+="A"
        elif i=="01":
            ba+="C"
        elif i=="10":
            ba+="G"
        else:
            ba+="T"
    return(ba)
       
        
#generatednatable()
#dnaencoding()

def convert_binary(n):
    final=""
    if n==0:
        final+="0000"
    else:
        b= []
        while(n>0):
            d=n%2
            b.append(str(d))
            n=n//2
        b.reverse()
        bina="".join(b)
        if len(bina)==3:
            final="0"+bina
        elif len(bina)==2:
            final="00"+bina
        elif len(bina)==1:
            final="000"+bina
        else:
            final=bina
    return(final)


plain_text=input("enter original text to encypt: ")
ascii_of_plaintext=""
binary=""
ordi=[]
for i in plain_text:
    ordi.append(ord(i))
    if ord(i)<100:
        ascii_of_plaintext+=("0"+str(ord(i)))
    else:
        ascii_of_plaintext+=str(ord(i))
print()
print("ascii_value_of_plain_text: ",ascii_of_plaintext,end="\n")
print()
for i in ascii_of_plaintext:
    binary+=convert_binary(int(i))
print("binary value of ascii: ",binary)
if len(binary)%4==0:
    pass
elif len(binary)%4==1:
    binary+="000"
elif len(binary)%4==2:
    binary+="00"
else:
    binary+="0"
    
binary_to_dna=binarytodna(binary)
dnaseqtable,Bool,no_of_rotation,initialdnatable=generatednatable(plain_text[0])
print()
print()
print("dnasequnce table after rotation: ",dnaseqtable,end="\n")
print()
print()
print("DNA base value for binary: ",binary_to_dna,end="\n")
dna_to_ascii=[]
if len(binary_to_dna)%4==1:   #issue point
    binary_to_dna+="AAA"
elif len(binary_to_dna)%4==2:
    binary_to_dna+="AA"
elif len(binary_to_dna)%4==3:
    binary_to_dna+="A"
else:
    pass   
for i in range(0,len(binary_to_dna),4):
    dna_to_ascii.append(binary_to_dna[i]+binary_to_dna[i+1]+binary_to_dna[i+2]+binary_to_dna[i+3])
#print(dna_to_ascii)   
newascii=""
for j in dna_to_ascii:
    value = {i for i in dnaseqtable if dnaseqtable[i]==j}
    newascii+=str(*value)
print("ascii character: " ,newascii)
integer_value_of_ascii=""
for i in newascii:
    if ord(i)<100:
        integer_value_of_ascii+="0"+str(ord(i))
    else:
        integer_value_of_ascii+=str(ord(i))
print("ascii integer value",integer_value_of_ascii,end="\n")
print(len(integer_value_of_ascii))

K = int(input("enter size of eack chunk you want to divide"))
ch = '0'
ans = dividestring(integer_value_of_ascii, K, ch)
print("chuncks: ",ans,end="\n")
cyphers=[]
encryption_key=[]
for i in ans:
    p=53
    q=59
    msg = i
    cypher_text,d,n = rsa_algo(p, q, msg,0)
    cyphers.append(cypher_text)
    encryption_key=[d,n]
#    print("Encrypted (Cypher text) : ", cypher_text)
print ("encryption of cyphers",cyphers,end="\n")
#print(encryption_key)   

''' #for rsa decryption

'''
asciichucks=[]
for i in cyphers:
    ascii_of_chucks=""
    for j in i:
        if ord(j)<100:
            ascii_of_chucks+=("0"+str(ord(i=j)))
        else:
            ascii_of_chucks+=str(ord(j))
    asciichucks.append(ascii_of_chucks)
print("ASCII OF ABOVE CIPHERS",asciichucks)
 
newbinary=[]  
for i in asciichucks:
   new_binary=""
   for j in i:
       new_binary+=convert_binary(int(j))
   newbinary.append(new_binary)
#print(newbinary)

lcipher=[]
for i in newbinary:
    lcipher.append(binarytodna(i))
#print(lcipher)
ci=lcipher
final_cipher,ldna=dnaencoding(lcipher)  
print("final cipher",final_cipher)      
       
print("################### decryption ######################")
no_of_iteration=1
print("Bool :",Bool)
print("no_of_rotation :",no_of_rotation)

#again generating dna sequnce table for decryption
    
#print(initialdnatable)
fit=""
for i in final_cipher:
    fit+=remove_chucks(i)
print(fit)
print("cipher after removing dnaencoding: ",ci)

convert_dna_to_binary=convertdnatobinary(ci)
print("converting adove DNA into binary: ", convert_dna_to_binary)

integer=[]
#for i in convert_dna_to_binary:
w=convert_dna_to_binary
integ=""
for i in w:
    for j in range(0,len(i),4):
        inte=""
        inte+=i[j]+i[j+1]+i[j+2]+i[j+3]
        value=str(int(inte,2))
        integ+=value
    integer.append(integ)
    integ=""
print(" converting above binary to integer: ",integer)
    
plain_text=""
for i in ans:
    plain_text+=str(rsa_algo(p, q, i,1))
print("decrypted chucks: ",plain_text)
#plaintext ascii to its corresponding symbol

ft=""
for i in  range(0,len(plain_text),3):
    ft+=str(chr(int(plain_text[i:i+3])))
print("converting decrypted chuck into ascii form: ",ft)    
#print(newascii)

#plain text to its corresponding dna bases
dna_to_asciis=[]
for i in ft:
    dna_to_asciis.append(dnaseqtable[i])
print("dna bses of ascii value: ",dna_to_asciis) 
    
form=convertdnatobinary(dna_to_ascii)
binaryform="".join(form) 
print("binary form of above dna bases: ",binaryform)

orimsg=""
for i in range(0,len(binaryform),4):
    ori=binaryform[i:i+4]
    orimsg+=str(int(ori,2))
print(orimsg)

original_msg=[]
g=[]
for i in range(0,len(orimsg),3):
    f=(int(orimsg[i:i+3]))
    g.append(f)
print(g)

for i in g:
    original_msg.append(chr(i))
print("".join(original_msg))

    