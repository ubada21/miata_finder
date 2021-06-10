import time
import settings as s


try:
    while True:
        s.scrape_link(s.craigs_link)
        time.sleep(600) # time between scrapes in seconds.
except KeyboardInterrupt:
    pass
