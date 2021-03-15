"""darkbox nmap command"""

import sys
import time
import socket
import argparse
import ipaddress

from darkbox.static.ports import tcp_ports
from darkbox.commands.template import Command


class nmap(Command):
    """darkbox nmap

    network exploration tool and security / port scanner

    Designed to be similar to nmap by Gordon "Fyodor" Lyon.
    Resource: https://nmap.org/
    """

    def __init__(self):
        self.version = '0.1.0'

    def get_parser(self):
        parser = super().get_parser(description='darkbox nmap')
        parser.add_argument('target', nargs='?')
        parser.add_argument('-p', '--ports', help='port specification')
        # TODO: Service scan.
        # parser.add_argument('-sV', help='service scan')
        return parser

    @staticmethod
    def validate_ip(ip):
        try:
            return ipaddress.ip_address(ip)
        except ValueError:
            return False
    
    @staticmethod
    def resolve_host(domain):
        try:
            return socket.gethostbyname_ex(domain)[2]
        except (socket.gaierror, socket.herror):
            return False

    @staticmethod
    def reverse_ip_lookup(ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except (OSError, socket.gaierror, socket.herror):
            return False

    @staticmethod
    def get_datetime():
        return time.strftime(f'%Y-%M-%d %H:%M {time.tzname[0]}', time.localtime())

    def validate_ports(self, ports):
        for port in ports:
            if not 0 < port < 65536:
                self.handle_port_outside_range(port)

    def handle_port_outside_range(self, port):
        print('Ports specified must be between 0 and 65535 inclusive')
        print('QUITTING!')
        sys.exit(1)

    def handle_invalid_port(self, port):
        print(f'Invalid port "{port}" specified')
        print('QUITTING!')
        sys.exit(1)

    def handle_backwards_port_range(self, a, b):
        print(f'Your port range {a}-{b} is backwards. Did you mean {b}-{a}?')
        print('QUITTING!')
        sys.exit(1)

    def parse_port_str(self, port_str):
        if (',' not in port_str) and ('-' not in port_str):
            try:
                return [int(port_str)]
            except ValueError:
                self.handle_invalid_port(port_str)

        ports = []
        for i in port_str.split(','):
            if '-' in i:
                try:
                    a, b = map(int, i.split('-'))
                except ValueError:
                    self.handle_invalid_port(i)
                if a > b:
                    self.handle_backwards_port_range(a, b)
                ports += range(a, b+1)
            else:
                try:
                    ports.append(int(i))
                except ValueError:
                    self.handle_invalid_port(i)
        return ports

    def run(self, args=None):
        args = self.get_args(args)
        target = args['target']
        if not target:
            print('Error: No target specified.')
            return

        start_time = time.time()
        print(f'Starting darkbox Nmap v{self.version} at {self.get_datetime()}')

        if self.validate_ip(target):
            ip = target
            domain = self.reverse_ip_lookup(ip)
            other_ips = False
        else:
            ips = self.resolve_host(target)
            if ips:
                ip = ips[0]
                other_ips = ips[1:]
            else:
                print(f'Failed to resolve "{target}".')
                return
            domain = target
        
        if not domain:
            report = ip
        else:
            report = f'{domain} ({ip})'

        print(f'Nmap scan report for {report}')
        if other_ips:
            print(f'Other addresses for {target} (not scanned): {", ".join(other_ips)}')

        # TODO: Add top 1000 ports, and UDP scanning.
        port_str = args['ports']
        if port_str:
            ports = self.parse_port_str(port_str)
        else:
            ports = tcp_ports

        self.validate_ports(ports)

        results = '\nPORT      STATE\n'
        for p in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c = s.connect_ex((ip, p))
            socket.setdefaulttimeout(0.5)
            state = 'open' if not c else 'closed'
            results += f'{str(p)+"/tcp":<9} {state:<7}\n'
        print(results)

        end_time = time.time()
        t_delta = end_time - start_time

        # TODO: multiple hosts / subnet
        print(f'Nmap done: 1 IP addresses scanned in {t_delta:.2f}')