# Grafana

## Install
- initial account : admin/admin
```shell
docker run -d --name grafana -p 3000:3000 grafana/grafana
```

## Data Sources
- Influx DB를 추가할 수 있음
    - Flux는 2.0버전용
    - influxQL은 1.x 버전용
  
## Reference
- [Grafana with InfluxDB](https://docs.influxdata.com/influxdb/v2.0/tools/grafana/)
- [Grafana with InfluxDB2](https://grafana.com/docs/grafana/latest/getting-started/getting-started-influxdb/)