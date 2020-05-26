import time
import subprocess

iocs = ["tank1", "tank2", "tank3", "tank4", "tank5"]


init = 0

while True:
    mod = 10
    for tank in iocs:
        subprocess.run(["caput", tank, str(init%mod)])
        mod += 10

    init += 1
    time.sleep(2)

