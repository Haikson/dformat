# -*- coding:utf-8 -*-
from dformat import dformat
from datetime import datetime


datetime_formates = [
    '2016/08/25',
    '26/08/2016',
    '27.08.2016',
    '2016-08-28 11:20:11',
    '20160829T112022',
    '2016/08/30 11:20:50',
    '22/08/2016 11:20:33',
    '21.08.2016 11:20:25',
    '20160820',
    '2016-08-20',
    '2016-08-11T11:20:58',
    '2016-08-85T11:20',
]


for datetime_format in datetime_formates:
    try:
        dt = dformat(datetime_format)  # .strftime('%d.%m.%Y %H:%M:%S')
    except:
        df = dformat(datetime_format)  # .strftime('%d.%m.%Y')
        
    assert isinstance(dt, datetime)
    #print(dformat(datetime_format))
