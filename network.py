# Python script to automate network device configuration
from netmiko import ConnectHandler
def configure_network_device(host, username, password, configuration_commands):
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
    }
    with ConnectHandler(device) as net_connect:
        net_connect.send_config_set(configuration_commands)

