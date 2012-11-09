#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import yaml

with open('people.yml', 'r') as peopleData:
	peopleData = yaml.load(peopleData)

people = sorted(peopleData.keys())

random.seed()
noGifterYet = people[:]
numTries = 1

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
			numTries += 1
			noGifterYet = people[:]
			naughtyOrNiceDict = {}

for person in people:
	print person + ' is giving a gift to ' + naughtyOrNiceDict[person] + '.'

print ''

notMentionedYet = people[:]
numCircles = 0
while notMentionedYet != []:
	numCircles += 1
	person = notMentionedYet[0]
	while person in notMentionedYet:
		notMentionedYet.remove(person)
		print person, '\xE2\x86\x92 ', # right-pointing arrow: →; http://unix.stackexchange.com/a/25907
		person = naughtyOrNiceDict[person]
	print person + '\n'

if numCircles == 1:
	circlePlural = ' circle.'
else:
	circlePlural = ' circles.'

if numTries == 1:
	tryPlural = ' try.'
else:
	tryPlural = ' tries.'

print str(numCircles) + circlePlural
print 'Done after ' + str(numTries) + tryPlural