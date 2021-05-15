# Telegraf

## Description
- InfluxDB와 같이 사용함.
- statsD형식의 데이터를 받아서 처리

## Get Started
https://docs.influxdata.com/influxdb/v2.0/get-started/?t=Docker#use-telegraf

### install telegraf on server
https://portal.influxdata.com/downloads/  

### Configure Telegraf conf file

#### No code solution
- 특별한 코드 설정 없이, plugin 적용 만으로 metric 수집 가능
- [Automatically Configure](https://docs.influxdata.com/influxdb/v2.0/write-data/no-code/use-telegraf/auto-config/)
    - InfluxData UI -> Data -> Telegraf -> create configuration
    - choose plugin agent which monitor the data.(system, docker, etc.)
        - there are lots of plugins which monitor data without code
    - create configuration.
        - the configuration already contains InfluxDataa url, organization, bucket
        - refer to [default configuration](telegraf-default.conf) for monitoring system
    - set the token as environment variable on the server
    - start Telegraf with the configuration url
- [Manually configure](https://docs.influxdata.com/influxdb/v2.0/write-data/no-code/use-telegraf/manual-config/)
    - able to modify configuration on InfluxData UI
- [Telegraf Plugins](https://docs.influxdata.com/telegraf/v1.18/plugins/)

#### StatsD input plugin
- 서버 애플리케이션 metric을 telegraf로 보내서, aggregation등의 가공처리를 한 후에, influxDB로 보냄.
https://github.com/influxdata/telegraf/tree/master/plugins/inputs/statsd
https://www.influxdata.com/blog/getting-started-with-sending-statsd-metrics-to-telegraf-influxdb/