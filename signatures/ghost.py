# Detects Ghost CMS
# @penetrat0r
# @ccampbell232 added RSS and JS checks


import requests
import re
headz = {'User-Agent': 'Firefox'}
directories = ["ghost/signin/", "ghost/", "rss/"]

def check(header, content, targetURL):
    if '<meta name="generator" content="Ghost'.upper() in content:
        return True
    elif '/ghost.min.js'.upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory, headers=headz)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if "ghost-login".upper() in content or "<title>Ghost Admin".upper() in content:
                        return True
                    elif '<generator>Ghost'.upper() in content:
                        return True
            except Exception:
                pass

def checkVersion(header, content, targetURL):
    versionURL = ["","ghost/signin/", "ghost/"]

    for url in versionURL:
        r = requests.get(targetURL + url, headers=headz)
        content = str(r.content).upper()
        if r.status_code == 200:
            try:
                version = splitXML(content)
                return "Ghost " + version
            except Exception:
                pass  

def splitXML(content):
    re1='.*?'   # Non-greedy match on filler
    re2='("Ghost \w\\.\w")'   # Double Quote String 1
    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
    m = rg.search(content)
    if m:
        stringLine=m.group(1)
        re1 = '.*?'       
        re2 = '(\w\\.\w)' # Detects version in the format of x.x
        rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
        m = rg.search(stringLine)
        if m:
            detectedVersion = m.group(1)
            return detectedVersion
        else:
            return null
    else:
        return null

