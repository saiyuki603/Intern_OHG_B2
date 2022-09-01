import B1
import B3
import B4
import B6

address = "千葉県千葉市稲毛区稲毛３丁目７−３０"

err = 0
"""
err = 0 : エラーなし
err = 1 : 住所が不適
"""

address_list = B6.yure(address)
if address_list == 1:
    err = 1
elif "千葉市" in address_list[0]:
    err = B1.chiba(address_list)
elif "さいたま市" in address_list[0]:
    err = B3.saitama_gesui(address_list)
    err = B4.saitama_doro(address_list)