#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("DorkAdminPanel.txt","r");
	link = raw_input("Masukkan Site Name \n(ex : contoh.com or www.contoh.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "# AdminPanelFinder #" 
	Space(9); print "By   :Ghost@AnonH2A"
	Space(9); print "Team :Kalsel(E)Xploit"
	
Credit()
findAdmin()