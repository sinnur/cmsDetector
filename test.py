#!/usr/bin/env python2.7

# CMS Detector V1.2
# @penetrat0r
# @sinnur 
# This project is designed to enumerate back-end hosting Content Management Systems and aid security professionals
# In quickly enumerating Content Management Systems and finding potential security vulnerabilities within them

from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
from bs4 import BeautifulSoup
from sys import argv
import sys
import cookielib
import getopt
import requests
import re
import os
import glob
import httplib
from collections import OrderedDict
import md5
import os.path
import imp
import traceback
import time
import socks
import socket

#socks config
ports = 9150
shost = "127.0.0.1"

## socks function sinnur
def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

## socks function sinnur
def socksf():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, shost, ports)
	socket.socket = socks.socksocket
	socket.create_connection = create_connection
	## notify user of current ip address of the tunnel
	ip = requests.get('http://my.ip.fi', headers=headz)
	print colors.red, "-" * 85
	print colors.white, "Using SOCKS Proxy, Current Public IP address: " + colors.lightblue, ip.content

## Added User agent sinnur
headz = {'User-Agent': 'Firefox'}

cmsDetections = []
success = False
enumerationEnabled = False
start_Time = time.time()
try:_ssl.PROTOCOL_SSLv23 = _ssl.PROTOCOL_TLSv1
except:pass

def load_module(code_path):
	#Used to dynamically import signature files
	try:
		try:
			code_dir = os.path.dirname(code_path)
			code_file = os.path.basename(code_path)
			fin = open(code_path, 'rb')

			return  imp.load_source(md5.new(code_path).hexdigest(), code_path, fin)
		finally:
			try: fin.close()
			except: pass
	except ImportError, x:
		traceback.print_exc(file = sys.stderr)
		raise
	except:
		traceback.print_exc(file = sys.stderr)
		raise

def launcher(r, targetURL):
	#Launches detection modules 
	status = r.status_code
	header = str(r.headers).upper()
	content = str(r.content).upper()
	success = False

	print "[Stage One] cmsDetector is currently analyzing the application..."
	for sig in glob.glob("signatures/*.py"):
		result = load_module(sig).check(header,content,targetURL)

		if result:
			try:
				#Attempts to enumerate version if checkVersion function exists
				version = load_module(sig).checkVersion(header, content, targetURL)
				print "\n   >> " + version + "\n"
				elapsedTime = "%.1f" % (time.time() - start_Time)
				if enumerationEnabled == True:
					getExploitDB(version)
					print "[***] Detection took: " + elapsedTime + " seconds", colors.normal + "\n"
					exit()
				else:
					exit()

			except Exception as e: 
				#Enumerates CMS but will not find a version
				fileStage = os.path.splitext(sig)[0]
				stagedFile = os.path.splitext(os.path.basename(fileStage))[0]
				print "\n   >> " + stagedFile.upper() + "\n"
				elapsedTime = "%.1f" % (time.time() - start_Time)
				
				if enumerationEnabled == True:
					getExploitDB(stagedFile)
					print "[***] Detection took: " + elapsedTime + " seconds", colors.normal + "\n"
					exit()
				else:
					print "[*] Detection took: " + elapsedTime + " seconds", colors.normal + "\n"
					exit()
		
	print "\n   >> No CMS was able to be enumerated. \n"

class colors:
	#Used for providing color to printed text
	lightblue = '\033[1;36m'
	blue = '\033[1;34m'
	normal = '\033[0;00m'
	red = '\033[1;31m'
	white = '\033[1;37m'

def help():
	# Prints out the help function, which guides users how to use the script.
	print colors.red, "\n", "-" * 85
	print colors.white, "CMS Detector v1.2", colors.blue
	print "-" * 85
	## added socks option
	print colors.white, "Usage: cmsDetector.py", colors.red,"http://www.somedomain.com", colors.blue,"-s (SOCKS)\n", colors.normal

def banner():
	print "\n"
	print "  ______ .___  ___.      _______. _______   _______ .___________. _______   ______ .___________.  ______   .______      "
 	print " /      ||   \/   |     /       ||       \ |   ____||           ||   ____| /      ||           | /  __  \  |   _  \     "
	print "|  ,----'|  \  /  |    |   (----`|  .--.  ||  |__   `---|  |----`|  |__   |  ,----'`---|  |----`|  |  |  | |  |_)  |    "
	print "|  |     |  |\/|  |     \   \    |  |  |  ||   __|      |  |     |   __|  |  |         |  |     |  |  |  | |      /     "
	print "|  `----.|  |  |  | .----)   |   |  '--'  ||  |____     |  |     |  |____ |  `----.    |  |     |  `--'  | |  |\  \----."
 	print " \______||__|  |__| |_______/    |_______/ |_______|    |__|     |_______| \______|    |__|      \______/  | _| `._____|"
 	print "\n"


def getResponse(targetURL):
	#This function might include additional functionality as well.
	r = requests.get(targetURL, headers=headz)
	newurl = r.url
	if targetURL != newurl:
		print "[*] Redirecting you to " + newurl

	analyzeResponse(r, newurl)

