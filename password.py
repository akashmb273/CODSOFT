#Completed
import random

a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n=['0','1','2','3','4','5','6','6','7','8','9']
s=['@','#','$','&']

na =int(input("NUMBER OF ALPHABETS IN PASSWORD : "))
nn =int(input("NUMBER OF DIGITS IN PASSWORD : "))
ns =int(input("NUMBER OF SPECIAL CHARACTERS IN PASSWORD : "))

passw = ""

for i in range(0,na):
    new1=random.choice(a)
    passw+=new1

for i in range(0,nn):
    new2=random.choice(n)
    passw+=new2
for i in range(0,ns):
    new3=random.choice(s)
    passw+=new3


l=list(passw)
#print(l)
random.shuffle(l)
#print(l)
password=""
for i in range(len(l)):
    password += l[i]

print("Your Generated Password is ",password)


