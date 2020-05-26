
FROM epics-base

RUN dnf -y install python3

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3", "update_tanks.py"]
