################################################################################## MODULE IMPORTS BELOW ######################################################
from guizero import App, Text, TextBox, Box, PushButton, Combo, MenuBar, Window, ListBox
import datetime
import sqlite3
import os
import os.path
##############################################################################################################################################################

################################################################################## FUNCTIONS/PROOCEDURES BELOW ###############################################
def sqlExecutor(sql):
	databaseConnection = sqlite3.connect(databaseFile)
	localCursor = databaseConnection.cursor()
	localCursor.executescript(*sql)
	databaseConnection.commit()
	databaseConnection.close()
####
##############################################################################################################################################################

################################################################################## MAIN CODE BELOW ########################################################### 
databaseFile = 'zooAppDB.db'
#if os.path.exists(databaseFile):
#    os.remove(databaseFile)
#####
#sqlExecutor(["""
#CREATE TABLE "zooAppDB_userdata" (
#	"user_ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#	"user_forename"	TEXT,
#	"user_surname"	TEXT,
#	"user_name" TEXT,
#	"user_password" TEXT,
#	"user_email" TEXT,
#	"user_phone" TEXT,
#	"user_created" TEXT
#);
#CREATE TABLE "zooAppDB_bookingdata" (
#	"booking_ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#	"booking_userid"	TEXT,
#	"booking_ticketquantity"	TEXT,
#	"booking_ticketdate" TEXT,
#	"booking_datebooked" TEXT
#);
#CREATE TABLE "zooAppDB_feedbackdata" (
#	"feedback_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#	"feedback_userid"	TEXT,
#	"feedback_improvetext"	TEXT,
#	"feedback_navigatetext" TEXT,
#	"feedback_stars" TEXT,
#	"feedback_date" TEXT
#);
#"""])
