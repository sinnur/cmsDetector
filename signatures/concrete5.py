# Detects Concrete5
# @sinnur


import requests
import re

headz = {'User-Agent': 'Firefox'}
directories = ["concrete/css/ccm.tinymce.css", "concrete/js/ccm.app.js", "index.php"]

def check(header, content, targetURL):
    if 'generator" content="concrete5'.upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory, headers=headz)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if 'ul.ccm-dialog-tabs'.upper() in content: 
                        return True
                    elif 'ccm-block-type-available'.upper() in content:
                        return True
            except Exception:
                pass
