import datetime

with open("1.txt", mode='a') as file:
    file.write('Printed string %s recorded at %s.\n' % 
               (1, datetime.datetime.now()))
