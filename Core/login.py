import hashlib

def getPasswordInput(prompt):
	passwd = raw_input("%s: " % (prompt))
	return hashlib.md5( passwd ).hexdigest()


if __name__ == '__main__':
	print "Checking password input: "
	mypass = getPasswordInput("Type a password")
	validPass = (mypass == '5f4dcc3b5aa765d61d8327deb882cf99')
	print "MD5 comparison is "+str(validPass)