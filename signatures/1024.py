# Detects 1024 CMS
# @ccmapbell232 @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}
directories = ["index.php"]

def check(header, content, targetURL):
    if "1024 CMS".upper() in content or "otatfpowered".upper() in content or "includes/admin_default_ajax.js".upper() in content:
        return True    
