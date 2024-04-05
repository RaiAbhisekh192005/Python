import random

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number="1234567890"
symbols='[]{}()*;/,_-!@#$%^&'

all=lower+upper+number+symbols


lenght=int(input('Enter home long pwd should be :'))
password="".join(random.sample(all, lenght))
print(password)
