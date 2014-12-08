# Detects Pacer Edition CMS
# @ccampbell232


import requests
import re
headz = {'User-Agent': 'Firefox'}

directories = ["pe/modules/tiny_mce/Pacer%20Edition%20License.txt", "pe/admin/login/", "index.php"]

def check(header, content, targetURL):
    if '"generator" content="The Pacer Edition CMS"'.upper() in content or 'pe/pacer/js/jquery.js"'.upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory, headers=headz)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if "pe_acp_theme".upper() in content or "The Pacer Edition CMS</strong>".upper() in content or '<a href="http://www.thepaceredition.com/" style='.upper() in content: 
                        return True
                    elif 'The Pacer Edition CMS -  TinyMCE plug-in File'.upper() in content:
                        return True
            except Exception:
                pass
