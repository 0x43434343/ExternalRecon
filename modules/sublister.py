
from os import *
def search_subdomains(domain):
	'''
	using sublister to find the subdomains 
	'''
	path = getcwd()
	system('python3 %s/modules/Sublist3r/sublist3r.py -d %s'%(path,domain))




