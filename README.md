#  MonArch (Monitoring The EPICS Archiver Appliance)
For now this repository is a test bed for developing a monitoring system for the EPICS Archiver Appliance.
## Set up
Docker compose is being used to automate the set-up of an EPICS development environment.

Before running `docker-compose` the epics-base image must be built first.
from the root of the repository run:
```bash
docker build -t epics-base BaseEPICS
```
this will take some time, because we are compiling the EPICS base from source. Now you can run
```bash
docker-compose up
```
This will instansiate 4 Docker containers.
1. QuickArchiverAppliance container running the Archiver Apppliance.
2. TestIOCs container running 5 IOCs: `tank1`, `tank2`, `tank3`, `tank4` and `tank5`.
3. UpdateIOCs container runs a python script that gradually increments the values of the afformentioned IOCs.
4. ArchiveIOCs container runs a python script that instructs the Archiver to start archiving changes in the IOC values.
Once the IOCs have been archived this container will close automatically.
---
To stop and delete all the containers run 
```bash
docker-compose down
```

## Explanation of the different containers
### QuickArchiverAppliance
### TestIOCs
### UpdateIOCs
### ArchiveIOCs




