import graphitesend
import time
def send_metric(key: str, val: int):
    g = graphitesend.init(graphite_server='1.1.1.1', graphite_port=2003, prefix='app.prod.service_name')
    g.send(key, val)

start = time.time()
# do something
send_metric("elapsed_sec", int(time.time() - start))