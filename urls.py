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
    "Seinfeld Chronicles",
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
    "Keys",

    # Season 4
    "Trip Part 1",
    "Trip Part 2",
    "Pitch",
    "Ticket",
    "Wallet",
    "Watch",
    "Bubble Boy",
    "Cheever Letters",
    "Opera",
    "Virgin",
    "Contest",
    "Airport",
    "Pick",
    "Movie",
    "Visa",
    "Shoes",
    "Outing",
    "Old Man",
    "Implant",
    "Junior Mint",
    "Smelly Car",
    "Handicap Spot",
    "Pilot Part 1",
    "Pilot Part 2",

    # Season 5
    "Mango",
    "Puffy Shirt",
    "Glasses",
    "Sniffling Accountant",
    "Bris",
    "Lip Reader",
    "Non-Fat Yoghurt",
    "Barber",
    "Masseuse",
    "Cigar Store Indian",
    "Conversion",
    "Stall",
    "Dinner Party",
    "Marine Biologist",
    "Pie",
    "Stand-In",
    "Wife",
    "Raincoats Part 1",
    "Raincoats Part 2",
    "Fire",
    "Hamptons",
    "Opposite"
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
    "http://www.seinfeldscripts.com/TheKeys.html",

    # Season 4
    "http://www.seinfeldscripts.com/TheTrip1.htm",
    "http://www.seinfeldscripts.com/TheTrip2.htm",
    "http://www.seinfeldscripts.com/ThePitch.htm",
    "http://www.seinfeldscripts.com/TheTicket.html",
    "http://www.seinfeldscripts.com/TheWallet.html",
    "http://www.seinfeldscripts.com/TheWatch.html",
    "http://www.seinfeldscripts.com/TheBubbleBoy.htm",
    "http://www.seinfeldscripts.com/TheCheeverLetters.htm",
    "http://www.seinfeldscripts.com/TheOpera.html",
    "http://www.seinfeldscripts.com/TheVirgin.htm",
    "http://www.seinfeldscripts.com/TheContest.htm",
    "http://www.seinfeldscripts.com/TheAirport.htm",
    "http://www.seinfeldscripts.com/ThePick.htm",
    "http://www.seinfeldscripts.com/TheMovie.htm",
    "http://www.seinfeldscripts.com/TheVisa.html",
    "http://www.seinfeldscripts.com/TheShoes.html",
    "http://www.seinfeldscripts.com/TheOuting.htm",
    "http://www.seinfeldscripts.com/TheOldMan.htm",
    "http://www.seinfeldscripts.com/TheImplant.html",
    "http://www.seinfeldscripts.com/TheJuniorMints.htm",
    "http://www.seinfeldscripts.com/TheSmellyCar.htm",
    "http://www.seinfeldscripts.com/TheHandicapSpot.html",
    "http://www.seinfeldscripts.com/ThePilot.html",
    "http://www.seinfeldscripts.com/ThePilot2.html",

    # Season 5
    "http://www.seinfeldscripts.com/TheMango.html",
    "http://www.seinfeldscripts.com/ThePuffyShirt.htm",
    "http://www.seinfeldscripts.com/TheGlasses.htm",
    "http://www.seinfeldscripts.com/TheSniffingAccountant.htm",
    "http://www.seinfeldscripts.com/TheBris.htm",
    "http://www.seinfeldscripts.com/TheLipReader.htm",
    "http://www.seinfeldscripts.com/TheNonFatYogurt.html",
    "http://www.seinfeldscripts.com/TheBarber.htm",
    "http://www.seinfeldscripts.com/TheMasseuse.html",
    "http://www.seinfeldscripts.com/TheCigarStoreIndian.htm",
    "http://www.seinfeldscripts.com/TheConversion.htm",
    "http://www.seinfeldscripts.com/TheStall.htm",
    "http://www.seinfeldscripts.com/TheDinnerParty.html",
    "http://www.seinfeldscripts.com/TheMarineBiologist.htm",
    "http://www.seinfeldscripts.com/ThePie.html",
    "http://www.seinfeldscripts.com/TheStand-In.html",
    "http://www.seinfeldscripts.com/TheWife.html",
    "http://www.seinfeldscripts.com/TheRaincoats.html",
    "http://www.seinfeldscripts.com/TheRaincoats2.html",
    "http://www.seinfeldscripts.com/TheFire.html",
    "http://www.seinfeldscripts.com/TheHamptons.htm",
    "http://www.seinfeldscripts.com/TheOpposite.htm"
]
i = 0 # index number
e = 1 # episode number
s = 1 # season number
while s < 6:
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
