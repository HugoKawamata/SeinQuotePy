#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup
import mechanize
import urls


if len(sys.argv) != 2:
    sys.exit("Usage: seinquote keyphrase\nTo use a keyphrase with"
             "multiple words, enclose the phrase in quotation marks.")
else:
    quot = sys.argv[1]

browser = mechanize.Browser()
trueEps = []

print("Searching scripts...\n")
for episode in urls.eps:
    try:
        # Get all the text from the document
        page = browser.open(episode.url)
        soup = BeautifulSoup(page.read(), features="lxml")

        content = soup.find("div", { "id": "content" })
        text = [p.text.lower() for p in content.find_all("p")]

        if len(text) == 0:
            print("Something's wrong with the formatting of episode", episode.name)

        final = ""
        for item in text:
            final += (item)

        # Scan it for instances of quot
        if quot.lower() in final:
            trueEps.append(episode)
            print("□", end="")
        else:
            print("■", end="")
        sys.stdout.flush()
    except:
        print("Something's wrong with the formatting of episode", episode.name)
        pass
print("\n")

for episode in trueEps:
    print(episode.__repr__())
