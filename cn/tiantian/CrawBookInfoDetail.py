import json
import demjson
import tiantian
import urllib3
import tiantian_book_info
import tiantian_book_info_detail
import ast
from cn.tiantian.course.BaseDB import DBSession

session = DBSession()
book_info_list = session\
    .query(tiantian_book_info.TiantianBookInfo.lessons).all()
# i = 0
# j = 0
param_list = []
for book_info in book_info_list:
    book_info_obj = ast.literal_eval(book_info[0])
    for book_info_lesson in book_info_obj:
        for topic in book_info_lesson['topics']:
            param_tmp = {}
            print('bookId:', book_info_lesson['bookId'])
            print('lessonId:', book_info_lesson['id'])
            print('topicId:', topic['id'])
            param_tmp['bookId'] = book_info_lesson['bookId']
            param_tmp['lessonId'] = book_info_lesson['id']
            param_tmp['topicId'] = topic['id']
            param_list.append(param_tmp)
print(param_list.__len__())
book_info_detail_list = []
url = 'https://www.6tiantian.com/api/student/book/lesson/info?mode=2&topicId={0}&hwType=4' \
      '&customConfigId=custom_config_id_1&lessonId={1}&token=d06b68b467abc7319b588720bbeb540c4973d66a'
http = urllib3.PoolManager()
for param in param_list:
    r = http.request('GET', url.format(param['topicId'], param['lessonId']),
                     headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                       'Chrome/89.0.4389.82 Safari/537.36',
                         'Cookie': 'SERVERID=5d170c41b460c390dc176c1f25b0'
                                   '8924|1616038965|1616038013'
                     }
                     )
    result = json.loads(r.data.decode('utf-8'))['homework']
    result['topicId'] = param['topicId']
    result['lessonId'] = param['lessonId']
    result['bookId'] = param['bookId']
    result['topics'] = str(result['topics'])
    result['studentScoreCommentThresholds'] = str(result['studentScoreCommentThresholds'])
    book_obj = tiantian_book_info_detail.TiantianBookInfoDetail(**result)
    book_info_detail_list.append(book_obj)
session.add_all(book_info_detail_list)
session.commit()
session.close()
