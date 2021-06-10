import time
import settings as s


try:
    while True:
        s.scrape_link(s.craigs_link)
        time.sleep(10)
except KeyboardInterrupt:
    pass