def analyzeResponse(r, targetURL):
	#Analyzes responses and queries signature files for detections
	status = r.status_code
	header = str(r.headers).upper()
	content = str(r.content).upper()
	print colors.blue, "-" * 85
	print colors.white, "We are currently analyzing the site.  Please wait a few moments"
	print colors.red, "-" * 85
	launcher(header, content, targetURL)

	if success == True:
		if enumerationEnabled == True:
			#print "** Breakpoint Enumeration enabled and successful CMS detection: " + cmsDetections[1]
	
			try:
				#Attempt to enumerate CMS vulnerabilities using ExploitDB query
				print colors.white, "\nThe following Content Management System(s) were discovered: "
				print colors.red,"\n".join(map(str, list(set(cmsDetections)))) + " CMS"
				elapsedTime = "%.1f" % (time.time() - start_Time)
				print colors.blue, "Detection took: " + elapsedTime + " seconds", colors.normal
				print "\n", colors.normal
				getExploitDB(cmsDetections[1])
				exit()
			except Exception as e:
				print "Analyze Response exception while attempting to getExploitDB ..."
				#print e
		else:
			
			print colors.white, "\nThe following Content Management System(s) were discovered: "
			print colors.red,"\n".join(map(str, list(set(cmsDetections)))) + " CMS"
			elapsedTime = "%.1f" % (time.time() - start_Time)
			print colors.blue, "Detection took: " + elapsedTime + " seconds", colors.normal
			print "\n", colors.normal
			#print "About to exit analyze response function....."
			exit()
	else:
		#print "Breakpoint.... success == False"
		print colors.red, "No CMS was detected", colors.white,".... Feel free to add a signature and help the project :P \n", colors.normal
		exit()

def getExploitDB(cmsName):
	#This module queries ExploitDB for potential vulnerabilities related to the discovered CMS

	baserequest = requests.get("http://www.exploit-db.com/search/?action=search&filter_page=1&filter_description=notavalidsearchtermbaseline&filter_exploit_text=&filter_author=&filter_platform=0&filter_type=0&filter_lang_id=0&filter_port=&filter_osvdb=&filter_cve=")
	baselineLength = len(baserequest.content)
	#print "Baseline content length = " + str(baselineLength)

	try:
		print "[Stage Two] Enumerating other potential vulnerabilities.."
		exploitQuery = "http://www.exploit-db.com/search/?action=search&filter_page=1&filter_description="
		exploitQuery += cmsName
		exploitQuery += "&filter_exploit_text=&filter_author=&filter_platform=0&filter_type=0&filter_lang_id=0&filter_port=&filter_osvdb=&filter_cve="

		r = requests.get(exploitQuery, headers=headz)
		content = r.content

		#print "About to compare baseline and new request"
		#print "Baseline length: " + str(baselineLength)
		#print "New response length: " + str(len(content))

		if len(content) > baselineLength:

			#print "New response is longer than baseline...."
			soup = BeautifulSoup(content) 
			tables = soup.findAll("td", attrs={"class":"list_explot_description"})
			
			#### Test code assuming a valid response is returned
			print "\n[**] ExploitDB has returned the following potential exploits:\n"

			try:
				for robblers in range(len(tables)):
					x = str(tables[robblers]).split('"')[4::5]
					y = str(x).split(">")[1::2]
					z = str(y[0]).split("<")

					print "   >> " + z[0]
					
			except Exception as e:
				#Thoroughly test here.... Only forseeable test case is a query returning no results
				#Possible to go off content length of response?
				#Might be easier to baseline based on a response with zero returns

				print "Exception was caught when attempting to parse results of exploit db table data"
				print e
		else:
			print "[**] ExploitDB returned no potential vulnerabilities"
			print "\n"
	except Exception as e:
		pass
		#print e

def start(argv):
	try:
		userInput = sys.argv[1]
		try:
			if userInput.endswith("/"):
				getResponse(sys.argv[1])
			else:
				getResponse(sys.argv[1] + "/")
		except Exception as e:
			try:
				if not (userInput.startswith("http://") or userInput.startswith("https://")):
					if userInput.endswith("/"):
						getResponse("http://" + sys.argv[1])
					else:
						getResponse("http://" + sys.argv[1] + "/")

			except Exception:
				if not userInput.startswith("www."):
					if userInput.endswith("/"):
						getResponse("http://www." + sys.argv[1])
					else:
						getResponse("http://www." + sys.argv[1] + "/")
		except Exception:
			print ("You managed to find a bug despite a number of try catch conditions.  Congratulations.")
	except Exception as e:
		print "Hostname lookup has failed.  Please ensure you've entered a proper URL."
		print e

if __name__ == '__main__':
	userInput = sys.argv
	if len(argv) < 2:
		help()
		banner()
		exit()
		## for socks menu sinnur
	elif len(argv) > 2 and sys.argv[2] == '-s':
		socksf()
		start(argv)
		## for calling help sinnur
	elif userInput == '-h' or '--help':
		help()
		banner()
		exit()
	else:
		try:
			banner()
			start(argv[2:])
		except Exception as e:
			print e