# Detects Textpattern
# @sinnur


import requests
import re
headz = {'User-Agent': 'Firefox'}
directories = ["textpattern/", "rss/" , "atom/", "index.php"]

def check(header, content, targetURL):
    if '"generator" content="Textpattern CMS"'.upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory, headers=headz)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if "textpattern.js".upper() in content or "Textpattern</generator>".upper() in content or "<title>Txp".upper() in content: 
                        return True
                    elif 'txp-container'.upper() in content or '_txp_token'.upper() in content:
                        return True
            except Exception:
                pass
