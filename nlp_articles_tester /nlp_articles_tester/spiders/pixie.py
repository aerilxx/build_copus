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

class PixieSpider(scrapy.Spider):
    name = 'pixie'
    
    def start_requests(self):
        
        urls = [
        'http://www.fashionvoyeur.co.uk'
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 

    def parse(self, response):
        final =[]
        for i in response.xpath('//a/@href'):
            blog = i.extract()
            if blog.startswith('http'):
                final.append(blog)

        remove_dup(final)

        with open('pixie.html', 'a') as links:
            #All we'll do is save the whole response as a huge text file.
            links.write(str(final))
        links.close()
