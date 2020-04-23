# Monitoring The EPICS Archiver Appliance (MonArch)
For now this repository is a test bed for developing a monitoring system for the EPICS Archiver Appliance.
## Set up
Docker compose is being used to automate the set-up of an EPICS development environment.

Before running `docker compose` the epics-base image must be built first.
from the root of the repository run:
```bash
docker build -t epics-base BaseEPICS
```
## Explanation of the different containers
### QuickArchiverAppliance
### TestIOCs
### UpdateIOCs
### ArchiveIOCs




