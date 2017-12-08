#Import modules
import json
import requests
import sys

#************ API KEYS

KEY_NYT = "1516c95485e1408e935c017d4b17dd41"
KEY_WSJ = "8c9c84eb251f426fb635a35bb66dbe26"

#************ INPUT VARIABLES

query = input("Enter your search query: ")
start = input("enter start date as YYYY-MM-DD: ")
end = input("enter end date as YYYY-MM-DD: ")

nyt_start = start
nyt_end = end
wsj_start = str(start) + "T00\:00\:00Z"
wsj_end = str(end) + "T00\:00\:00Z"

#************ CACHING SYSTEM

#Specify cache file

CACHE_FILE_NAME = "SI506finalproject_cache.json"

#Load the cache file into a python dictionary

try: 
	cache_file = open(CACHE_FILE_NAME, 'r')
	cache_str = cache_file.read()
	CACHE_DICT = json.loads(cache_str)
except:
	CACHE_DICT = {}

#Define the unique identifier function

def unique_id(baseurl, params_dict, private_keys):
	sorted_keys = sorted(params_dict.keys())
	result = []
	for item in sorted_keys:
		if item not in private_keys:
			result.append("{}-{}".format(item,params_dict[item]))
	return baseurl + "_".join(result)


#************ DATA REQUESTS


##NYT
def get_nyt_data(keywords,start_date,end_date,offset=0):
	#data request components
	baseurl = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
	params_dict = {
		'q': keywords,
		'begin_date': start_date,
		'end_date': end_date,
		'offset' : offset, #to blow away limit of 10 
		'api-key': KEY_NYT
	}
	#build unique identifier
	unique_ident_nyt = unique_id(baseurl, params_dict,['api-key'])
	#Pull data from cache if it's in there
	if unique_ident_nyt in CACHE_DICT:
		print("Getting cached data from NYT")
		return CACHE_DICT[unique_ident_nyt]
	#otherwise request it from the NYT API	
	else:
		print("Requesting new data from NYT")
		nyt_resp = requests.get(baseurl,params_dict)
		print("NYT request status:" + str(nyt_resp.status_code))
		#add response to the cache dictionary
		CACHE_DICT[unique_ident_nyt] = json.loads(nyt_resp.text)
		dumped_data = json.dumps(CACHE_DICT)
		cache_write_file = open(CACHE_FILE_NAME,'w')
		cache_write_file.write(dumped_data)
		cache_write_file.close()
		print("New NYT data written to cache")
		return CACHE_DICT



##WSJ
def get_wsj_data(keywords,start_date,end_date):
	#data request components
	baseurl = "https://newsapi.org/v2/everything"
	params_dict = {
		'q': keywords,
		'from': start_date,
		'to': end_date,
		'apiKey': KEY_WSJ,
		'language': 'en',
		'sources': 'the-wall-street-journal'
	}
	#build unique identifier
	unique_ident_wsj = unique_id(baseurl, params_dict,['apiKey'])
	#Pull data from cache if it's in there
	if unique_ident_wsj in CACHE_DICT:
		print("Getting cached data from WSJ")
		return CACHE_DICT[unique_ident_wsj]
	#otherwise request it from the WSJ API	
	else:
		print("Requesting new data from WSJ")
		wsj_resp = requests.get(baseurl,params_dict)
		print("WSJ request status:" + str(wsj_resp.status_code))
		print(wsj_resp.url)
		#add response to the cache dictionary
		CACHE_DICT[unique_ident_wsj] = json.loads(wsj_resp.text)
		dumped_data = json.dumps(CACHE_DICT)
		cache_write_file = open(CACHE_FILE_NAME,'w')
		cache_write_file.write(dumped_data)
		cache_write_file.close()
		print("New WSJ data written to cache")
		return CACHE_DICT

#************ BRING IN THE POSITIVE/NEGATIVE WORD FILES

pos_words = []
file = open('positive_words.txt', 'r')
for item in file.readlines()[35:]:
	pos_words.append(item.strip())
file.close()

neg_words = []
file = open('negative_words.txt', 'r')
for item in file.readlines()[35:]:
	neg_words.append(item.strip())
file.close()

#************ DEFINE ARTICLE CLASSES

#NYT	
class Article_NYT(object):

	def __init__(self, article_dict={}):
		if 'pub_date' in article_dict:
			self.pub_date = article_dict['pub_date'][:10]
		else:
			self.pub_date = ''
		if 'headline' in article_dict:
			self.title = article_dict['headline']['main'].replace(","," ")
		else:
			self.title = ''
		if 'snippet' in article_dict:
			self.abstract = article_dict['snippet']
		else:
			self.abstract = ''
		if 'byline' in article_dict:
			self.author = article_dict['byline']['original'].replace(","," ")

	def abstract_clean(self):
		return self.abstract.lower().replace('.','').replace(',','').replace(';','').replace(':','').replace(')','').replace('(','')

	def abstract_list(self):
		return self.abstract_clean().split()

	def positive_count(self):
		pos_count = 0
		for item in self.abstract_list():
			if item in pos_words:
				pos_count += 1
		return pos_count

	def negative_count(self):
		neg_count = 0
		for item in self.abstract_list():
			if item in neg_words:
				neg_count += 1
		return neg_count

	def emo_score(self):
		return self.positive_count() - self.negative_count()

	def __str__(self):
		return "{}; by {}; New York Times; published {}; emotional score: {}".format(self.title, self.author, self.pub_date, self.emo_score())

