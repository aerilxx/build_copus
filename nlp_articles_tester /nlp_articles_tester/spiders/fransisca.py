# -*- coding: utf-8 -*-
import scrapy

def remove_dup(a):
	i = 0
	while i < len(a):
	   j = i + 1
	   while j < len(a):
	      if a[i] == a[j]:
	         del a[j]
	      else:
	         j += 1
	   i += 1

class FransiscaSpider(scrapy.Spider):
    name = 'fransisca'

    def start_requests(self):
    	urls = ['https://fransiscalifestyle.com']
    	for url in urls:
    		yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self, response):
        	domin = "https://fransiscalifestyle.com"
        	final =[]
        	for i in response.xpath('//a/@href'):
        		blog = i.extract()
        		if blog.startswith(domin):
        			final.append(blog)
    
        	remove_dup(final)
        	with open('fransisca.html', 'a') as links:
        		links.write(str(final))
        	links.close()


    	
