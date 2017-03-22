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
    "Busboy",

    # Season 3
    "Note",
    "Truth",
    "Pen",
    "Dog",
    "Library",
    "Parking Garage",
    "Cafe",
    "Tape",
    "Nose Job",
    "Stranded",
    "Alternate Side",
    "Red Dot",
    "Subway",
    "Pez Dispenser",
    "Suicide",
    "Fix Up",
    "Boyfriend Part 1",
    "Boyfriend Part 2",
    "Limo",
    "Good Samaritan",
    "Letter",
    "Parking Space",
    "Keys"
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

    # Season 3
    "http://www.seinfeldscripts.com/TheNote.html",
    "http://www.seinfeldscripts.com/TheTruth.htm",
    "http://www.seinfeldscripts.com/ThePen.html",
    "http://www.seinfeldscripts.com/TheDog.htm",
    "http://www.seinfeldscripts.com/TheLibrary.htm",
    "http://www.seinfeldscripts.com/TheParkingGarage.htm",
    "http://www.seinfeldscripts.com/TheCafe.html",
    "http://www.seinfeldscripts.com/TheTape.htm",
    "http://www.seinfeldscripts.com/TheNoseJob.html",
    "http://www.seinfeldscripts.com/TheStranded.html",
    "http://www.seinfeldscripts.com/TheAlternateSide.htm",
    "http://www.seinfeldscripts.com/TheRedDot.htm",
    "http://www.seinfeldscripts.com/TheSubway.htm",
    "http://www.seinfeldscripts.com/ThePezDispenser.htm",
    "http://www.seinfeldscripts.com/TheSuicide.html",
    "http://www.seinfeldscripts.com/TheFixUp.html",
    "http://www.seinfeldscripts.com/TheBoyfriend1.htm",
    "http://www.seinfeldscripts.com/TheBoyfriend2.htm",
    "http://www.seinfeldscripts.com/TheLimo.html",
    "http://www.seinfeldscripts.com/TheGoodSamaritan.html",
    "http://www.seinfeldscripts.com/TheLetter.htm",
    "http://www.seinfeldscripts.com/TheParkingSpace.html",
    "http://www.seinfeldscripts.com/TheKeys.html"
]
i = 0 # index number
e = 1 # episode number
s = 1 # season number
while s < 4:
    print(str(s) + " " + str(e) + " " + str(i))
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
