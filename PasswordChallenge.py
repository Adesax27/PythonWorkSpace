"""
PROJECT 2: Password Check

A website requires the users to input a new password to register.
Write a python program that checks the validity of password input by a user. 

The Following are the criteria for checking the password:

1. At least 4 letters between a - z (upper or lower case). Case sensitive 
2. At least 2 numbers between 0 - 9
3. Minimum length of password: 6
4. Maximum length of password: 12

Your program will check the user input 
according to the above criteria. 
If a password given matches the above criteria, PASSWORD IS VALID will be printed out, if not INVALID PASSWORD will be printed out with the necessary required criteria.

E.g 1
Input 
Please enter a New Password: abcd123

Output: 
PASSWORD IS VALID 


E.g 2
Input 
Please enter a New Password: ab123

Output: 
INVALID PASSWORD 

- At least 4 letters must be used
- Minimum length of password must be 6

Please try again...


"""
PasswordFormat = 'ADEMsax123'
print('PasswordFormat: ABCDefgh123/123abcdEFGH')
smallLetters = 'qwertyuiopasdfghjklzxcvbnm'
capitalLetters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '0123456789'
'''
print(len(smallLetters))
print(len(capitalLetters))
len(smallLetters) + len(capitalLetters)
'''

Password = input('please enter your password: ')

smallLetter_input = []
capitalLetter_input = []
number_input = []

for x,y, z in zip (Password, Password, Password):
    if x in smallLetters:
        smallLetter_input.append(x)
    elif y in capitalLetters:
        capitalLetter_input.append(y)
    elif z in numbers:
        number_input.append(z)
        #print()
    

if len(smallLetter_input) >= 4 and len(capitalLetter_input) >= 4 and len(number_input) >= 2 and len(Password) >= 6 and len(Password) <=12:
    print('Password is VALID')
    
elif len(smallLetter_input) >= 4:
    print('error message')
    print('At least four letters including a capital letter')
    
elif len(capitalLetter_input) >= 4:
    print('At least four letters including a small letter')
    
elif len(number_input) >= 2:
    print('Must include letters')
    
elif len(Password) >= 6:
    print('minmum input is 6')
else:
    print('INVALID')
    
    
Password




