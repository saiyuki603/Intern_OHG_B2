import B1
import B2
import B3
import B4
import B6
import trigger

import time
import pickle
import base64
import json
import logging
import re

#from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # arguments = docopt(__doc__, version="0.1")
    query = "is:read"  # arguments["<query>"]
    tag = "map"  # arguments["<tag>"]
    count = 1  # arguments["<count>"]
    logging.basicConfig(level=logging.INFO)

    messages_ = trigger.main(query=query, tag=tag, count=count)
    print(messages_)

    if messages_ == None:
        time.sleep(5)
    else:
        re_body_1 = r'"body": ".*, "subject"'
        address = re.search(re_body_1, messages_).group()
        address = address[9:-16]
        print(address)
        re_body_2 = r'<.*@.*>'
        from_mail = re.search(re_body_2, messages_).group()
        from_mail = from_mail[1:-1]
        print(from_mail)

err = 0
"""
err = 0 : エラーなし
err = 1 : 住所が不適
err = 2 : 千葉道路の画像なし
err = 3 : 千葉下水の画像なし
err = 4 : 入力内容が不正
"""

address_list = B6.yure(address)
if address_list == 1:
    err = 1
elif "千葉市" in address_list[0]:
    err, a = B1.chiba_gesui(address_list)
    err = B2.chiba_doro(address_list, a, err)
elif "さいたま市" in address_list[0]:
    if __name__ == '__main__':
        process_list = []

        process1 = Process(target=B3.saitama_gesui,args=(address_list,))
        process1.start()
        process_list.append(process1)

        process2 = Process(target=B4.saitama_doro,args=(address_list,))
        process2.start()
        process_list.append(process2)

        for process in process_list:
            process.join()