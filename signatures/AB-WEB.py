# Detects AB-WEB CMS
# @ccampbell232 @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}
def check(header, content, targetURL):	
    if "AB WEB".upper() in content or "bdp_z01_z02_l".upper() in content or "hdp_z01_z03_l".upper() in content or "Imprimer".upper() in content:
        return True	
