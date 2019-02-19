# -*- coding: utf-8 -*-

import threading
import time
from crawler_manager import crawler_manager

port = 8000

if __name__ == '__main__':
    crawler_thread = threading.Thread(target=crawler_manager, args=(port,))
    time.sleep(10)
    crawler_thread.start()
    crawler_thread.join()
