from outline_api import (
    Manager)
import urllib3

import settings

urllib3.disable_warnings()

apiurl = settings.APIURL
apicert = settings.APICERT

manager = Manager(apiurl=apiurl, apicrt=apicert)

active_keys = manager.all_active()
if active_keys:
    print(active_keys)

all_keys = manager.all()
if all_keys:
    print(all_keys)
