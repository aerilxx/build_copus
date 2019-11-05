# -*- coding: utf-8 -*-
import scrapy
import gspread
from oauth2client.service_account import ServiceAccountCredentials        
import oauth2client 

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


def get_user_url():
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project-10f1ac3d4686.json', scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/12mDHB32G3j4QmGD9TomAklqcNk0zDh6ldNLf40LAi1Q/edit#gid=1045059713")
    worksheet = sheet.get_worksheet(2) 
    url_list = worksheet.col_values(3)
    
    return url_list

class ScrapblogSpider(scrapy.Spider):
    name = 'scrapblog'
    
    def start_requests(self):
        urls = ['http://www.nikkitheblogger.com/',
                'http://www.theincogneatist.com/',
                'http://www.theantwiwaa.com/',
                'http://www.mysweetgenevieve.com/',
                'http://www.effortlesslysophisticated.com/',
                'https://www.likesofablonde.com/',
                'http://www.mrsbowretro.com/',
                'http://aworldofdresses.com/',
                'http://www.myanci.com/',
                'http://www.fashionvoyeur.co.uk/',
                'http://www.fashioninflight.com/',
                'http://www.nicoleineverycolour.com/'
                ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self, response):
        page = response.url.split("//")[-1].replace('/','')
        filename = str(page)+'.txt'
        
        final = []
        for i in response.xpath('//a/@href'):
            blog = i.extract()
            final.append(blog)
            
        remove_dup(final)
        
        with open(filename, 'w') as f:
            f.write(str(final))
        f.close()
        self.log('Saved file %s' % filename)

