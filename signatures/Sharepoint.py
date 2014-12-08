# Detects Sharepoint
# @sinnur @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}

def check(header, content, targetURL):	
		if "/_vti_bin/spsdisco.aspx".upper() in content or '%2FPages%2Fdefault'.upper() in content:
			return True
		else:
			if "SharePoint".upper() in header:
			   	return True
#
#def checkVersion(header, content, targetURL):
#    versionURL = ["/_layouts/help.aspx"]
#    for url in versionURL:
#        r = requests.get(targetURL + url)
#        content = str(r.content).upper()
#        if r.status_code == 200:
#            try:
#                print "testing version"
#                match = re.compile(ur'Sharepoint\sServer\s\d{4}', re.IGNORECASE)
#                print match
#            except Exception:
 #               pass 
            #print content