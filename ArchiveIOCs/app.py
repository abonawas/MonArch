import requests
import time
import sys


def print_all_good():
    print("all good! OK \u2705")
    print("all good! OK \u2705")
    print("all good! OK \u2705")
    print("all good! OK \u2705")
    print("all good! OK \u2705")


def print_not_good():
    print("Failed to archive PVs. Not OK \u274C")
    print("Failed to archive PVs. Not OK \u274C")
    print("Failed to archive PVs. Not OK \u274C")
    print("Failed to archive PVs. Not OK \u274C")


# try to connect a 100 times then give up
for i in range(100):
    try:
        res = requests.get(
            "http://archappl:17665/mgmt/bpl/archivePV?pv=tank1,tank2,tank3,tank4,tank5,tank6&samplingperiod=1&samplingmethod=MONITOR"
        )
        res.raise_for_status()
        print_all_good()
        sys.exit(0)
    except requests.exceptions.RequestException as e:
        print("could not connect to Archiver Appliance", e)
        time.sleep(1)


print_not_good()
sys.exit(1)
