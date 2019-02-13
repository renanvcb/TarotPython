import random

#Dictionary with the card values as keys and their names
tarot = {1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

#created a new dictionary named "spread" with three cards pulled from the tarot deck.
#Each card pulled will pop it from the deck.
#Still needs to upgrade it to some kind of random
spread = {}
spread["past"] = tarot.pop(random.randint(1, 22))
spread["present"] = tarot.pop(random.randint(1, 22))
spread["future"] = tarot.pop(random.randint(1, 22))

#print(spread)

#Printing the spread cards. If the name of the card starts with "The", the output do not include the
#word "the" and use what comes in the card name.
for key, value in spread.items():
  if value[:3] == "The":
    print("Your {key} is {value} card.".format(key=key, value=value))
  else:
    print("Your {key} is the {value} card.".format(key=key, value=value))