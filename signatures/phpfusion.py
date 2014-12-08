# Detects phpfusion
# @ccampbell232


import requests
import re
headz = {'User-Agent': 'Firefox'}
directories = ["themes/Gillette/styles.css", "register.php", "news.php", "index.php"]

def check(header, content, targetURL):
    if "alt='PHP-Fusion Powered Website'".upper() in content or "scapmain-right'>".upper() in content or "Powered by <a href='https://www.php-fusion.co.uk'>PHP-Fusion</a> Copyright &copy; 2014 PHP-Fusion Inc<b".upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory, headers=headz)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if ".admin-message".upper() in content: 
                        return True
                    elif "noscript-message admin-message".upper() in content:
                        return True
            except Exception:
                pass
