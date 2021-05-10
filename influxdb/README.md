# InfluxDB

## 특징 
- log 저장에 사용되는 elasticsearch는 full-text 검색에 특화된 document indexing database. 검색이 용이해야 하는 경우에 사용함.
- influx-db 는 time-series database. 검색기능 보다는 모니터링에 필요한 time-series 기능만 있어, elastic search처럼 indexing을 안해서, 쓰기가 빠르다.
- textual query기능은 없음. 이를 위해 추가 엔진이 필요.
- 조합 : StatsD reporter - Telegraf - influxDB - Grafana
- 조합2 : Spring Actuator - Telegraf(optional) - influxDB - Grafana

## Install by Docker
```shell
INFLUX_PATH=$(PWD)/influxdb
INFLUX_VERSION=2.0.6
docker run \
  --rm influxdb:"$INFLUX_VERSION" \
  influxd print-config > "$INFLUX_PATH"/config.yml

docker run -d \
    --name influxdb \
    --restart unless-stopped \
    -p 8086:8086 \
    -v "$INFLUX_PATH"/.data:/var/lib/influxdb2 \
    -v "$INFLUX_PATH"/config.yml:/etc/influxdb2/config.yml \
    influxdb:"$INFLUX_VERSION" \
    --reporting-disabled
```

## Setup by CLI
https://docs.influxdata.com/influxdb/v2.0/get-started/?t=Docker#optional-set-up-and-use-the-influx-cli

## Reference
https://grafana.com/docs/grafana/latest/getting-started/getting-started-influxdb/
https://www.influxdata.com/blog/getting-started-with-sending-statsd-metrics-to-telegraf-influxdb/