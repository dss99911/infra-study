# Write Data

## No code solution
### Scraper
- 특정 url의 /metrics에서 데이터를 가져오는 듯.
- 보통은 서비스 어플리케이션에서, 데이터를 전송하지만, scrapper는 직접 긁어 오는 방식.
- [prometheus format](https://prometheus.io/docs/instrumenting/exposition_formats/ )이어야 함
- [node_exporter](https://github.com/prometheus/node_exporter)등이 scraping해 갈 수 있게, metric을 보여주고, scraper가 scrap함.
    - 여러 collector가 exporter에 설정되어 있어서, metrics에 여러 데이터가 추가됨.
    - default외의 collector들은 직접 설정해줘야함.
- 그 외 exporter 들(prometheus format이므로, prometheus에 정리되어 있음)
    - https://prometheus.io/docs/instrumenting/clientlibs/
    - https://prometheus.io/docs/instrumenting/exporters/