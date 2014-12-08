# Detects Mambo CMS
# @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}
directories = ["administrator/"]

def check(header, content, targetURL):
    
    if "Mambo Communities".upper() in content or "mambo/index.php".upper() in content:
        return True
    else:    
        for directory in directories:
            r = requests.get(targetURL + directory, headers=headz)
            if "Mambo".upper() in content:
                return True
                
