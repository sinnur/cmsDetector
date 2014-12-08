# Detects Yanel CMS
# @penetrat0r
# Test site veriifed http://www.yanel.org/en/about.html

import requests
headz = {'User-Agent': 'Firefox'}

directories = ["admin"]

def check(header, content, targetURL):
    if "_yanel-analytics".upper() in header:
        return True
    else:    
        for directory in directories:
            r = requests.get(targetURL + directory, headers=headz)
            if r.status_code == 200:
                if "yanel".upper() in content:
                    return True