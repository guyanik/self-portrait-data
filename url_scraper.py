#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 23:10:46 2021

@author: gorkem
"""

import requests
from bs4 import BeautifulSoup

'''
with open("clean-links.txt", "w") as clean_links:
    with open("links.txt", "r") as links:
        for line in links:
            if 4 < line.count('/'):
                line = line[:-1] + ".jpg!Large.jpg\n"
                clean_links.write(line)
                print(line)
'''

with open("urls-and-titles.txt", "w") as urls:
    with open("clean-links.txt", "r") as links:
        for link in links:
            try:
                html = requests.get(link[:-1]).text
                soup = BeautifulSoup(html, "html.parser")
                images = soup.find_all('img')
                
                urls.write(images[0]['src'] + "|" + images[0]['title'] + "\n")
                print(images[0]['title'])
            except:
                try:
                    html = requests.get(link[:-1]).text
                    soup = BeautifulSoup(html, "html.parser")
                    images = soup.find_all('img')
                    
                    urls.write(images[0]['src'] + "|" + images[0]['alt'] + "\n")
                    print(images[0]['alt'])
                except Exception as exc:
                    print(f"Exception occured while extracting url from {link} {str(exc)}")
    urls.close()

