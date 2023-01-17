import sys
#print python's version
print(sys.version)

#using date
import datetime
now = datetime.date.today()
new=str(now.day)+'-'+str(now.month)+'-'+str(now.year)
guess = str(input("Название продукта: "))
new=new+' '+guess
print(now)
print(new)

#print hosts's name
import socket
#print server name
print(socket.gethostname())