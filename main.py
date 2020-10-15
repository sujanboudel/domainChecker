import whois
from datetime import datetime
#opening csv file
file = open('domainlist.csv', 'r')

#reading file
w = whois.whois(file.readline())
file.close()

#prints all information about domain
print(w)
if type(w.expiration_date) is list:
    check_date = w.expiration_date[0]
else:
    check_date = w.expiration_date
present = datetime.now()
#comparing present date and domain expiry date
if check_date < present:
    print('Domain is expired')
else:
    print('Domain is active')
