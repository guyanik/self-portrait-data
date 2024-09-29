#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 01:35:25 2021

@author: gorkem
"""

import urllib.request
import os
from titlecase import titlecase


with open("urls-and-titles.txt", "r") as urls:
    for line in urls:
        line = line.split("|")
        url = line[0]
        title = titlecase(line[1][:-1])
        try:
            urllib.request.urlretrieve(url, "images/{}".format(title))
        except Exception as e:
            print(f"Exception occured while downloading image from url {url} {str(e)}")
            
'''

with open("urls-and-titles.txt", "r") as urls:
    for line in urls:
        print(line)
        line = line.split("|")
        parts = line[0].split('/')
        filename = parts[-1].split(".")[0].replace("-", " ").title() + " - " + parts[-2].replace("-", " ").title() + ".jpg"
        title = titlecase(line[1])
        try:
            os.rename(filename, title)
        except Exception as exc:
            print(f"{exc}: {title}     file not found")
'''

