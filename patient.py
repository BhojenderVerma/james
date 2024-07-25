user_id = input("enter your patient Id number : ")  # Take input as a string
f=open('patient.txt', 'r')  # Use context manager to open the file
flag = 0
s = '0'
while s != '':
        s = f.readline().strip()  # Read line and strip any newline characters
        if s != '':
            if s == user_id:  # Compare strings directly
                print('he?she is a patient')
                flag = 1
                break
if flag == 0:
    print('this is not in patient list')







'''user_id = input("Enter the phone number: ")

with open('phone_numbers.txt', 'r') as f:
    flag = False
    for line in f:
        s = line.strip()  # Remove any trailing newline characters
        if s == user_id:
            print('The number was found')
            flag = True
            break

if not flag:
    print('The number was not found')
    '''
