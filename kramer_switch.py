#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Florent Thiery florent.thiery@ubicast.eu

import socket
import struct

ip = "192.168.1.39"
port = 5000
BUFFER_SIZE = 1024
autoswitch_delay = 30

# http://www.kramerelectronics.com/downloads/protocols/protocol_2000_rev0_51.pdf
#msg = 0x01818181
#msg = 0xFUNC_8INP_8OUT_8MACH
# \x01\x83\x81\x81

cmds = {
    'input_1': 0x01818081, 
    'input_2': 0x01828081,
    'input_3': 0x01838081,
    'input_4': 0x01848081,
}


def send_command(cmd_name):
    print 'Setting all outputs to input %s' %cmd_name
    msg = cmds[cmd_name]
    #msg = cmds['all_off']
    hexstring = struct.pack('!I', msg)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(hexstring)
    print 'Sent %s to tcp://%s:%s' %(repr(hexstring), ip, port)
    data = sock.recv(BUFFER_SIZE)
    sock.close()
    print 'Received %s' %repr(data)

if __name__ == '__main__':
    import gobject, gtk
    import random
    import sys

    def autoswitch():
        input = random.randint(1, 4)
        send_command('input_%s' %input)
        return True

    try:
        input = int(sys.argv[1])
        if input in range(1, 5):
            send_command('input_%s' %input)
        else:
            print "Selected input (%s) not in accepted range: %s" %(input, range(1, 5))
    except Exception:
        print 'Launched without arguments, starting random autoswitch every %s seconds' %autoswitch_delay
        gobject.timeout_add_seconds(autoswitch_delay, autoswitch)
        gtk.main()


