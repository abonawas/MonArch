FROM openjdk:14-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache curl
RUN apk add --no-cache tar

RUN curl -LO https://github.com/slacmshankar/epicsarchiverap/releases/download/v0.0.1_SNAPSHOT_13-Nov-2019/archappl_v0.0.1_SNAPSHOT_13-November-2019T15-45-42.tar.gz


RUN pwd

RUN ls -al


RUN tar -zxvf archappl*

RUN curl -O http://mirror.vorboss.net/apache/tomcat/tomcat-9/v9.0.34/bin/apache-tomcat-9.0.34.tar.gz

EXPOSE 17665

CMD ["./quickstart.sh", "apache-tomcat-9.0.34.tar.gz"]
