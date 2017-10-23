'''
a tools for load any context from all link in the main target page url.
this tools is for educational purpose.
'''


import requests
import time
import lxml.html

l = []
path = ''
target = ""


r = requests.get(target)



file = open(path+'main.html','w')
file.write(r.content)
file.close()
file2 = open(path+'link.txt','w')

dom = lxml.html.fromstring(r.content)

for link in dom.xpath('//a/@href'):
	l.append(link)
	file2.write(str(link)+'\n')


for allLink in l:
	r = requests.get(allLink)
	cal = r.content.replace('/','').split('<title>')
	cal2 = cal[1].split('-')
	print cal2[0]

	file = open(path+str(cal2[0])+'.html','w')
	file.write("<html><body>")

	cal3 = r.content.split('<p>')
	for i in range(1,len(cal3)-1):
		cal4 = cal3[i].split('</p>')
		file.write("<p>")
		file.write(cal4[0])
		file.write("</p>")

	file.write("</body></html>")	

	file.close()

	#time.sleep(0.3)



