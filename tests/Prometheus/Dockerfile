# FROM prom/prometheus
# ADD prometheus.yml /etc/prometheus/
FROM alpine:3.11.6
RUN apk add --no-cache curl tar tini
RUN curl -LO https://github.com/prometheus/prometheus/releases/download/v2.18.0-rc.0/prometheus-2.18.0-rc.0.linux-amd64.tar.gz
RUN tar xzvf prometheus-2.18.0* && rm prometheus-2.18.0*.gz
RUN mv /prometheus-2.18.0* /prometheus-2.18.0
# WORKDIR /prometheus-2.18.0
copy ./prometheus.yml /prometheus-2.18.0/prometheus.yml

# ENV HTTP_PROXY "127.0.0.1:9091"
# ENV HTTPS_PROXY "127.0.0.1:9091"

EXPOSE 9090
ENTRYPOINT ["/sbin/tini", "/prometheus-2.18.0/prometheus", "--config.file=/prometheus-2.18.0/prometheus.yml"]

