import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore, Back, Style
from pprint import pprint
import re
from socket import gethostbyname

def prepareGoogle(search_term, number_results=100, language_code='en'):
        USER_AGENT = {'User-Agent':''+UserAgent().random+''}
        assert isinstance(search_term, str), 'Search term must be a string'
        assert isinstance(number_results, int), 'Number of results must be an integer'
        escaped_search_term = search_term.replace(' ', '+')
        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
        response = requests.get(google_url, headers=USER_AGENT)
        response.raise_for_status()
        # Parsing
        soup = BeautifulSoup(response.text, 'html.parser')
        found_results = []
        rank = 1
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3', attrs={'class': 'r'})
            description = result.find('span', attrs={'class': 'st'})
            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                if link != '#':
                    found_results.append({'link': link,'keyword': search_term, 'rank': rank, 'title': title, 'description': description})
                    rank += 1
        return found_results

def GoogleSearch(domain,value):
	'''
    
	'''
	result = prepareGoogle('site:'+domain+' '+value)
	getLinks(result)

def getLinks(domain):
	'''
	the purpose of this function to get only the links for later use 
	'''
	for getAll in range(len(domain)):
		print(domain[getAll]['link'])



