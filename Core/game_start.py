#!/usr/bin/env python

import sys
import sqlite3
import os.path
import time
import login

print '''
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	~|  Welcome to War for the Zone Beta!   |~
	~| Type install the first time you play |~
	~|         Type start to begin          |~
	~|       Type help for more info        |~
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

def startGame():
	print 'This game will test your abilities to survive in harsh apocalyptic conditions.'
	time.sleep(1)
	inputPlayerInfo()

def installDB():
	print "Installing db"
	# create a table
	cursor.execute("""CREATE TABLE players
			  (user text, password text, screen_name text, faction text) 
		   """)
			   
def inputPlayerInfo():
	print 'Welcome to War For the Zone.'
	playerName = raw_input("Type your login:")

	rec = getPlayer(playerName)
	time.sleep(1)
	
	if rec == None:
		print 'Welcome then, ' + playerName
		playerPassword = login.getPasswordInput("Make a new password");
		#'\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'
		
		screenName = raw_input("Make a Screen-Name:")
		print 'your screen name is ' + screenName
		
		for faction in factions:
			print faction 

		playerFaction = raw_input("Please choose one of the factions:")
		if playerFaction not in factions:
			print "That is not a faction. please fill out your information again."
			inputPlayerInfo()
		else:
			print 'You have chosen the faction ' + playerFaction

		cursor.execute("INSERT INTO players (user, password, screen_name, faction) VALUES (?, ?, ?, ?)",  (playerName, str(playerPassword), screenName, playerFaction))
		
		conn.commit()
	else:
		playerPassword = login.getPasswordInput("Type your password");
		
		if str(rec[1]) == playerPassword:
			print "Welcome back %s" % rec[0]
		else:
			print "Password incorrect"
			print str(rec[1])
			print playerPassword

def getPlayer(playerName):
	cursor.execute("SELECT * from players where user=?", (playerName,))
	for rec in cursor:
		return rec

currentCommand = raw_input(">")
		
conn = sqlite3.connect("game.db") 		
cursor = conn.cursor()

allCommands = {"start": "start the game", "exit":"quit the game",
"help":"list all available commands", "install":"Install the base files"}

factions = {"Loners": "Lone wanderers who choose no side", "Bandits":"Dastardly muggers and outlaws of the Zone",
	"Army":"Soldiers who kill most who enter their currently expanding territory", "Mercenaries":"Merciless guns for hire", "New Freewind":"An unknown faction that is somewhat friendly to most",
	"Dolgotarv":"A militarisitc faction with a small supply of military grade equipment", 
	"Scientists":"A group of rather enthusiastic ecologists that study the zones anomalous traits"}
	

if currentCommand not in allCommands:
	print "Command does not exist - type help for more."
else:
	print "\'%s\'" % (currentCommand)
	if currentCommand == 'install':
		installDB()
		print 'Installed base files'
	elif currentCommand == 'exit': 
		print 'exiting'
		time.sleep(3)
		sys.exit()
	elif currentCommand == 'start':
		startGame()

for i in allCommands:
	print "%s > %s" % (i, allCommands[i])