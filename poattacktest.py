import po1 as po


def attack(c):
	iv 	= c[:16]
	cblock 	= c[16:]
	
# Find the length of the message
	length = 0
	i = 0
	while(length==0):
		newiv = iv[:i] + "\x30" + iv[i+1:]
		try:
			po.dec_check(newiv+cblock)
		except:
			length = i
		else:
			i=i+1
	spacelen = 16-length
	
# Add the spaces to the message
	newiv = iv[:length]
	diff = spacelen^16-length
	message = ""
	for i in range(length,16):
		curr = iv[i]
		newiv = newiv + chr(ord(iv[i])^diff)
		message = chr(spacelen) + message
	current_space_length = spacelen
# Figure out the rest of the message
	newiv = iv[:length]
	current_space_length = 12
	diff = current_space_length^spacelen
	for i in range(length,16):
		curr = iv[i]
		newiv = newiv + chr(ord(curr)^diff)
	for j in range(1,256):
		tryiv = newiv[:4] + chr(ord(newiv[4])^j)+newiv[5:]
		try:
			po.dec_check(tryiv+cblock)
		except:
			pass
		else:
			print "O Worked"
			message = chr(j^current_space_length) + message
			print message


#L
	length = 4
	newiv = iv[:length]
	current_space_length = 13
	for i in range(length,16):
		curr = iv[i]
		msgchr = message[i-length]
		diff = ord(msgchr)^current_space_length
		newiv = newiv + chr(ord(curr)^diff)
	for j in range(1,256):
		tryiv = newiv[:3] + chr(ord(newiv[3])^j)+newiv[4:]
		try:
			po.dec_check(tryiv+cblock)
		except:
			pass
		else:
			print "L Worked"
			message = chr(j^current_space_length) + message
			print message

#L2
	length = 3
	newiv = iv[:length]
	current_space_length = 14
	for i in range(length,16):
		curr = iv[i]
		msgchr = message[i-length]
		diff = ord(msgchr)^current_space_length
		newiv = newiv + chr(ord(curr)^diff)
	for j in range(1,256):
		tryiv = newiv[:2] + chr(ord(newiv[2])^j)+newiv[3:]
		try:
			po.dec_check(tryiv+cblock)
		except:
			pass
		else:
			print "L2 Worked"
			message = chr(j^current_space_length) + message
			print message
#E
	length = 2
	newiv = iv[:length]
	current_space_length = 15
	for i in range(length,16):
		curr = iv[i]
		msgchr = message[i-length]
		diff = ord(msgchr)^current_space_length
		newiv = newiv + chr(ord(curr)^diff)
	for j in range(1,256):
		tryiv = newiv[:1] + chr(ord(newiv[1])^j)+newiv[2:]
		try:
			po.dec_check(tryiv+cblock)
		except:
			pass
		else:
			print "E Worked"
			message = chr(j^current_space_length) + message
			print message
#H
	length = 1
	newiv = iv[:length]
	current_space_length = 16
	for i in range(length,16):
		curr = iv[i]
		msgchr = message[i-length]

		diff = ord(msgchr)^current_space_length

		newiv = newiv + chr(ord(curr)^diff)
	for j in range(1,256):
		tryiv = newiv[:0] + chr(ord(newiv[0])^j)+newiv[1:]
		try:
			po.dec_check(tryiv+cblock)
		except:
			pass
		else:
			print "H Worked"
			message = chr(j^current_space_length) + message
			print message

