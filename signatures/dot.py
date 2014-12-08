# Detects Dot CMS
# @penetrat0r

import requests

headz = {'User-Agent': 'Firefox'}
directories = ["dotCMS/login", "admin"]

def check(header, content, targetURL):
	if "Built with dotCMS".upper() in content or 'login?referrer'.upper() in content or "application/themes/dotcms/css/".upper() in content:
		return True
	else:	
		for directory in directories:
			r = requests.get(targetURL + directory, headers=headz)
			if r.status_code == 200:
				if 'dotCMS/login?referrer'.upper() in content or ("SHARED_SESSION_ID".upper() in content and "JSESSIONID=".upper() in content):
					return True

