import json
import tiantian
import urllib3
from cn.tiantian.course.BaseDB import DBSession
url = 'https://www.6tiantian.com/api/student/book/menu?pageNumber=1&customConfigId=custom_config_id_1' \
      '&menuId=739485&pageSize=500&token=d06b68b467abc7319b588720bbeb540c485dd58e'

http = urllib3.PoolManager()
r = http.request('GET', url,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/89.0.4389.82 Safari/537.36',
                    'Cookie':'SERVERID=5d170c41b460c390dc176c1f25b0'
                             '8924|1616038965|1616038013'
                    }
                 )
obj_list = []
results = json.loads(r.data.decode('utf-8'))['books']
for result in results:
    book_obj = tiantian.TiantianBook(**result)
    book_obj.lessons = ''
    obj_list.append(book_obj)
session = DBSession()
session.add_all(obj_list)
session.commit()
session.close()




