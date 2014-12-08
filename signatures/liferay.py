# Detects LifeRay CMS
# @penetrat0r

import requests
headz = {'User-Agent': 'Firefox'}
def check(header, content, targetURL):
    if 'liferay.aui'.upper() in content:
        return True

