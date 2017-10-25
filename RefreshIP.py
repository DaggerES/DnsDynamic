#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Created by Dagger - https://github.com/gavazquez/DnsDynamic
#Script for refreshing your IP against the https://www.dnsdynamic.org service

username = "USERNAME" #Your username is the email you've registered on https://www.dnsdynamic.org
password = "PASSWORD" #The password you use on https://www.dnsdynamic.org
hostnames = "HOSTNAME" #The hostname/s you use on https://www.dnsdynamic.org. You can add several hostnames separated by comma

def TryGetIpAddress(url, regex, timeout):
    import urllib2, re
    try:
        return re.search(regex, urllib2.urlopen(url, timeout=5).read()).group(1)
    except:
        return "0"

def GetMyIP():
    import urllib2, re

    currentIpAddress = '0'
    if currentIpAddress == '0':
        currentIpAddress = TryGetIpAddress("http://ip.42.pl/raw", '(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})', 5)
    if currentIpAddress == '0':
        currentIpAddress = TryGetIpAddress("http://jsonip.com", '(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})', 5)
    if currentIpAddress == '0':
        currentIpAddress = TryGetIpAddress("http://ip.jsontest.com/", '([0-9.]*)', 5)
    if currentIpAddress == '0':
        currentIpAddress = TryGetIpAddress("http://httpbin.org/ip", '(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})', 5)
    if currentIpAddress == '0':
        currentIpAddress = TryGetIpAddress("https://api.ipify.org/", '(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})', 5)
    if currentIpAddress == '0':
        currentIpAddress = TryGetIpAddress("http://checkip.dyndns.org", '(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})', 15)

    return currentIpAddress

def RefreshIP():
    import urllib
    try:
	for hostname in [x.strip() for x in hostnames.split(',')]:
		url = "https://" + username + ":" + password + "@www.dnsdynamic.org/api/?hostname=" + hostname + "&myip=" + GetMyIP()
		print urllib.urlopen(url).read()
    except:
        print "Could not update IP!"

if __name__ == "__main__":
	RefreshIP()
