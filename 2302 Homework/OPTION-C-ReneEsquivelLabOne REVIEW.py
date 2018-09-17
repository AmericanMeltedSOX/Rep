# CS2302
import os
import hashlib
from itertools import product

user_input = {}
my_list = "0123456789"
password_list = []

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def checkPassword(gen_pswd):
    for key, value in user_input.items():
        if value[2] == hash_with_sha256(value[1].join(gen_pswd)):
            print("Password matches user: " + key)

def passWrdArray(text):
    value = text.split(',')
    user_input[value[0]] = value

def brute_force_recursion(lower, upper):
    password_list = product(my_list, repeat=lower)
    lower += 1

    for i in list(password_list):
        generate_pswd = password_list
        print("brute_for_recursion " + generate_pswd)
        checkPassword(generate_pswd)
        if lower < upper:
            brute_force_recursion(lower, upper)

def main():

 hex_dig = hash_with_sha256('This is how you hash a string with sha256')
 print(hex_dig)

 dirpath = os.path.dirname('password_file.txt')
 filepath = os.path.join(dirpath, 'password_file.txt')
 open(filepath, 'r')

 fr = open('password_file.txt', 'r')
 text = fr.read()
 print(text)
 fr.close()

 with open('password_file.txt', 'r') as open_File:
     for text in open_File:
         passWrdArray(text)

         brute_force_recursion(3, 7)

main()