#WSJ

class Article_WSJ(object):

	def __init__(self, article_dict={}):
		if 'publishedAt' in article_dict:
			self.pub_date = article_dict['publishedAt'][:10]
		else:
			self.pub_date = ''
		if 'title' in article_dict:
			self.title = article_dict['title'].replace(","," ")
		else:
			self.title = ''
		if 'description' in article_dict:
			self.abstract = article_dict['description']
		else:
			self.abstract = ''
		if 'author' in article_dict:
			self.author = str(article_dict['author']).replace(","," ")

	def abstract_clean(self):
		return self.abstract.lower().replace('.','').replace(',','').replace(';','').replace(':','').replace(')','').replace('(','')

	def abstract_list(self):
		return self.abstract_clean().split()

	def positive_count(self):
		pos_count = 0
		for item in self.abstract_list():
			if item in pos_words:
				pos_count += 1
		return pos_count

	def negative_count(self):
		neg_count = 0
		for item in self.abstract_list():
			if item in neg_words:
				neg_count += 1
		return neg_count

	def emo_score(self):
		return self.positive_count() - self.negative_count()

	def __str__(self):
		return "{}; by {}; Wall Street Journal; published {}; emotional score: {}".format(self.title, self.author, self.pub_date, self.emo_score())

#************ DEFINE ARTICLE LIST FORMATTING FUNCTIONS

#Pull NYT and WSJ articles from the cache dictionary, we can identify
#Them because

#NYT stores them as a list of dicts as value of key 'docs' within dict 'response'

#WSJ stores them as a list of dicts as value of key 'articles'

#Finally we'll create instances of the artcle classes we defined for each article

#Let's do NYT
def nyt_format(response_data):
	nyt_articles = []
	#assembling list of NYT articles
	for item in CACHE_DICT:
		if 'response' in CACHE_DICT[item]:
			# print('found nyt articles')
			for item2 in CACHE_DICT[item]['response']['docs']:
				nyt_articles.append(Article_NYT(item2))
	print("NYT article count " + str(len(nyt_articles)))
	return sorted(nyt_articles, key = lambda x:x.emo_score())

#Okay now the WSJ,
def wsj_format(response_data):
	wsj_articles = []
	#assembling list of NYT articles
	for item in CACHE_DICT:
		if 'articles' in CACHE_DICT[item]:
			# print('found wsj articles')
			for item2 in CACHE_DICT[item]['articles']:
				wsj_articles.append(Article_WSJ(item2))
	print("WSJ article count " + str(len(wsj_articles)))
	return sorted(wsj_articles, key = lambda x:x.emo_score())

#************ PULL DATA BASED ON USER DEFINED PARAMETERS

nyt = nyt_format(get_nyt_data(query,nyt_start,nyt_end,0)) + nyt_format(get_nyt_data(query,nyt_start,nyt_end,1))

#sort descending by emo score
nyt_sorted = sorted(nyt, key = lambda x:x.emo_score(), reverse=True)

#sort by emo score
# test_nyt = str(nyt[0])

# print(test_nyt)

# print(test_nyt.title)
# print(test_nyt.pub_date)
# print(test_nyt.abstract)
# print(test_nyt.author)

#List of WSJ classed articles 
wsj = wsj_format(get_wsj_data(query,wsj_start,wsj_end))

#sort descending by emo score
wsj_sorted = sorted(wsj, key = lambda x:x.emo_score(), reverse=True)

# test_wsj = str(wsj[0])

# print(test_wsj)

# print(test_wsj.title)
# print(test_wsj.pub_date)
# print(test_wsj.abstract)
# print(test_wsj.author)

#************ WRITE OUTPUT DATA TO CSV

#Open the file and specify column headers
output_file = open('output_data.csv','w')
output_file.write('query_term,source,title,author,published_on,emo_score,description\n')

#Write in the NYT data
for item in nyt_sorted:
	output_file.write(query+", NYT, {}, {}, {}, {}, {}\n".format(item.title,item.author,item.pub_date,item.emo_score(),str(item)))

#Write in the WSJ data

for item in wsj_sorted:
	output_file.write(query+", WSJ, {}, {}, {}, {}, {}\n".format(item.title,item.author,item.pub_date,item.emo_score(),str(item)))


