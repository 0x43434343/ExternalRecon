'''
author ; Fahad Alharbi
twitter; @0x4142
language python3

https://developers.google.com/custom-search/json-api/v1/overview


'''

import subprocess
import sys

def enum_domain_users(ip="",domain="",username="",password=""):

	badgame = subprocess.getoutput('rpcclient -U "{0}/{1}%{2}" {3} -c "lookupnames {4}"'.format(domain,username,password,ip,username))
	badgame = badgame.split(" ")
	badgame = badgame[1].split("-")
	ready = helper_function(badgame)
	for i in range(499,2000):
			badgame = subprocess.getoutput('rpcclient -U "{0}/{1}%{2}" {3} -c "lookupsids {4}{5}"'.format(domain,username,password,ip,ready,i))
			print(badgame)

def helper_function(s):
	new_str = ""
	for getAll in range(len(s)):
		#it will avoid the last number for later use 
		if s[getAll] == s[-1]:
			break
		new_str += s[getAll]
		new_str += "-"

	return new_str

