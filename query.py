"""
We used (https://mtgjson.com/json/PD2.json) for our data. It's a list of
every card in the 2010 Fire and Lightning Series of Magic The Gathering.
Every card has the following fields:
  id                        The unique SHA1 hash of setCode + cardName + cardImageName
  layout                    How this card is formatted. Possible values: normal, split, flip, double-faced, token, plane, scheme, phenomenon, leveler, vanguard, meld
  names                     The string name of this card.
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