#!/usr/bin/env python

'makeOreadTextFile.py -- make or read and display text file'

import os
ls  = os.linesep

# select to make or read & display
print "Please select to make or read & display a text file!"
print "1.Enter 'make' to make a text file !"
print "2.Enter 'read' to read & display a text file !"
print 
while True:
	operate = raw_input("input operate:")
	if operate == 'make' or operate == 'read':
		break
	else:
		print "ERROR: '%s' is not a right operation!" %operate

# make a text file
if operate == 'make':
	# set filename
	while True:
		fname = raw_input("input file name:")
		if os.path.exists(fname):
			print "ERROR: '%s' already exists" %fname
		else:
			break

	# get file content (text) lines
	all = []
	print "\nEnter lines ('.' by itself to quit).\n"

	# loop until user terminates input 
	while True:
		entry = raw_input('>')
		if entry == '.':
			break
		else:
			all.append(entry)

	# write lines to files with proper line-ending
	fobj = open(fname, 'w')
	fobj.writelines(['%s%s' % (x, ls) for x in all])
	fobj.close()
	print 'Done!'

elif operate == 'read':
	# get filename
	fname = raw_input('Enter filename:')
	print

	# attempt to open file fot reading
	try:
		fobj = open(fname, 'r')
	except IOError, e:
		print "*** file open error:", e
	else:
		#display contents to the screen
		for eachLine in fobj:
			print eachLine
		fobj.close()

