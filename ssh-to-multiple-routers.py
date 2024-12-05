from netmiko import ConnectHandler

with open('file.txt') as routers:
    for ip in routers:
        csr = {
            'deviceType':'ciscoIs',
            'Ip':ip,
            'username':'tanim',
            'password' : 'dontknow'

        }

        netcon=ConnectHandler(**csr)
        print('connecting to'+ip)
        print('-'*70)
        output = netcon.send_command('show ip int brief')
        print(output)

netcon.disconnect()