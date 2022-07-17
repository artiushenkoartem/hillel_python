"""Задача 1.

Написать программу которая будет спрашивать у пользователя имя и возраст.
Проверять
если возраст более 16 вывести Welcome < user_name> on our website.
еcли возраст равен 16 вывести Dear < user_name> need to wait one year.
если возраст между 70 и 90 вывести You are lucky < user_name> and welcome.
если возраст более 121 вывести You are not real < user_name>.
и в конце, если ни одно из условий не удовлетворенно то вывести I'm sorry < user_name>
you are too young.
"""
# ask the user for information to create variables
user_name = input('Fill up you name \t ')
user_age = int(input('Fill up you age \t '))
# use comparison operators. So that based on the evaluation of
# the variable (user_age), you can decide whether to execute certain code or not.
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
