import os, ipaddress

os.system('cls')

while True:
    ip = input('enter ip:')
    try:
        print(ipaddress.ip_address(ip))
        print('ip valid')
    except:
        print('-'*49)
        print('invalid ip')
    finally:
        if ip =='quit':
           print('script ended')
           break
