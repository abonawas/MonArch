FROM openjdk:14-alpine

WORKDIR /aa

RUN apk add --no-cache curl tar tini

RUN curl -LO https://github.com/slacmshankar/epicsarchiverap/releases/download/v0.0.1_SNAPSHOT_13-Nov-2019/archappl_v0.0.1_SNAPSHOT_13-November-2019T15-45-42.tar.gz

RUN tar -zxvf archappl*

RUN curl -LO http://mirror.vorboss.net/apache/tomcat/tomcat-9/v9.0.34/bin/apache-tomcat-9.0.34.tar.gz
RUN mv apache-tomcat* apache-tomcat.tar.gz

RUN curl -LO https://github.com/prometheus/node_exporter/releases/download/v1.0.0-rc.0/node_exporter-1.0.0-rc.0.linux-amd64.tar.gz
RUN tar xzvf node_exporter* && rm node_exporter*.gz && mv node_exporter* node_exporter

COPY ./docker-entrypoint.sh /aa/docker-entrypoint.sh

EXPOSE 9100
EXPOSE 17665

CMD ["/sbin/tini", "/bin/sh", "/aa/docker-entrypoint.sh"]
