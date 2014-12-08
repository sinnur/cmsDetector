# Detects Weebly CMS
# @penetrat0r
# Find additional logic for this module

import requests
headz = {'User-Agent': 'Firefox'}

def check(header, content, targetURL):
	if "weebly".upper() in content:
		return True


