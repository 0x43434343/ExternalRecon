
from pgoogle import *


def search_config_extension(domain):
	'''
All Config Extensions: site:tdforeverproud.ca ext:xml 
| ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp 
| ext:cfg | ext:txt | ext:ora | ext:ini | ext:sql |
 ext:dbf | ext:mdb | ext:log | ext:bkf | ext:bkp |
  ext:bak | ext:old | ext:backup

	'''
	ext = ('conf','cnf','reg','inf','rdp','cfg','txt','ora','ini'
				'sql','dbf','txt','mdb','log','bkf','bkp','bak','old','backup','xml')

	'''
	the purpose of this function is search for Extension 
	'''
	print("start searching for All Config Extensions")
	for getAll in range(len(ext)):
		GoogleSearch(domain,'ext:'+ext[getAll])
