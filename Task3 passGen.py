print("******Random password generator using python******")

import string
import random

# input the length of password
length =int(input("enter the length of password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

# create password
password = "".join(temp)

print("password:-",password)