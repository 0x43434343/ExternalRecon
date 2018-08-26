from pgoogle import *
def googleSubdomain(domain):
	'''
	not complete modules 

	ret; will return a list of domains
	'''
	l = list()
	reg = r'.*?\//(.*)/.*'
	result = prepareGoogle("site:*."+domain)
	for getAll in range(len(result)):
		s = result[getAll]['link']
		a = re.search(reg,s)
		if (a.group(1) not in l):
			if '/' in a.group(1):
				continue
			l.append(a.group(1))

	return l
def cleanAfterChar(c):
	'''
	the purpose of this function is to remove all the chracters 
	that comes after a specfic chracters
	'''
	#you can modfied / to any chracters 
	return re.sub(r'\s*/.*', '', c)

def bingSubdomain(domain):
	#this will store the domain in a list for later use 
	l = list()
	reg = r'.*?\//(.*)/.*'
	word = "site:"+domain
	for i in range(1,200,12):   
		r = requests.get("https://www.bing.com/search?q="+word+"&first="+str(i))
		soup = BeautifulSoup(r.text, "html.parser")
		for li in soup.find_all(class_="b_algo"):
			s = li.a.get('href')
			a = re.search(reg,s)
			#CleanAfter function it will remove any chracters after / 
			clear = cleanAfterChar(a.group(1))		
			if clear in l:
				continue
			l.append(clear)
	return l

def getSubdomain(domain):
	merge = googleSubdomain(domain) + bingSubdomain(domain)
	subdomain = list(set(merge))
	print("#---------------------------------#")
	print("###### ( get the subdomains )###### ")
	for i in range(len(subdomain)):

		print(subdomain[i] + ' : ' + gethostbyname(subdomain[i])) 


