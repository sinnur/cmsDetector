# Detects Active Builder CMS
# @ccampbell232 @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}
def check(header, content, targetURL):	
    if "/includes_js/site_functions.js".upper() in content or "/includes_js/ccLayers_cross.js".upper() in content or "Talk Active".upper() in content or "ActiveBuilder".upper() in content:
        return True	
