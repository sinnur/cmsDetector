# Detects AtomicCms
# @ccampbell232 @penetrat0r

import requests
#"Account/LogOn/?ReturnUrl=%2fadmin%2f"
directories = ["Account/LogOn/"]
headz = {'User-Agent': 'Firefox'}

def check(header, content, targetURL):
    if "/scripts/syntaxhighlighter/scripts/".upper() in content or "AtomicCms".upper() in content:
        return True
    else:    
        for directory in directories:
            r = requests.get(targetURL + directory, headers=headz)
            if r.status_code == 200: 
                if "content/liquid-admin/admin-login.css".upper() in content:
                    return True

