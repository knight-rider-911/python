#test
import datetime
print("Test")

now = datetime.date.today()
new=str(now.day)+'-'+str(now.month)+'-'+str(now.year)
guess = str(input("Название продукта: "))
new=new+' '+guess
print(now)
print(new)