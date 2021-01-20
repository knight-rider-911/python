import hashlib
print (hashlib.md5(open("d:\\1.txt", 'rb').read()).hexdigest())

inputFile = raw_input("Enter the name of the file:")
openedFile = open(inputFile)
readFile = openedFile.read()

md5Hash = hashlib.md5(readFile)
md5Hashed = md5Hash.hexdigest()

sha1Hash = hashlib.sha1(readFile)
sha1Hashed = sha1Hash.hexdigest()

# print "File Name: %s" % inputFile
# print "MD5: %r" % md5Hashed
# print "SHA1: %r" % sha1Hashed