'''
Write a program only one statement long (it can span multiple lines) that prints the number 
of palindromes in /users/abrick/resources/english
'''

print(len(list(filter(lambda line: line.strip() == line.strip()[::-1], 
    open('/users/abrick/resources/english')))));
