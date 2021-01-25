#!/usr/bin/python3
import os
makefile = './Debug/makefile'

rf = open(makefile)
temp = ''
for line in rf:
	pattern = ''
	if('Users' in str(line)):
		lin = str(line).replace('\n','').split(' ')
		for arg in lin:
			if('Users' in arg):
				pattern = arg
				arg = arg.split('\\')
				nln = arg[0].split('C:')[0] + '../' +  arg[-1]
	if(len(pattern) > 1):
		line = line.replace(pattern, nln)
<<<<<<< HEAD
	temp += line
=======
	temp += line + '\n'
>>>>>>> 5538bb480bebe983ebe5b2147e90e6cc4d02eccf
rf.close()

os.remove(makefile)

wf = open(makefile, 'w')
wf.write(temp)
wf.close()


