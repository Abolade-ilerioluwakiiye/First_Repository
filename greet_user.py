"""Welcome new users to the firm"""
New_Users= ['bolu', 'tife', 'eyinju', 'ileri']
Name= input('Enter your name:')
User = Name.lower()

if User in New_Users:
    print(f"{User.title()}, welcome to the firm.")
else:
    print(f'Your name, {User.title()}, was not found in the list of new recriuts.')



