import whois
from datetime import datetime

w = whois.whois('google.com')
print(w)
check_date = w.expiration_date[0]
print(check_date)
present = datetime.now()
print(present)
if check_date < present:
    print('Domain is expired')
else:
    print('Domain is active')
