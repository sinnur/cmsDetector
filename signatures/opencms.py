# Detects OpenCMS
# @penetrat0r
# Basic signature... but then again... who uses OpenCMS anyway

import requests
headz = {'User-Agent': 'Firefox'}
def check(header, content, targetURL):
	if "OpenCms".upper() in content:
		return True
