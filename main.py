import B1
import B3
import B4
import B6

address = "埼玉県さいたま市浦和区常盤６丁目４−４"

address_list = B6.yure(address)
if "千葉市" in address_list[0]:
    B1.chiba(address_list)
elif "さいたま市" in address_list[0] or "埼玉" in address_list[0]:
    B3.saitama_gesui(address_list)
    B4.saitama_doro(address_list)