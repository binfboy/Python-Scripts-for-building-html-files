import os  
#IMG2HTML.py creates a html page that has all 
#images from specified folder.
#02/25/2017
#Joshua Rhoades
#
#Set path to folder containing images
#Enter TITLE of Page
#Enter COMMENT that you may want
#set IMGSIZE, which is a % of page, 100 is probably best
#run in command line IMG2HTML.py >PAGENAME.html
#
#############################################################
#USER VARIABLES
#############################################################
path = 'goodpics/' #Set folder path
TITLE = 'RANDOM' #Set title page
COMMENT = 'Random pictures that I like!' #Any text before pictures?
IMGSIZE = '100' #how big? use 100 for full
MARGIN = '16.5' #16.5 seems like a good value
#############################################################

print '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
print '<html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>' + TITLE + '</title><style type="text/css">'
print 'body {margin: ' + MARGIN + '%;font-weight: normal; font-style: normal;font-family: Arial,Helvetica,sans-serif;}'
print 'img.one{height:' + IMGSIZE + '%;width:' + IMGSIZE + '%;}</style>'
print '</head><body style="background-color: wheat;">'
print '<div style="text-align: center;">'
print '<h1><big style="font-weight: normal;"><big><big><big>|||</big></big></big></big><big style="font-weight: bold;"><big><big><big>BINF BOY</big></big></big></big><big style="font-weight: normal;"><big><big><big>|||</big></big></big></big></h1>'
print '</div><div style="text-align: center; font-weight: bold;">'
print '<h2><big><a href="HOME.html">HOME</a> | <a href="TRAVEL.html">TRAVEL</a> | <a href="SCIENCE.html">SCIENCE</a> | <a href="PHOTOGRAPHY.html">PHOTOGRAPHY</a>| <a href="TECH.html">TECH</a> | <a href="ABOUT.html">ABOUT</a> | <a href="CONTACT.html">CONTACT</a>'
print '<br></big></h2></div>'

print '<span style="text-decoration: underline;"><span style="font-weight: bold;"></span></span><br>'
print '<br><br><br><br>' + COMMENT + '<br>'



for root, dirs, filenames in os.walk(path):
    for f in filenames:
		#print '<br><img style="width: 1234px; height: 822px;" src="' + path + f +'" alt="f"><br>'
		print '<br><img class="one" src="' + path + f +'"><br>'
		fullpath = os.path.join(path, f)
		log = open(fullpath, 'r')
print '</body></html>'









