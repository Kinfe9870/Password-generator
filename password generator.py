import random

length = int(input("Enter the length of the password: "))

data = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%&*"

password = "".join(random.sample(data,length))
print(password)

