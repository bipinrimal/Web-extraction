import os
from urllib.request import urlopen
script_dir = os.path.dirname(_file_)
real_path = 'states.txt'
file_path = os.path.join(script_dir,real_path)
states = open(file_path)
for state in states:
	url = 'https://www.gradschools.com/masters/biology/on-campus?in='+str(state)
	response = urlopen(url)
	webContent = response.read()
	f = open('%s.html'%state, 'wb')
	f.write(webContent)
	f.close

from bs4 import BeautifulSoup
for i in *.html:
	file = open(i)
	soup = BeautifulSoup(file,'html.parser')
	rimal = soup.findAll('li',{'itemtype':'http://schema.org/CollegeOrUniversity'})
	for r in rimal:
	print("University: " + r.find('h4').text)
	print("Location: " + r.find("address").text)
	print("Program: " + r.find("h3").text)
	print("Description: " + r.find('p').text)
