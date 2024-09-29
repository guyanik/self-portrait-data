#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 01:35:25 2021

@author: gorkem
"""

import urllib.request
import os
from titlecase import titlecase

"""
with open("urls-and-titles.txt", "r") as urls:
    for line in urls:
        print(line)
        parts = line[:-1].split('/')
        filename = parts[-1].split(".")[0].replace("-", " ").title() + " - " + parts[-2].replace("-", " ").title() + ".jpg"
        url = line[:-1]
        try:
            urllib.request.urlretrieve(url, "images/{}".format(filename))
        except Exception as e:
            print(f"Exception occured while downloading image from url {url} {str(e)}")
"""


def uniquify(title):
    counter = 2

    while os.path.isfile(title + ".jpg"):
        title = title + " (" + str(counter) + ")"
        counter += 1

    return title


jpeg_list = []
png_list = []

with open("urls-and-titles.txt", "r") as urls:
    for line in urls:
        print(line)
        line = line.split("|")
        parts = line[0].split("/")
        filename = (
            parts[-1].split(".")[0].replace("-", " ").title()
            + " - "
            + parts[-2].replace("-", " ").title()
            + ".jpg"
        )
        title = titlecase(line[1][:-1])

        extension = parts[-1].split(".")[-1]
        if extension == "jpeg" or extension == "JPEG":
            jpeg_list.append(title)
        if extension == "png" or extension == "PNG":
            png_list.append(title)

        title = uniquify(title)

        try:
            os.rename(filename, title + ".jpg")
        except Exception as exc:
            print(f"{exc}: {title}")
for i in jpeg_list:
    print(i)

print(len(jpeg_list), "\nhela vela velvela\n")

for i in png_list:
    print(i)

print(len(png_list))
