print("Happy ticket\nInput number of ticket")
num_ticket = input()
left = int(num_ticket[0])+int(num_ticket[1])+int(num_ticket[2])
right = int(num_ticket[3])+int(num_ticket[4])+int(num_ticket[5])
if len(num_ticket)<6:
    if left == right:
        print("Happy ticket")
    elif (left == right+1) or (left +1 == right):
        print("Nice meet")
    else:
        print("Not today")
else:
    print("Incorrect input")