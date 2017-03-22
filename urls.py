class Episode:
    def __init__(self, name, sn, en, url):
        self.name = name
        self.sn = sn
        self.en = en
        self.url = url

    def __repr__(self):
        return "S" + self.sn + " E" + self.en + ": " + self.name

eps = []

names = [
    "The Pilot",
    "The Stakeout",
    "The Robbery",
    "Male Unbonding",
    "The Stock Tip"
]

urls = [
    "http://www.seinfeldscripts.com/TheSeinfeldChronicles.htm",
    "http://www.seinfeldscripts.com/TheStakeout.htm",
    "http://www.seinfeldscripts.com/TheRobbery.htm",
    "http://www.seinfeldscripts.com/MaleUnbonding.htm",
    "http://www.seinfeldscripts.com/TheStockTip.htm"
]
i = 0
while i < 5:
    ep = Episode(names[i], 1, i+1, urls[i])
    eps.append(ep)
    i += 1
