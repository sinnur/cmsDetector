
# Detects Django CMS
# @penetrat0r

import requests

headz = {'User-Agent': 'Firefox'}
directories = ["en/admin/", "admin/"]

def check(header, content, targetURL):
    if "django_language=".upper() in header or "d_lang=".upper() in header:
        return True
    else:
        for directory in directories:
            r = requests.get(targetURL + directory, headers=headz)
            if "Django".upper() in content:
                return True