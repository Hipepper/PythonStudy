#!/usr/bin/env python
# _*_ coding=utf-8 _*_

from scapy.all import *
import psutil

def test1():
    for ipFix in range(1, 254):
        ip = "192.168.2." + str(ipFix)
        arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
        res = srp1(arpPkt, timeout=0.1, verbose=0)
        if res:
            print("IP: " + res.psrc + "     MAC: " + res.hwsrc)


def test2():
    arping("192.168.2.*")


def test3():
    psutil.net_connections()


if __name__ == "__main__":
    test3()
