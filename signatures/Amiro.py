# Detects Amiro
# @sinnur @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}

def check(header, content, targetURL):
    if "_mod_files/".upper() in content or "var AMI_SessionData".upper() in content or "var active_module_link".upper() in content:
        return True
    else:
        if "Powered by: Amiro CMS".upper() in content or "www.amirocms.com".upper() in content or "www.amiro.ru".upper() in content:
            return True

