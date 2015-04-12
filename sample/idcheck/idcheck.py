#coding = utf-8
#!usr/bin/env python

'check the identifier'
'for ... else ...'
'only after the for cycle is over and no break, then else will be executed!'

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
print
myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
	if myInput[0] not in alphas:
		print "'invalid: first symbol must be alphabetic'"
	else:
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print "invalid: remaining symbols must be alphabetic"
				break
		# only after the for cycle is over and no break
		else:
			print "okay as an identifier"
	

