#Given 
#L1=d3ZucXN0b2tib2xlamp5ZW5zdnlicGpsa3VhcGx2
#L2=b2dzd2xmcndwb2JmY2J4dmdtZGZseGp1dnZuaGZ0amFiZ2M=
#L3=YW9sdWxlYXJsZnB6anlmd2F2bnlod29m
#L4=aGZyZ3VyeHJsZ2pyYWds
#L5=Z3JlYXRzdGFydA== 
#L5 after decoding using the e5 we will get -----   greatstart
#L4 after decoding using the e5 and e4 we will get -----  usethekeytwenty      ---->so we will use the key as 20 for e3
#L3 after decoding using the e5, e4 and e3 we will get -----  thenextkeyiscryptography       ---->so we will use the key as cryptography for e2
#L2 after decoding using the e5, e4, e3 and e2 we will get ----- finalkeyisnatdszgrqhebvpmxilfywcuko    ---->so we will use key as natdszgrqhebvpmxilfywcuko for e1
#L1 after decoding using the e5, e4, e3, e2 and e1 we will get -----  welcomepotentialwebclubrecruit    ---->so this is the final answer


#NOTE : This the normal(basic) code for 'encoding' using base 64
#def e5(s):
#	st=''
#	binary=''
#	equ=0
#	for i in range(len(s)):
#		temps=str(bin(ord(s[i])).replace("0b",""))
#		while(len(temps)<8):
#			temps='0'+temps
#		binary=binary+temps
#	temps=''
#	temps2=''
#	k=len(binary)%24
#	if(k>0):
#		equ=4-(k//6+1)
#		for j in range(6):
#			if(len(binary)-(k%6)+j <len(binary)):
#				temps=temps+binary[len(binary)-(k%6)+j]
#			else:
#				temps=temps+'0'
#	for i in range((len(binary)//6)*6):
#		if((i+1)%6!=0):
#			temps2=temps2+binary[i]
#		else:
#			temps2=temps2+binary[i]
#			st=st+chr(int(temps2,2))
#			temps2=''
#	st=st+chr(int(temps,2))
#	for i in range(equ):
#		st=st+'='
#	return st

import base64
def e5(s):                              #This is base 64 format
	data=base64.b64decode(s)
	data=str(data).replace("'",'')
	data='0'+data
	data=data.replace('0b','')
	return data

def e4(s):                               #This is shift or caesar cipher with key=13
	st=''
	for i in range(len(s)):
		if(ord(s[i])>=97):
			st=st+chr(((ord(s[i])-97+13)%26)+97)
		elif(ord(s[i])>=65):
			st=st+chr(((ord(s[i])-65+13)%26)+65)
	return st
def e3(s):                                #This is shift or caesar cipher with key=20
	st=''
	for i in range(len(s)):
		if(ord(s[i])>=97):
			k=(ord(s[i])-97-20)
			if(k<0):
				st=st+chr((k+26)+97)
			else:
				st=st+chr((k)+97)
		elif(ord(s[i])>=65):
			k=(ord(s[i])-65-20)
			if(k<0):
				st=st+chr((k+26)+65)
			else:
				st=st+chr((k)+65)
	return st
def e2(s):                                #This is vigenere cipher with key='cryptography'
	st=''
	j=0
	key='cryptography'
	for i in range(len(s)):
		if(j==len(key)):
			j=0
		if(ord(s[i])>=97):
			k=(ord(s[i])-97-ord(key[j])+97)
			if(k<0):
				st=st+chr((k+26)+97)
			else:
				st=st+chr((k)+97)
		elif(ord(s[i])>=65):
			k=(ord(s[i])-65-ord(key[j])+97)
			if(k<0):
				st=st+chr((k+26)+65)
			else:
				st=st+chr((k)+65)
		j=j+1
	return st
def e1(s):                                   #This is Playfair cipher with key='natdszgrqhebvpmxilfywcuko'
	l=[]
	temps=[]
	st=''
	key='natdszgrqhebvpmxilfywcuko'          #This code is for the this fixed key only
	for i in range(len(key)):
		temps.append(key[i])
		if((i+1)%5==0):
			l.append(temps)
			temps=[]
		

	if(len(s)%2==1):
		s=s+'z'
	for i in range(len(s)):
		if(i%2==0):
			p=key.find(s[i])
			p1=p//5
			p2=p%5
		else:
			q=key.find(s[i])
			q1=q//5
			q2=q%5
			if(p1!=q1 and p2!=q2 ):
				st=st+l[p1][q2]
				st=st+l[q1][p2]
			elif(p1==q1):
				p2=p2-1
				q2=q2-1
				if(p2<0):
					p2=p2+5
				if(q2<0):
					q2=q2+5
				st=st+l[p1][p2]
				st=st+l[q1][q2]
			elif(p2==q2):
				p1=p1-1
				q1=q1-1
				if(p1<0):
					p1=p1+5
				if(q1<0):
					q1=q1+5
				st=st+l[p1][p2]
				st=st+l[q1][q2]

	return st



s=input('Enter the one line cipher text\n')
s=e5(s)
#print(s)                             #If you want to see the each step tranformation remove the comment
s=e4(s)
#print(s)
s=e3(s)
#print(s)
s=e2(s)
#print(s)
s=e1(s)
print('The final answer is: ',s)