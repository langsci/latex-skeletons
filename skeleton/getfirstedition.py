from bs4 import BeautifulSoup
import yaml 
import requests
import sys
import urllib2
import datetime
import json
import copy


bookid = sys.argv[1]
url = 'http://www.langsci-press.org/catalog/book/%s'%bookid
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

link = soup.find("div","pub_format_single").find("a","pdf").attrs['href']
print "downloading", link
response = urllib2.urlopen(link)
file = open("first_edition.pdf", 'wb')
file.write(response.read())
file.close()
print "download completed"

json_file =  open('versions.json')
data = json.load(json_file)
#retrieve most recent version
newversion = copy.deepcopy(data['versions'])[-1]
newversion['versiontype'] = 'first_edition'
newversion['publishedAt'] = datetime.datetime.now().isoformat()
data['versions'].append(newversion)
json_file.close()
json_file =  open('versions.json','w')
print(json.dump(data,json_file))
json_file.close()

