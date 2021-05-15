# InfluxDB Query
https://docs.influxdata.com/influxdb/v2.0/query-data/get-started/

## Bucket
- v2 가 되면서, Database가 Bucket으로 바뀜

## Table
- Group Key
    - start, stop, field를 그룹키 로해서, start와 stop사이에 받은 데이터를 저장한다.
    - start와 stop사이에 받은 데이터의 시간과 값을 저장.
```
Group key: [_start, _stop, _field]
_start:time                      _stop:time           _field:string                      _time:time                  _value:float
------------------------------  ------------------------------  ----------------------  ------------------------------  ----------------------------
2019-04-25T17:33:55.196959000Z  2019-04-25T17:34:55.196959000Z            used_percent  2019-04-25T17:33:56.000000000Z             65.55318832397461
2019-04-25T17:33:55.196959000Z  2019-04-25T17:34:55.196959000Z            used_percent  2019-04-25T17:34:06.000000000Z             65.52391052246094
2019-04-25T17:33:55.196959000Z  2019-04-25T17:34:55.196959000Z            used_percent  2019-04-25T17:34:16.000000000Z             65.49603939056396
2019-04-25T17:33:55.196959000Z  2019-04-25T17:34:55.196959000Z            used_percent  2019-04-25T17:34:26.000000000Z             65.51754474639893
2019-04-25T17:33:55.196959000Z  2019-04-25T17:34:55.196959000Z            used_percent  2019-04-25T17:34:36.000000000Z              65.536737442016
```

## Function
- Manipulate and process table data and make other table
- [Pipe-forward operator](https://docs.influxdata.com/influxdb/v2.0/query-data/get-started/syntax-basics/#pipe-forward-operator)
  - |> : make different data from source data
  - `data |> someFunction() |> anotherFunction()`
  

## Query
- from : bucket
- range : time range
- window :
  - `window(every: 5m)`
  - window별로 다른 색깔로 표시됨
```shell
cpuUsageUser =
  from(bucket:"example-bucket")
    |> range(start: timeRange)
    |> filter(fn: (r) =>
      r._measurement == "cpu" and
      r._field == "usage_user" and
      r.cpu == "cpu-total"
    )

memUsagePercent =
  from(bucket:"example-bucket")
    |> range(start: timeRange)
    |> filter(fn: (r) =>
      r._measurement == "mem" and
      r._field == "used_percent"
    )
```