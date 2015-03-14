#!/usr/bin/python
#encoding:utf-8

import requests
import re

domain = 'http://www.google.com'

def submit_form():
	#Submit a form
	resp = requests.get('http://alexa.chinaz.com/?domain='+domain)
	content = resp.content
	#match
	regex = '(?<=<td class="rank_left">)\w*\.\w*\.\w*(?=</td>)'
	m = re.compile(regex)
	urls = m.findall(content)
	for i in urls:
		print i
		
if __name__ == '__main__':
	submit_form()
