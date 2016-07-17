from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os


def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),"html.parser")
def get_image(query_get):
  image_type = "Any Type"
    # you can change the query for the image  here  
  query = query_get
  query= query.split()
  query='+'.join(query)
  url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
  print url
  header = {'User-Agent': 'Mozilla/5.0'} 
  soup = get_soup(url,header)

  images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
  #print images
  for img in images:
    raw_img = urllib2.urlopen(img).read()
    #add the directory for your image here 
    DIR="C:\\Users\\ahmetwww\\Desktop\\youtube\\"
    cntr = len([i for i in os.listdir(DIR) if query in i]) + 1
    print cntr
    f = open(DIR + query + "_"+ str(cntr)+".jpg", 'wb')
    f.write(raw_img)
    f.close()

def download():
  import voice as v
  print "\n\nPlease tell some words to search and download.\n\n"
  query_sent = v.voice()
  print query_sent
  print "We understood from your speech that and we are going to download images.Are you sure ?  Yes/No" 
  voice_control = v.voice()
  if voice_control == "yes" or voice_control == "Yes" or voice_control =="YES":
    get_image(query_sent)
  else:
    download()
