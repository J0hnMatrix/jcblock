#! /usr/bin/python3
#
#	Copyright:      Copyright 2016 Walter S. Heath
#
#	Copy permission:
#	This program is free software: you can redistribute it and/or
#	modify it under the terms of the GNU General Public License as
#	published by the Free Software Foundation, either version 3 of
#	the License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You may view a copy of the GNU General Public License at:
#		<http://www.gnu.org/licenses/>.
#
#	Description:
#	A program to display and edit the .dat data files of the jcblock
#	(and jcblockAT) program. It is written in Python (version 3) and
#	uses the tkinter binding to the tk part of tcl/tk for the GUI.
#	It may be run remotely by logging into a Pi via ssh -X <path>
#	or locally on the Pi. It will run on a Pi with a touchscreen
#	monitor using the matchbox-keyboard program to	enter .dat file
#	record data. See README3 for further details.
#
from tkinter import *
import os
import tkinter.messagebox as box

window = Tk()
window.title('jcblock program data file editor' )
window.tk_bisque()

frameUp = Frame(window, bg = 'bisque' )	# Upper frame
frameLo = Frame(window, bg = 'bisque' )	# Lower frame

fileWasChosen = False
dialogIsUp = False
fileString = StringVar()
fileName = StringVar()

#
# Upper frame contents
#

# File display listbox
listbox = Listbox(frameUp, width=82, height = 5, \
                                         font="Courier 10 bold")
# Radio button frame
frameRt = Frame(frameUp, bg = 'bisque' ) # To right in Upper frame
frameRt.pack( side = RIGHT )

