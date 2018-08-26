
# -*- coding: utf-8 -*-

'''
author ; Fahad Alharbi
twitter; @0x4142
language python3
started in jun 12, 2018 at 6:28 PM

'''


import sys
if sys.version_info[0] < 3:
    sys.stdout.write("this script required a Python3\n")
    sys.stdout.write("python3 ExternalRecon.py\n")
    sys.exit(0)

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore, Back, Style
from pprint import pprint
import re
from socket import gethostbyname
import sys
import os
from pgoogle import *
from modules.enum_domain_users import *
from modules.search_public import searchPublicly
from modules.search_subdomain import *
from modules.search_vuln import *
from modules.search_offensive_dork import *
from modules.sublister import search_subdomains
from modules.theharvester import *
from modules.search_config_extension import *
import readline

class External:

	def __init__ (self,target="",module="",payload="",console="you can do it"):

		self.target = target
		self.module = module
		self.payload = payload
		self.console = console

	def welcomeToExternalProj(self):
		'''
		welcome framework that shows the version and the author. Bsides that shows 
		the contains modules
		'''
		gre = '\038[0m'
		yu = '\033[93m'
		red = '\033[91m'  
		white = '\033[0m'

		print("""%s

		__author__= Fahad Alharbi
		__twitter__ = @0x4142
		__version__ = 1.0
		__date__ = jun 15th,2018

____      _                        _ ____                      
| ____|_  _| |_ ___ _ __ _ __   __ _| |  _ \ ___  ___ ___  _ __  
|  _| \ \/ / __/ _ \ '__| '_ \ / _` | | |_) / _ \/ __/ _ \| '_ \ 
| |___ >  <| ||  __/ |  | | | | (_| | |  _ <  __/ (_| (_) | | | |
|_____/_/\_\\__\___|_|  |_| |_|\__,_|_|_| \_\___|\___\___/|_| |_|
                                   
%s

			"""%(yu,white))

	def checkConsoleStatus(self,console):

		if console != None:
			return True



	def help_commands(self):

		print("""


		set -> to assign 
			
		use -> to use a module
		
		run -> to run and execute the module

		show modules -> to display the current modules 

		? -> help command

		help -> help command

		#Example; 
		set target sony.com
		use module search_extension
		show options
		run

			""")

	def show_modules(self):

		print("""


/==//==//==//==//==//==//==//==//==//==//==//==//==//==//==//==/
/
/ -#- search_public ; This will search for a documents such as pdf,docs for metadata analysis

/ -#- search_subdomains ; using sublist3r

/ -#- search_config_extension ; this module will look up the extension config files

/ -#- offensive_search ; using offensive security database dorks

/ -#- search_emails ; using theharvester 

/ -#- enum_domain_users ; 

/ -#- search_vuln ; using google dork 

/==//==//==//==//==//==//==//==//==//==//==//==//==//==//==//==/




			""")
	def addModules(self,module_name=""):
		"""
		this will add a new modules to a list to allow user for autocompleter commmand line 
		in the future 
		
		"""
		modules = [
			'search_vuln',
			'search_subdomain',
			'search_public',
			'search_emails',
			'enum_domain_users',
			'search_config_extension'
			]

		return modules

	def autocompleter(self,text,status):

		names = ["module","set","show","options","show options","target","payload"]
		names +=  self.addModules()
	
		options = [x for x in names if x.startswith(text)]
		try:
			return options[status]
		except IndexError:
			return None

	def createInput(self):

		readline.set_completer(self.autocompleter)
		readline.set_completer_delims('')

		if 'libedit' in readline.__doc__:
			readline.parse_and_bind("bind ^I rl_complete")
			readline.parse_and_bind('set editing-mode vi')

		else:
			readline.parse_and_bind("tab: complete")

		self.console = ""
		#self.console = input("\33[37m#er>: "+ self.console).split()
		self.console = input("\033[93m#er>: "+ self.console).split()

	def displayOptions(self):
		"""
		to display options
		"""
		print("##################################")
		print("target: " + self.target)
		print("module: " + self.module)
		print("payload: " + self.payload)
		print("##################################")


	def createACommand(self):
		self.console = ""
		self.console = input("\33[37m#er>: "+ self.console).split()


	def checkModule(self,target):
		"""
		it will check which module is assignt to and execute the module
		"""
		if self.module == "search_subdomain":

			search_subdomains(self.target)
		elif self.module == 'search_vuln':
			search_vuln(self.target,self.payload)

		elif self.module == 'search_emails':
			search_emails(self.target)

		elif self.module == "search_offensive_dork":

			search_offensive_dork(self.target)

		elif self.module == "search_config_extension":

			search_config_extension(self.target)

		elif self.module == "enum_domain_users":
			#enum_users_domain(ip="",domain="",username="",password=""):
			enum_domain_users(self.target,self.domain,self.username,self.password)

	def checkCommand(self):
		"""
		will check the command during the loop inside the modules
		"""

		if "exit" in self.console or "background" or "back" in self.console:
			return True


	def displayCurrent(self,module):

		gre = '\038[0m'
		print("\033[92m#er>:(/modules/{0})>".format(self.module))

		#self.createACommand()
		self.createInput()
		while self.console != "exit" or self.console[0] !="exit":

			print("\033[92m#er>:(/modules/{0})>".format(self.module))
			if "run" in self.console:

				self.checkModule(self.target)


			if self.checkCommand() == True:
				break

			if "enum_domain_users" == self.module:
				if "username" in self.console:

					self.username = self.console[2]
				elif "password" in self.console:
					self.password = self.console[2]

				elif "domain" in self.console:
					self.domain = self.console[2]

				print("required input")
				print("username: " + self.username)
				print("domain: " + self.domain)
				print("password: " + self.password)


			#to let the user check his/her status 

			if "show" in self.console:

				self.displayOptions()

	def displayModules():
		"""	
		this function to display modules
		"""
		pass

	def clearConsole(self):

		self.console = ""
		self.console = input("\33[37m#er>: "+ self.console).split()
		#return self.console
	def Execute(self):

		self.username = ""
		self.password = ""
		self.domain = ""

		""" 
		-# will start execute the Recon #-
		pre-condition , if the length 3 and the list contains target letter or length equal 3 and the list
		contains module letter
		post-condition store the last value on the variable for later use 

		"""
		self.welcomeToExternalProj()
		while self.console != "exit":

			self.createInput()
			if 'exit' in self.console:
				break

			elif "modules" in self.console:

				self.show_modules()

			elif "help" in self.console:

				self.help_commands()

			elif len(self.console) == 3 and "target" in self.console:
					self.target = self.console[2]

			elif len(self.console) == 3 and "module" in self.console: 

				if "module" in self.console:
					self.module = self.console[2]
					#to display the current module inuse 
					self.displayCurrent(self.module)

			elif len(self.console) == 3 and "payload" in self.console: 

				if "payload" in self.console:
					self.payload = self.console[2]
					#to display the current module inuse 
			if "show"  in self.console:
				self.displayOptions()

def main():

	ExternalRec = External(console="")
	ExternalRec.Execute()



if __name__ == '__main__':
	main()




