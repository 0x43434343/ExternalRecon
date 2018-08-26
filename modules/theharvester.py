
from os import *
def search_emails(domain):
	'''
	using theHarvester to get all email address 
	'''
	path = getcwd()
	system('python2.7 %s/modules/theHarvester/theHarvester.py -d %s -b all'%(path,domain))
