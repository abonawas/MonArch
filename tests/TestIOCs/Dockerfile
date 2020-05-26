FROM epics-base

# RUN curl -LO https://github.com/krallin/tini/releases/download/v0.19.0/tini
# RUN chmod +x /tini

COPY . /app
WORKDIR /app

# ENV EPICS_CA_ADDR_LIST 172.17.255.255
# ENV EPICS_CA_AUTO_ADDR_LIST NO

# ENTRYPOINT ["/tini", "--", "softIoc", "-d", "tanks.db"]
ENTRYPOINT ["softIoc",  "-d",  "tanks.db", "-S" ]

