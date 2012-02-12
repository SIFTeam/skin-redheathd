#!/usr/bin/python

import os

# just because i'm lazy :)
tmpfiles = os.popen('cat skin.xml | grep "\.png" | sed "s/.*\\"\(.*\.png\).*/\\1/"').read().split("\n")
allfiles = []
for tmpfile in tmpfiles:
	tmps = tmpfile.split(",")
	for tmp in tmps:
		if tmp not in allfiles:
			allfiles.append(tmp)

allfiles = sorted(allfiles)

print "* THE FOLLOWING ELEMENTS ARE IN SKIN.XML BUT NOT ON FILESYSTEM"
for file in allfiles:
	if not os.path.exists("../" + file):
		print "WARNING: file %s not found on filesystem" % file

print
print "* THE FOLLOWING ELEMENTS ARE ON FILESYSTEM BUT NOT IN SKIN.XML"

def checkDir(realpath, skinpath):
	for entry in os.listdir(realpath):
		if entry[-4:] == ".png":
			if skinpath + "/" + entry not in allfiles:
				print "WARNING: file %s not found in skin" % (skinpath + "/" + entry)
		elif os.path.isdir(realpath + "/" + entry):
			checkDir(realpath + "/" + entry, skinpath + "/" + entry)


prefix = os.path.abspath(os.curdir).split("/")[-1]
checkDir(".", prefix)
