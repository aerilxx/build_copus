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
       
def html_tag(url):
    return '<a href=\''+ url +'\' ><br/> '
       

class RachnaSpider(scrapy.Spider):
    name = 'rachna'

    def start_requests(self):
    	urls = ['https://www.whytostop.com/']
    	for url in urls:
    		yield scrapy.Request(url=url, callback=self.parse) 

   
    def parse(self, response):
    
    	domin = "https://whytostop.com/"
    	final =[]
    	for i in response.xpath('//a/@href'):
            blog = i.extract()
            if blog.startswith(domin):
                final.append(blog)

    	with open('rachna.txt', 'w') as links:
            links.writelines(str(final))
                
    	links.close()
            
         
            
        
