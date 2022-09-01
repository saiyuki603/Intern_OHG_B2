import re
import mojimoji

def yure(address):

    address_han = mojimoji.zen_to_han(address.replace('〇', '0').replace('一', '1').replace('二', '2').replace('三', '3').replace('四', '4').replace('五', '5').replace('六', '6').replace('七', '7').replace('八', '8').replace('九', '9'))

    re_kenshi = r'.*?市'
    re_ku = r'市.*?区'
    re_machi = r'区.*?\d'
    re_numbers = r'\D\d+'

    ken = re.search(re_kenshi, address_han).group()
    ku = re.search(re_ku, address_han).group()
    ku = ku[1:]
    machi = re.search(re_machi, address_han).group()
    machi = machi[1:-1]
    numbers = re.findall(re_numbers, address_han)

    address_list = []

    address_list.append(ken)
    address_list.append(ku)
    address_list.append(machi)

    for i in numbers:
        address_list.append(mojimoji.han_to_zen(i[1:]))

    return(address_list)
