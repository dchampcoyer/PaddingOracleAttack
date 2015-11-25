import po1 as po


def attack(c):
	iv 	= c[:16]
	cblock 	= c[16:]
	
# Find the length of the message
	message_length = 0
	i = 0
	while(message_length==0):
		newiv = iv[:i] + "\x30" + iv[i+1:]
		try:
			po.dec_check(newiv+cblock)
		except:
			message_length = i
		else:
			i=i+1
	pad_length = 16-message_length
	
# Add the spaces to the output message
	message = ""
	for i in range(message_length,16):
		message = chr(pad_length) + message
	current_pad_length = pad_length

# Figure out the rest of the message
	for i in range(0,message_length):
		newiv = iv[:message_length-i]
		current_pad_length = current_pad_length + 1
		for j in range(message_length-i,16):
			curr = iv[j]
			msgchr = message[j-(message_length-i)]
			diff = ord(msgchr)^current_pad_length
			newiv = newiv + chr(ord(curr)^diff)
		for j in range(1,256):
			tryiv = newiv[:message_length-i-1] + chr(ord(newiv[message_length-i-1])^j)+newiv[message_length-i:]
			try:
				po.dec_check(tryiv+cblock)
			except:
				pass
			else:
				#print str(j^current_pad_length) + " Worked"
				message = chr(j^current_pad_length) + message
	return message
