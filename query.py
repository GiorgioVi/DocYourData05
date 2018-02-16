# -*- coding: utf-8 -*-
"""
We used (https://mtgjson.com/json/PD2.json) for our data. It's a list of
every card in the 2010 Fire and Lightning Series of Magic The Gathering.
Every card has the following fields:
  id                        The unique SHA1 hash of setCode + cardName + cardImageName
  layout                    How this card is formatted. Possible values: normal, split, flip, double-faced, token, plane, scheme, phenomenon, leveler, vanguard, meld
  name                      The string name of this card.
  names                     An array of names if this is a split or double-sided card. Not always present.
  manaCost                  A string of the mana cost symbols. Every symbol is in {} and is either a number(colorless) or a one-letter abbreviation of the colored mana.
  cmc                       This is a number called the Converted Mana Cost. It is the sum of all the mana required to play this card.
  colors                    This is a list of color names derived from the mana cost.
  colorIdentity             An array of one-letter abbreviations for all the colors mentioned on this card.
  type                      This is the card's type. Consists of "supertypes types — subtypes" like "Legendary Creature — Angel"
  rarity                    How rare this card is. One of Common, Uncommon, Rare, Mythic Rare, Special, Basic Land
  text                      The text of the card. Describes its abilities.
  flavor                    Some cards have this. It's a quote to add flavor to the card.
  artist                    The name of the artist who drew this card.
  power                     The offense. This is a number in a string.
  toughness                 The defense. This is a number in a string.
"""

import pymongo


def query(document):
    connection = pymongo.MongoClient("homer.stuy.edu")
    db = connection["its2010again"]
    collection = db["deck"]
    return collection.find(document)

def cursorToList(c):
    l = []
    for e in c:
        l.append(e)
    return l

def get_by_id(id):
    result = query({"id": id})
    for card in result:
        return card

def get_by_name(name):
    result = query({"name": name})
    for card in result:
        return card

def get_cards_with_color(c):
    return cursorToList(query({"colors": c}))

def get_mana_range(minCMC, maxCMC):
    return cursorToList(query({"cmc": {"$lte": int(maxCMC), "$gte": int(minCMC)}}))

def get_by_artist(artist):
    return cursorToList(query({"artist": artist}))

def get_tougher_than(defense):
    return cursorToList(query({"toughness": {"$gte": str(defense)}}))

def get_stronger_than(attack):
    return cursorToList(query({"power": {"$gte": str(attack)}}))

def get_cheaper_tougher(cmc, defense):
    return cursorToList(query({"cmc": {"$lte": int(cmc)}, "toughness": {"$gte": str(defense)}}))

def get_cheaper_stronger(cmc, attack):
    return cursorToList(query({"cmc": {"$lte": int(cmc)}, "power": {"$gte": str(attack)}}))

def get_min_stats(attack, defense):
    return cursorToList(query({"toughness": {"$gte": str(attack)}, "power": {"$gte": str(defense)}}))

print "get_by_name Spark Elemental"
print get_by_name("Spark Elemental")
print ""
print "get_cards_with_color Red"
print len(get_cards_with_color("Red"))
print ""
print "get_mana_range(3, 4)"
print len(get_mana_range(3, 4))
print ""
print "get_by_artist Michael Sutfin"
print get_by_artist("Michael Sutfin")[:2]
print ""
print "get_min_stats(2, 2)"
print len(get_min_stats(2, 2))
print ""
print "get_cheaper_tougher(3, 2)"
print len(get_cheaper_tougher(3, 2))
print ""
print "get_cheaper_stronger(3, 2)"
print len(get_cheaper_stronger(3, 2))