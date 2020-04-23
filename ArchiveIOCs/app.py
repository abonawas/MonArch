import requests
import time

while True:
    retries = 100
    try:
        res = requests.get("http://archappl:17665/mgmt/bpl/archivePV?pv=tank1,tank2,tank3,tank4,tank5,tank6&samplingperiod=1&samplingmethod=MONITOR")
        res.raise_for_status()
        break
    except requests.exceptions.RequestException as e:
        print("could not connect to Archiver Appliance", e)
        if retries <= 0:
            break
    retries -= 1
    time.sleep(1)

print("all good! OK")
print("all good! OK")
print("all good! OK")
print("all good! OK")
print("all good! OK")

