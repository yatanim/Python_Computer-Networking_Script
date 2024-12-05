import ConnectHandler from netmiko

#its a dictionary for creating device

csr = {
    'deviceType':'ciscpIos',
    'ip':'192.168.0.33',
    'username':'tanim',
    'password':'dontknow'
}

#its time to establish ssh connection

net_con = ConnectHandler(**CSR)

# send the command and print output

output = net_con.send_command('show ip int brief')
print(output)

#close the connection

net_con.disconnect()