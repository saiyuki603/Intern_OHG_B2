import B1
import B3
import B4
import B6

#from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process

address = "埼玉県さいたま市大宮区大門町２ー1-１"

err = 0
"""
err = 0 : エラーなし
err = 1 : 住所が不適
err = 2 : 千葉道路の画像なし
err = 3 : 千葉下水の画像なし
"""

address_list = B6.yure(address)
if address_list == 1:
    err = 1
elif "千葉市" in address_list[0]:
    err = B1.chiba(address_list)
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