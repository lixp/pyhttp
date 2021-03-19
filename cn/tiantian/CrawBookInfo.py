import json
import tiantian
import urllib3
from cn.tiantian.course.BaseDB import DBSession
import tiantian_book_info

url = 'https://www.6tiantian.com/api/student/book/info?customConfigId=custom_config_id_1' \
      '&token=d06b68b467abc7319b588720bbeb540c4973d66a&hasTopic=true&bookId='
session = DBSession()
book_id_list = session.query(tiantian.TiantianBook.id)
book_info_list = []
for book_id in book_id_list:
    print(book_id.id)

    http = urllib3.PoolManager()
    r = http.request('GET', url + str(book_id.id),
                     headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                       'Chrome/89.0.4389.82 Safari/537.36',
                         'Cookie': 'SERVERID=5d170c41b460c390dc176c1f25b0'
                                   '8924|1616038965|1616038013'
                     }
                     )
    result = json.loads(r.data.decode('utf-8'))['book']
    result['lessons'] = str(result['lessons'])
    result['lessonGroups'] = str(result['lessonGroups'])
    result['tags'] = str(result['tags'])
    book_obj = tiantian_book_info.TiantianBookInfo(**result)
    book_info_list.append(book_obj)
session.add_all(book_info_list)
session.commit()
session.close()
