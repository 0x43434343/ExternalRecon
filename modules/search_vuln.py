from pgoogle import *
import time


def search_vuln(domain="",payload=""):



	ext = (
		"syntax error has occurred",
		"sql syntax near",
		"incorrect syntax near",
		"unexpected end of SQL command",
		"Warning: mysql_connect()",
		"Warning: mysql_query()",
		"Warning: pg_connect()",
		)
	'''
	intext:"sql syntax near" 
	the purpose of this function is find vulnerability or error 
	'''

	if payload:
		f = open(payload)
		for getAll in f:
			getAll = getAll.rstrip()
			time.sleep(3)
			GoogleSearch(domain,"intext:"+ext[getAll])
	else:
		for getAll in range(len(ext)):	
			GoogleSearch(domain,"intext:"+ext[getAll])
			#to avoid block lol
			time.sleep(3)

