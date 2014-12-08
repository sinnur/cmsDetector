# Detects Adapt CMS
# @ccampbell232 @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}

def check(header, content, targetURL):    
    if "adaptcms".upper() in header:
        return True    
    else:
        if "AdaptCMS".upper() in content or "www.adaptcms.com".upper() in content:
            return True
            