# Attach scrollbar to the side of listbox
scrollbar = Scrollbar(frameUp, bg = 'bisque' )
scrollbar.pack(side = RIGHT, fill = Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.pack( side = LEFT )
frameUp.pack( side = TOP, padx = 10, pady = 4 )

# Function to show a prompt
def prompt( promptStr ):
	box.showinfo( 'info', promptStr )

#
# Function to display the selected 'fileName' file.
#
def fileDisplay():
	global fileWasChosen

	listbox.delete(0, END)

	# Make sure the file exists
	if os.path.isfile(fileName.get() + '.dat' ):
		# Open the file and copy its contents to the listbox
		file1 = open( fileName.get() + '.dat', 'r' )
		for line in file1:
			# For display, remove terminating '\n' character
			listLine=line.split('\n')
			listbox.insert(END, listLine[0])
		file1.close()
		fileWasChosen = True
	else:
		prompt( 'No file selected or file does not exist' )

#
# Radio buttons for selecting a file to display
#
Radiobutton( frameRt, text = 'callerID', variable = fileName,\
	bg = 'bisque', value = 'callerID' ).pack(side = TOP, \
                                        anchor = W, pady = 5)
Radiobutton( frameRt, text = 'whitelist', variable = fileName,\
	bg = 'bisque', value = 'whitelist' ).pack(side = TOP, \
                                        anchor = W, pady = 5)
Radiobutton( frameRt, text = 'blacklist', variable = fileName,\
	bg = 'bisque', value = 'blacklist' ).pack(side = TOP, \
                                        anchor = W, pady = 5)
fileButton = Button( frameRt, text = 'Choose file', bg = 'bisque', \
		command = fileDisplay ).pack(side = TOP, pady = 5)

#
# Function to delete a record from a whitelist or blacklist file
#
def deleteRecord():
	global fileString

	# Get the name of the selected file
	fileString = fileName.get()

	# If 'Choose file' button was not pushed,
	if fileWasChosen == False:
		prompt( "Must press 'Choose file' button first" )

	# If no file was selected,
	elif len(fileString) == 0:
		prompt( 'Select whitelist or blacklist first' )

	# If callerIO file was selected,
	elif fileString == 'callerID':
		prompt( 'callerID records cannot be deleted' )

				# If no record was selected,
	elif len(listbox.curselection()) == 0:
		prompt( 'Select (highlight) a record first' )
	else:
		# Get the index of the record to delete
		index = int(listbox.curselection()[0])

		# Open the .dat file and a .tmp file
		file1 = open( fileString + '.dat', 'r' )
		file2 = open( fileString + '.tmp', 'w' )

		# Load all records except the one to delete
		file1.seek( 0 )
		idx = 0
		for line in file1:
			# If the line is not the record to delete,
			if idx != index:
				file2.write( line )
			idx += 1
		file1.close()
		file2.flush()
		file2.close()
		# If a .bak file is present, remove it
		if os.path.isfile(fileString + '.bak' ):
			os.remove( fileString + '.bak' )

		# Now rename the .dat file to .bak and .tmp to .dat
		# (note: the jcblock program closes and reopens files
		# before access, so there should be no confusion here)
		os.rename( fileString + '.dat', fileString + '.bak' )
		os.rename( fileString + '.tmp', fileString + '.dat' )

		# Now redisplay the file
		fileDisplay()

#
# A class that creates a dialog for constructing a new file entry.
#
class AppendDialog:
	global fileWasChosen

	def __init__(self, parent):

		top = self.top = Toplevel(parent)

		label1 = Label( top, width = 15 )
		label2 = Label( top, width = 15 )
		label3 = Label( top, width = 15 )

		label1.grid( row = 2, column = 1, padx = 10, pady = 4 )
		label2.grid( row = 2, column = 2, padx = 10, pady = 4 )
		label3.grid( row = 2, column = 3, padx = 10, pady = 4 )

		label1.configure( text = 'Match field:', bg = 'Tan' )
		label2.configure( text = 'Date field:', bg = 'Tan' )
		label3.configure( text = 'Comment field:', bg = 'Tan' )

		self.matchField = Entry( top )
		self.dateField = Entry( top )
		self.commentField = Entry( top )

		self.enterButton = Button( top )
		self.enterButton.configure( text = 'Enter record', \
			command = self.enterRec, bg = 'Tan' )

		self.cancelButton = Button( top )
		self.cancelButton.configure( text = 'Cancel', \
			command = self.cancelRec, bg = 'Tan' )

		self.matchField.grid( row = 3, column = 1, padx = 5 )
		self.dateField.grid( row = 3, column = 2, padx = 5 )
		self.commentField.grid( row = 3, column = 3, padx = 5 )
		self.enterButton.grid( row = 3, column = 4, padx = 5 )
		self.cancelButton.grid( row = 3, column = 5, padx = 5 )

	def enterRec(self):
		global dialogIsUp

		match = self.matchField.get()
		date = self.dateField.get()
		comment = self.commentField.get()

		if self.testMatchField(match) == True and \
			self.testDateField(date) == True and \
			self.testCommentField(comment) == True:

			# Build a record in a list; then convert it
			# to a string
			recordList = []

			# Fill the list with ' ' chars to start
			j = 0
			while j < 80:
				recordList.append(' ')
				j += 1
			# Insert the match string
			j = 0
			while j < len(match):
				recordList[j] = match[j]
				j += 1
			# Add the terminating '?' char
			recordList[j] = '?'

			# Insert the date string starting in
			#column twenty
			j = 0
			while j < len(date):
				recordList[j + 19] = date[j]
				j += 1
			# Insert the comment string
			j = 0
			while j < len(comment):
				recordList[j + 33] =  comment[j]
				j += 1

			# First, make sure the file ends with a '\n'
			# (if last entry was added manually, some
			# editors add a '\n' automatically, some
			# don't).
			file3 = open( fileString + '.dat', 'r+' )
			file3.seek( 0, 2) # seek to file end
			idx = file3.tell() # get its index
			file3.seek( idx - 1, 0) # seek to last char
			if file3.read(1) != '\n': # if not a '\n',
				file3.seek( 0, 2) # seek to the end
				file3.write('\n') # add a '\n'
			file3.close()

			# Convert the list to a string; slice off
			# the ' ' characters after the comment;
			# add a '\n' at the end
			recordStr = ''.join(recordList[:j + 33]) + '\n'

			# Append the record to the selected file
			file3 = open( fileString + '.dat', 'a' )
			file3.write( recordStr )
			file3.flush()
			file3.close()
			
			self.top.destroy()
			dialogIsUp = False
		return

	def cancelRec(self):
		global dialogIsUp

		self.top.destroy()
		dialogIsUp = False

	def testMatchField(self, match):
		if len(match) == 0 or len(match) > 15:
			prompt( 'Match field must contain one to fifteen chars' )
			return False

		elif '?' in match:
			prompt( "Match field must not contain a '?'" )
			return False
		else:
			return True

	def testDateField(self, date):
		global fileString
		daysInMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		monthNames = ('January', 'February', 'March', 'April', 'May', \
			'June', 'July', 'August', 'September', 'October', \
			'November', 'December' ) 
		if len(date) != 6:
			prompt( "Date field must have format 'MMDDYY'" + \
				" or content '++++++' (blacklist)" )
			return False

		elif date != '++++++' and date.isdigit() == False:
			prompt( "Date field 'MM' 'DD' 'YY' fields must all \
				 be numbers" )
			return False

		elif date == '++++++' and fileString != 'blacklist':
			prompt( "Date field '++++++' only valid in blacklist" )
			return False
		else:
			month = int( date[0:2] )
			day = int( date[2:4] )
			year = int( date[4:6] )
			if month < 1 or month > 12:
				prompt( "In Date field, choose a valid month (01-12)" )
				return False

			elif day < 1 or day > daysInMonth[month - 1]:
				prompt( "In Date field, choose valid day (DD) of \
					month: " + monthNames[month - 1] )
				return False

			elif year < 15:
				prompt( "In Date field, choose valid year (15 or later)" )
				return False
			else:
				return True

	def testCommentField(self, comment):
		if len(comment) < 1 or len(comment) > 46:
			prompt( 'Comment field must contain 1 to 46 characters' ) 
			return False
		else:
			return True
#
# Function to append an record to a whitelist or blacklist file
#
def appendRecord():
	global dialogIsUp
	global fileWasChosen
	global fileString

	# If an appendRecord dialog is already up (displayed), return
	if dialogIsUp == True:
		return
	# Get the name of the selected file
	fileString = fileName.get()

	if fileWasChosen == False:
		prompt( "Must press 'Choose file' button first" )

	# If no file was selected,
	elif len(fileString) == 0:
		prompt( 'Select whitelist or blacklist first' )

	# If callerIO file was selected,
	elif fileString == 'callerID':
		prompt( 'callerID records cannot be appended' )

	# Make an AppendDialog instance and wait for it to finish
	else:
		dialogIsUp = True
		d = AppendDialog(frameLo)
		frameLo.wait_window(d.top)

		# Now redisplay the file
		fileDisplay()

#
# Lower frame contents
#
deleteButton = Button( frameLo )
deleteButton.configure( text = 'Delete the marked record',\
			bg = 'Tan', command = deleteRecord )

appendButton = Button( frameLo )
appendButton.configure( text = 'Append a new record',\
			bg = 'Tan', command = appendRecord )

# Put the buttons in a grid
deleteButton.grid( row = 1, column = 1, columnspan = 2, padx = 5 )
appendButton.grid( row = 1, column = 3, columnspan = 2, padx = 5 )

frameLo.pack( side = BOTTOM, padx = 10, pady = 10 )

window.mainloop()

