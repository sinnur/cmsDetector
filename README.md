cmsDetector.py
==============

Main Coder: penetrator <br>
Breaking main coder's code: sinnur <br>


CMS Detector V1.2

This project is designed to aid security professionals in quickly enumerating back-end content management systems and find potential security vulnerabilities within them.  The first iteration of this application will focus on accurately and efficiently detecting the most common CMS solutions as identified here:

http://en.wikipedia.org/wiki/List_of_content_management_systems

Future versions will then enumerate CMS versions and query a number of sources to find potential associated vulnerabilities and exploit them.  The eventual goal is to combine this application with other enumeration tools to create an effective solution for automating preliminary web application testing.  

Hardcoded Socks Proxy functionality. Options can be easily changed to suit your needs.

Variables to change in the main code are:

ports = 9150<br>
shost = "127.0.0.1"<br>
