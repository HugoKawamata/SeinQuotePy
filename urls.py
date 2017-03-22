class Episode:
    def __init__(self, name, sn, en, url):
        self.name = "The " + name
        self.sn = sn
        self.en = en
        self.url = url

    def __repr__(self):
        return "S" + str(self.sn) + " E" + str(self.en) + ": " + self.name

eps = []

names = [
    # Season 1
    "Pilot",
    "Stakeout",
    "Robbery",
    "Male Unbonding",
    "Stock Tip",

    # Season 2
    "Ex-Girlfriend",
    "Pony Remark",
    "Jacket",
    "Phone Message",
    "Apartment",
    "Statue",
    "Revenge",
    "Heart Attack",
    "Deal",
    "Baby Shower",
    "Chinese Restaurant",
    "Busboy"
]

urls = [
    # Season 1
    "http://www.seinfeldscripts.com/TheSeinfeldChronicles.htm",
    "http://www.seinfeldscripts.com/TheStakeout.htm",
    "http://www.seinfeldscripts.com/TheRobbery.htm",
    "http://www.seinfeldscripts.com/MaleUnbonding.htm",
    "http://www.seinfeldscripts.com/TheStockTip.htm",

    # Season 2
    "http://www.seinfeldscripts.com/TheExGirlfriend.htm",
    "http://www.seinfeldscripts.com/ThePonyRemark.htm",
    "http://www.seinfeldscripts.com/TheJacket.htm",
    "http://www.seinfeldscripts.com/ThePhoneMessage.htm",
    "http://www.seinfeldscripts.com/TheApartment.htm",
    "http://www.seinfeldscripts.com/TheStatue.htm",
    "http://www.seinfeldscripts.com/TheRevenge.htm",
    "http://www.seinfeldscripts.com/TheHeartAttack.htm",
    "http://www.seinfeldscripts.com/TheDeal.htm",
    "http://www.seinfeldscripts.com/TheBabyShower.htm",
    "http://www.seinfeldscripts.com/TheChineseRestaurant.htm",
    "http://www.seinfeldscripts.com/TheBusboy.htm",

    
    
]
i = 0 # index number
e = 1 # episode number
s = 1 # season number
while s < 3:
    ep = Episode(names[i], s, e, urls[i])
    eps.append(ep)
    i += 1
    e += 1
    if e > 5 and s == 1:
        s += 1
        e = 1
    elif e > 12 and s == 2:
        s += 1
        e = 1
    elif e > 23:
        s += 1
        e = 1
