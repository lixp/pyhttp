# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import urllib3
import json
from urllib.parse import parse_qsl
import csv


def print_hi():
    query_string = 'sort=CreateTime&desc=1&SubItem=1&Others=1&onlyLastDate=1&FriendlyDate=1' \
                   '&TotalCount=201987&PageCount=20199'

    params = parse_qsl(query_string)
    params = dict(params)
    url = 'https://ubest.xiaogj.com/api/Customer/Query'
    http = urllib3.PoolManager()

    count = 0
    with open('data_file.csv', 'w', newline='', encoding='utf-8-sig') as data_file:
        for index in range(1, 20200):
            params['PageIndex'] = index
            r = http.request(
                'POST',
                'https://ubest.xiaogj.com/api/Customer/Query',
                headers={
                    'Cookie': 'chargeVersion=2; _ga=GA1.2.1785795811.1607683724; %E5%88%98%E9%BB%8E%40hjyjGetNewChargeGuide=true; 201706201422studentManage%23studentManage_table%23studentManage_selectColum=%5B%5D; lastloginname=admin%40hjyj; _gid=GA1.2.1213429744.1612841139; 201706201422customerManage%23customerManage_table%23customerManage_selectColum=%5B%5D; admin%40hjyjGetNewChargeGuide=true; ASP.NET_SessionId=fydawplcrle4ng2qrpsjdsrp; acw_tc=ac11000116129568062567614e00caa95d1025cf72de0c7563215b3250fa69; .ASPXAUTH=4557E1A7633C3B043289D7EE06D00CD6C8444FC4BFBEC79CD0667B24C83F670547CE09DD9D6937D6512BB6AA7F0066FB2D3078ED1D833EED277D3F55EDAB9AC1464A90CFE955C5D3DCD6F1BD9E32D754DD09D48C3DA6C0C0CF896A8FD99893380795A12504ABECFE48C4C17C1883F24696F06C36CC4CACB8017BDE83FA957173ED5976884AF16709A144E4B525DAE262; _gat_gtag_UA_167872829_1=1',
                },
                fields=params
            )
            result = json.loads(r.data.decode('utf-8'))
            csv_writer = csv.writer(data_file)
            for client in result['Data']:
                if count == 0:
                    headers = client.keys()
                    csv_writer.writerow(headers)
                    count += 1
                csv_writer.writerow(client.values())
            print('完成了第', index, '页')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
