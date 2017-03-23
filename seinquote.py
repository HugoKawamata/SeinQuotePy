#!/usr/bin/env python3

import sys
from lxml import html
import requests
import urls


if len(sys.argv) != 2:
    sys.exit("Usage: seinquote keyphrase\nTo use a keyphrase with"
             "multiple words, enclose the phrase in quotation marks.")
else:
    quot = sys.argv[1]

trueEps = []

print("Searching scripts...\n")
for episode in urls.eps:
    # Get all the text from the document
    page = requests.get(episode.url)
    tree = html.fromstring(page.content)
    content = tree.xpath('//div[@id="content"]//p')
    text = ["".join(item.xpath('.//text()')) for item in content]
    if len(text) == 0:
        print("Something's wrong with the formatting of episode " + 
        episode.name)
    final = ""
    for item in text:
        final += (item)

    # Scan it for instances of quot
    if quot in final:
        trueEps.append(episode)
        print("□", end="")
    else:
        print("■", end="")
    sys.stdout.flush()
print("\n")
for episode in trueEps:
    print(episode.__repr__())