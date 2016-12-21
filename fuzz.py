#!/usr/bin/env python

# import modules
import httplib
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
      valid = False    # is url valid
      relative = True # is link relative url addressing
     
      # If tag is a link
      if tag == "a":
        for name, value in attrs:
          # Webpage link
          if name == "href":
            value = value.encode('ascii', 'ignore')
            base  = value # Copy of value that will be modified

            # Begin initial truncation 
            tok = value.split("//")

            # Removing http or https
            if tok[0] == "https:" or tok[0] == "http:":
              base = ''.join(tok[1:])
              relative = False

            # Removing www.
            tok = value.split("www.")
            if len(tok) > 1:
              base = tok[1]
              relative = False
            
            # Extrapolate base url to determine if url is in scope
            if not relative :
              value = base # setting to full path
              base = base.split("/")[0] # removing path to compare
              if base == url :
                valid = True
            # Relative Adressing -- There are two types
            # If address begins with '/' it's relative to base url
            # Otherwise address is relative to base + path url
            else :
              valid = True # Relative will usually be valid
              if value[0] != '/':
                value = baseUrl + basePath + value
              else :
                value = baseUrl + value
              
            print value

baseUrl  = "" 
basePath = ""
// TODO multithreading
// TODO check posix safety

# Gather our code in a main() function
def main(url, path):
    global baseUrl, basePath
    baseUrl = url
    basePath = path
    conn = httplib.HTTPSConnection(url)
    conn.request("GET", path)
    rsp = conn.getresponse()
    print rsp.status, rsp.reason
    data = rsp.read()
    parser = MyHTMLParser()
    parser.feed(data)
    conn.close()

if __name__ == '__main__':
    url = 'resources.allsetlearning.com' 
    path = '/chinese/grammar/'
    main(url, path)
