# -*- coding: utf-8 -*-

import threading
import time
from manager import create_app
from crawler_manager import crawler_manager

port = 5000

if __name__ == '__main__':
    manager = create_app()
    manager_thread = threading.Thread(target=manager.run, kwargs=dict(port=port))
    crawler_thread = threading.Thread(target=crawler_manager, args=(port,))
    manager_thread.start()
    time.sleep(10)
    crawler_thread.start()
    manager_thread.join()
    crawler_thread.join()
