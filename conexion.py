# establecer conexion a equipos via ssh

from netmiko import ConnectHandler

vyos = {
    'device_type':'vyos',
    'host':'192.168.1.8',
    'username':'vyos',
    'password':'vyos',
}

lista = [
    {'interface':'eth1','ip':'10.1.1.1/30','description':'eth1vyos'},
    {'interface':'eth2','ip':'11.1.1.1/30','description':'eth2vyos'}
]

try:
    ssh = ConnectHandler(**vyos)
    print(ssh.send_command('show interfaces'))
    for element in lista:
        commands = [
            'set interfaces ethernet '+element['interface']+' address '+element['ip'],
            'set interfaces ethernet '+element['interface']+' description '+element['description']
        ]
        ssh.send_config_set(commands)
    print(ssh.send_command('commit && save'))
    print(ssh.send_command('show interfaces'))
except Exception as e:
    raise e