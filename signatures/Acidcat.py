# Detects Acidcat-CMS
# @sinnur @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}
def check(header, content, targetURL):	
    if "Acidcat CMS".upper() in content or "ac_admin_main".upper() in content or "admin/css/admin_import.cs".upper() in content or "acidcat_logo.gif".upper() in content:
        return True	
