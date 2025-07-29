print('\nPassword Strength Checker')

# Take password
password = input('Enter your password: ')

# Track conditions
has_upper = False
has_lower = False
has_digit = False

# Check each character
for char in password:
    if 'A' <= char <= 'Z':
        has_upper = True
    elif 'a' <= char <= 'z':
        has_lower = True
    elif '0' <= char <= '9':
        has_digit = True

# Check password length and conditions
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print('Strong password.')
else:
    print('Weak password.')
    print('Password must contain atleast:')
    print('- 8 characters')
    print('- 1 uppercase letter')
    print('- 1 lowercase letter')
    print('- 1 digit')
