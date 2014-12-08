# Detects Movable Type
# @sinnur


import requests
import re
headz = {'User-Agent': 'Firefox'}
directories = ["admin/mt/mt.cgi", "atom.xml"]

def check(header, content, targetURL):
    if 'content="Movable Type'.upper() in content:
        return True
    elif '/mt-static/'.upper() in content:
        return True    
    elif '/mt-static/mt.js'.upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory, headers=headz)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if "/admin/mt/mt.cgi".upper() in content or "<title>Sign in | Movable Type".upper() in content:
                        return True
                    elif '>Movable Type Pro</generator>'.upper() in content:
                        return True
            except Exception:
                pass
