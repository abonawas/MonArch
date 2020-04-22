FROM epics-base

# RUN dnf -y install wget

# RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64
# RUN chmod +x /usr/local/bin/dumb-init

COPY . /app

WORKDIR /app

# ENV EPICS_CA_ADDR_LIST 172.17.255.255
# ENV EPICS_CA_AUTO_ADDR_LIST NO

# ENTRYPOINT ["dumb-init", "softIoc",  "-d",  "tanks.db"]
ENTRYPOINT ["softIoc",  "-d",  "tanks.db", "-S" ]

