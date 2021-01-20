import shutil,os


import hashlib

inputFile = raw_input("Enter the name of the file:")
openedFile = open(inputFile)
readFile = openedFile.read()

md5Hash = hashlib.md5(readFile)
md5Hashed = md5Hash.hexdigest()

sha1Hash = hashlib.sha1(readFile)
sha1Hashed = sha1Hash.hexdigest()
sha1Hash256 = hashlib.sha3_256()

print ("File Name: %s" % inputFile)
print ("MD5: %r" % md5Hashed)
print ("SHA1: %r" % sha1Hashed)