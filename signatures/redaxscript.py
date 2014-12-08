# Detects Redaxscript
# @ccampbell232


import requests
import re
headz = {'User-Agent': 'Firefox'}
directories = ["templates/default/images/redaxscript.svg", "admin", "index.php"]

def check(header, content, targetURL):
    if '"generator" content="Redaxscript'.upper() in content or 'Powered by <a class="link_powered_by" href="http://redaxscript.com">Redaxscript</a>'.upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory, headers=headz)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if 'class="js_panel_admin panel_admin">'.upper() in content: 
                        return True
                    elif '15.378-15.357s-6.892-15.358-15.357-15.358z"/></svg>'.upper() in content:
                        return True
            except Exception:
                pass
