#!/usr/bin/python3

from __future__ import division

import urllib.request as ur
from functools import reduce
from time import asctime ,time
import sys
import re
import gzip

class Trer(object):
    def __init__(self,url):
        self.url = url
        self.requester = ur.Request(self.url)
        self.header = {
           'Host':'translate.google.cn',
           'Refer' : 'http://translate.google.cn/?hl=en',
           'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
           'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
           'Accept-Encoding':'gzip,deflate,sdch',
        }

        ## spawn to request
        list(map(lambda x: self.requester.add_header(*x), self.header.items()))
        self.result = ur.urlopen(self.requester)
        self.info = self.result.info()

        self.encode_way = self.check_content_type(self.info)
        self.content_checked_gzip = self.check_gzip(self.result)
        self.content = self.content_checked_gzip.decode(self.encode_way)

       
    def check_gzip(self,buf):
        chars = buf.read(2)
        rest_chars = buf.read()
        if chars == b'\x1f\x8b':
            return gzip.decompress(chars+rest_chars)
        else:
            return buf.read()

    def check_content_type(self,info_dict):
        if not "Content-Type" in info_dict.keys():
            return None
        if "gb" in info_dict['Content-Type'].lower():
            return "gbk"
        elif "utf-8" in info_dict['COntent-Type'].lower():
            return "utf8"
        else:
            return info_dict['Content-Type']
    def get_content(self):
        if self.content :
            return self.content

    @classmethod    
    def search(cls,words,base_search_url="http://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&dt=sw&ie=UTF-8&oe=UTF-8&prev=btn&srcrom=1&ssel=0&tsel=0&q="):
        words_url = ""
        if words:
            words_url = ur.quote(" ".join(words))
        handler = cls(base_search_url+words_url)
        return handler.get_content()

def para(words):
    _words = re.split(r'\[\[',words)
    for word in _words:
        word = word.replace(",,","\n")
        word = word.replace("[","")
        word = word.replace(","," ")
        word = word.replace("]","   ")
        print(word)
if __name__== "__main__":
    words = sys.argv[1:]
    result  = Trer.search(words)
            
    para(result)
