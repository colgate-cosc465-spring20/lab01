#!/usr/bin/python3

from argparse import ArgumentParser
import fcntl
import os
import selectors
import socket
import sys

def main():
    # Parse arguments
    arg_parser = ArgumentParser(description='Messenger', add_help=False)
    arg_parser.add_argument('-m', '--mode',
            choices=['client','server'], required=True,
            help='Mode in which to run messenger')
    arg_parser.add_argument('-p', '--port',
            type=int, required=True, help='''Port to connect to (in client 
            mode) or listen on (in server mode)''')
    arg_parser.add_argument('-h', '--hostname',
            default='localhost', help='Hostname to connect to (in client mode)')
    arg_parser.add_argument('-b', '--bot', action='store_true',
            help='Run bot (in server mode')
    settings = arg_parser.parse_args()

    # Start in server or client mode
    if (settings.mode == 'server'):
        server(settings.port, bot_mode=settings.bot)
    elif (settings.mode == 'client'):
        client(settings.port, settings.hostname)

def server(port, hostname='', bot_mode=False):
    print("** Starting messenger server on %s:%d **" % (hostname, port))

    # TODO

def client(port, hostname):
    print("** Connecting messenger client to %s:%d **" % (hostname, port))

    # TODO

""" Uses a selector to monitor for input from a socket and stdin and calls the
    appropriate handler """
def process_messages(sock):
    print("** Message processing started **")

    # Make stdin non-blocking
    orig_flags = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_flags | os.O_NONBLOCK)

    # Make socket non-blocking
    sock.setblocking(False)

    # Register inputs
    selector = selectors.DefaultSelector()
    selector.register(sock, selectors.EVENT_READ, recv_message)
    selector.register(sys.stdin, selectors.EVENT_READ, send_message)

    # Keep processing messages until socket closes or user enters ctrl+d
    keep_processing = True
    while keep_processing:
        events = selector.select()
        for key, mask in events:
            callback = key.data
            had_message = callback(sock)
            if not had_message:
                keep_processing = False
                break
    
    print("** Message processing finished **")

""" Reads a message from stdin and sends it on the socket; returns True if a 
    message was sent or false otherwise """
def send_message(sock):
    # TODO
    return False

""" Receives a message from a socket and prints it to stdout; returns True if a 
    message was received or false otherwise """
def recv_message(sock):
    # TODO
    return False

def bot(sock):
    print("** Bot started **")

    # TODO

    print("** Bot finished **")

if __name__ == '__main__':
    main()
