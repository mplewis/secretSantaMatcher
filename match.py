import random

import yaml
with open('people.yml', 'r') as peopleData:
	peopleData = yaml.load(peopleData)

people = sorted(peopleData.keys())
	
random.seed()
noGifterYet = people[:]

# {key : value} --> {gifter : recipient}
naughtyOrNiceDict = {}

while noGifterYet != []:
	for person in people:
		try:
			possRecipients = list(set(noGifterYet).difference(peopleData[person]['willNotGive']))
			if person in possRecipients:
				possRecipients.remove(person)
			recipient = random.choice(possRecipients)
			noGifterYet.remove(recipient)
			naughtyOrNiceDict[person] = recipient
		except IndexError:
			# Ran out of people. Restarting...
			noGifterYet = people[:]
			naughtyOrNiceDict = {}

for person in people:
	print person, 'is giving a gift to', naughtyOrNiceDict[person]