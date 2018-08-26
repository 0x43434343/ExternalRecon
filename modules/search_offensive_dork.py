import time
def offensiveSecurityGoogleHacking():
	'''
	using offensive security gooogle hacking to grap the new dork 
	then use it for a specfic target
	return l: will return the list of dorks
	'''
	#this function not done yet 
	l = list()
	USER_AGENT = {'User-Agent':''+UserAgent().random+''}
	site = "https://www.exploit-db.com/google-hacking-database/?action=search&ghdb_search_page=1&ghdb_search_text=&ghdb_search_cat_id=0"
	r = requests.get(site,headers=USER_AGENT)
	content = r.content
	soup = BeautifulSoup(content,"html.parser")

	for name in soup.find_all("tbody"):

		count = 0
		for i in name.parent.find_all('a'):
			
			d = name.parent.find_all('a')[count]
			l.append(d)
			count +=1
	return l




def OffensiveSearch(domain=""):
	'''
	using the list that return from the offensiveSecurityGoogleHacking function
	then use it with GoogleSearch
	print: links
	return: 

	'''
	#what I need here is to split the list 
	#not finish
	l = list()
	s = offensiveSecurityGoogleHacking()
	d= [[item] for c_list in s for item in c_list]
	c = 0
	for getAll in range(len(d)):
		#print(d[getAll].strip())
		result = prepareGoogle('site:'+domain+ ' ' + d[getAll][0].strip())
		print("dork: "+d[getAll][0].strip())
		GoogleSearch(domain,d[getAll][0].strip())
		getLinks(result)
		time.sleep(5)

