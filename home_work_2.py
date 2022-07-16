user_name = input('Fill up you name \t ')
user_age = int(input('Fill up you age \t '))
if user_age > 122:
    print('You are not real ' + user_name + '.')
elif 70 < user_age < 90:
    print('You are lucky ' + user_name + ' and welcome.')
elif user_age == 16:
    print('Dear ' + user_name + ' need to wait one year.')
elif user_age > 16:
    print('Welcome ' + user_name + ' on our website.')
else:
    print("I'm sorry " + user_name + " you are too young.")
