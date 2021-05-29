# Write your code here :-)
print('What\'s your name')
name = input()
print('Hello ' + name)
print('How old are you')
age = input()
age = int(age)
if age < 18:
    print('You are too young')
elif age >= 18:
    print('Go on right ahead')

