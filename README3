
	Program: jcEdit.py

	A program to display and edit the .dat data files of the jcblock
	(or jcblockAT) program. It is written in Python (version 3) and
	uses the tkinter binding to the tk part of tcl/tk for the GUI.
	It may be run remotely by logging into a Pi via ssh -X <path>,
	locally on the Pi with a TV, keyboard and mouse, or on a Pi with
	a touchscreen display using the matchbox-keyboard program and a
	stylus to enter .dat file record data.

	ORIENTATION:

	This file contains a description of the jcEdit.py program and
	platforms for running it. File README2 contains descriptions of
	the jcblock and jcblockAT programs running on a Raspberry Pi
	processor using various modem models. A description of the
	jcblock program, itself, is present in file README.

	PROGRAM DESCRIPTION:

	The jcblock and jcblockAT programs create and manage three
	data files: callerID.dat, whitelist.dat and blacklist.dat. When
	a call is received, a record of its caller ID data is appended to
	the callerID.dat file. That record is compared to match fields
	in records in the whitelist.dat file and then in the blacklist.dat
	file. If a match is found in the whitelist.dat file, the call is
	accepted and no further action is taken. If a match is found in
	the blacklist.dat file, the program "answers" the call with a
	string of FAX noise and then hangs up the call. If the call is on
	neither list, it is accepted. In all cases a caller ID record is
	appended to the callerID.dat file.

	The whitelist and blacklist must be managed by the user. The
	jcEdit.py program facilitates that process by presenting a GUI
	interface to the files. Note that the files may also be managed
	using a conventional text editor. The task is also nicely
	performed using the FireFTP add-on to the Firefox browser. The
	jcEdit.py program is simply another way.

	To determine the ID of calls that have been received, the user
	needs to be able to view the callerID.dat file records. From
	this information the user may then add appropriate records to
	the whitelist and blacklist files. So the callerID.dat file
	must only be viewed. But it must be possible to add to and delete
	records from the whitelist.dat and blacklist.dat files. The
	jcEdit.py program provides a GUI interface for performing these
	tasks.

	PLATFORMS:

	The simplest way to use the program is to run it on a Pi using
	a TV monitor and USB mouse and keyboard. A more convenient way
	is to run it remotely from a desktop (etc.) machine via a
	ssh -X <path> login. When the program is started on the Pi its
	GUI is displayed on the desktop and the desktop's keyboard and
	mouse may be used (note: a description of the setup for using
	ssh -X <path> is present in the README file for project jablock
	which is also hosted by SourceForge. Enter 'jablock' in the
	SourceForge Search: window. Other useful configuration tips are
	also present in the file).

	The program was also designed to be used with a 7" touchscreen
	display (available from element14, ~$60 see REFERENCES: below). 
	The display takes the place of a TV monitor. The touch feature
	takes the place of a left mouse button. USB keyboard and mouse
	may be used. The matchbox-keyboard program may also be used (see
	REFERENCES:), in which case no TV, keyboard or mouse is needed.
	In this configuration, a stylus is a practical necessity to make
	screen entries (since items are small). To attract the focus of
	the keyboard, a program dialog window must first be taped (or
	clicked).

	Excellent touchscreen configuration information available at the
	web sites referenced below. Some additional tips from my personal
	experience follow:

	Ribbon cable installation:
	I found it quite difficult to insert the ribbon cables into the
	connectors. I had to start a ribbon corner first and then work
	the rest in. Be patient! Make sure the cable is the right way up
	(so that the contacts meet). The connectors are not keyed.

	Screen touch sensitivity:
	I found that the touch screen cursor jumped around randomly.
	The solution was to decrease "mouse" sensitivity. I used a USB
	mouse to make the following menu selections:

		Menu | Preferences | Keyboard and Mouse | Mouse
	
	Then set mouse sensitivity to the lowest value (Low, 100) and
	press OK. It may then be necessary to reboot (don't remember).

	Program startup:
	To start the messagebox-keyboard and jcEdit.py programs using
	a stylus, make a bash script file called startjcEdit in your
	project directory, (mine is: /home/pi/jcblockAT. substitute
	your directory) with the following contents (don't forget the
	'&'s! They run the programs in the background and allow the
	script to continue):

		#!/bin/bash
		/usr/bin/matchbox-keyboard &
		cd /home/pi/jcblockAT
		./jcEdit.py &

	The file must then be made executable (make sure jcEdit.py is
	also executable):

		chmod +x startjcEdit

	Use the Pi's Main Menu Editor to add an entry for the
	program:

		Menu | Preferences | Main Menu Editor | New item

	For the Name: field, enter:
		jcblock file editor (or your choice)
	For the Command: field enter:
		/home/pi/jcblockAT/startjcEdit
	and press OK.

	This adds the entry after Preferences. To get it to show
	up in the Main menu, I had to highlight it and move it up
	using the Move Up button.

	LXterminal colors:
	I found gray foreground on a black background to be too hard
	to see! The colors may be changed as follows (you need to use
	a USB mouse for this):

		Click on the LXterminal icon.
		Right click in the console text area.
		Select: Preferences | Style
		Click the Background color:
			From the color wheel, select a color.
		Do the same for the Foreground.
		Now use the mouse to pull the dialog as high
		as it will go on the screen. You will just see
		the tops of the Cancel and OK buttons.
		Click the OK button (the right one).
		It may now be necessary to reboot (I don't remember).

	SUMMARY:

	That's about it. As indicated earlier, there are other ways to
	manage the .dat files, so this program is not needed for the
	proper operation of jcblock (or jcblockAT). This is my first
	Python program, so I'm sure there are better ways to implement
	it. 

	REFERENCES:

	Raspberry Pi 7" Touchscreen Display (one line URLs):
	http://www.element14.com/community/docs/DOC-78156/l/
				raspberry-pi-7-touchscreen-display

	matchbox-keyboard installation procedure, etc.:
	http://www.element14.com/community/docs/DOC-78327/l/
		turn-the-raspberry-pi-into-a-tablet-with-7-touchscreen

	YouTube touchscreen assembly demo:
	https://www.youtube.com/watch?v=tK-w-wDvRTg

	Touchscreen available in the US:
	http://www.mcmelectronics.com/product/83-16872

	Python books used:
	"Python In Easy Steps", Mike McGrath, ISBN 978-1-84078-596-8,
	www.ineasysteps.com. Concise Python and tkinter starter
	guide (excellent, ~$15).
  
	"Visual Quickstart Guide, Python", Chris Fehily, ISBN 0-201-
	74884-3, Thorough concise Python language description. 2002
	copyright (hopefully there's a more recent edition).

	"Python and Tkinter Programming", John E. Grayson, Manning
	Publications Co., 2000 copyright. Full language reference
	(as of the copyright date).

