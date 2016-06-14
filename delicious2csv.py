#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 12/29/10
# Source: https://gist.github.com/ckoehn/779847

from HTMLParser import HTMLParser # Python 2
import pandas as pd
# from html.parser import HTMLParser # Python 3 


########################################################################
class BookmarkParser(HTMLParser):
    """
    Parses a delicious.com bookmark file and transforms it into a list of 
    dictionaries.
       
    Usage:
    b = BookmarkParser()
    b.feed(open('delicious.htm').read())
    b.close()
    print b.bookmarks
    
    Output:
    [{'tags': ['flash', 'actionscript', 'blog'], 
    'add_date': '1204034881', 
    'title': 'blog.je2050.de - blog and database of joa ebert', 
    'private': False, 
    'note': '', 
    'href': 'http://blog.je2050.de/'}, ...]
    """
    
    #----------------------------------------------------------------------
    def reset(self):
        HTMLParser.reset(self)
        self.bookmarks = []
        self.last_bookmark = {}
        
                
    #----------------------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            bookmark = {}        
            bookmark['title'] = u''
            bookmark['note'] = u''
            
            for k, v in attrs:
                if k == 'href':
                    bookmark['href'] = v
                elif k == 'add_date':
                    bookmark['add_date'] = v
                elif k == 'private':
                    bookmark['private'] = int(v)
                elif k == 'tags':
                    bookmark['tags'] = v
                
            self.bookmarks.append(bookmark)
            self.last_bookmark = bookmark
    
        
    #----------------------------------------------------------------------       
    def handle_data(self, data):
        if self.lasttag == 'a' and self.last_bookmark['title'] == '':
            self.last_bookmark['title'] = str(data).rstrip()
            
        if self.lasttag == 'dd' and self.last_bookmark['note'] == '':
            self.last_bookmark['note'] = str(data).rstrip()
            
if __name__ == '__main__':
    b = BookmarkParser()
    b.feed(open('delicious.html').read())
    b.close()
    
    df = pd.DataFrame(b.bookmarks)
    df.to_csv('delicious.csv')
