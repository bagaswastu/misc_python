import socket
from queue import Queue
import sys
import threading

target = ""
queue = Queue()
open_ports = []


def port_scan():
    while not queue.empty():
        try:
            port = queue.get()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target, port))
            open_ports.append(port)
        except:
            pass


def run_scanner(threads):
    for port in range(1, 49152):
        queue.put(port)
    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=port_scan)
        thread_list.append(thread)

    print("Please wait....", end="")

    for thread in thread_list:
        thread.start()

    thread.join()
    print("\r", end="") # Clear line
    print("List port that have been detected:\n>",open_ports)
    quit()


target = input("Input your target IP: ")
threads = int(input("Input thread you want to use: "))
run_scanner(threads)
