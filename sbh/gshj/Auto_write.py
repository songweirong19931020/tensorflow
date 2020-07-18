# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Auto_write
   Description :
   Author :       CBH
   date：         2020/7/13 17: 40
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/13 17: 40:
-------------------------------------------------
"""
from sbh.gshj.util.LogUitl import *
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
key = ['JX01003',
'JX0100308',
'JX0100301',
'JX0100304'

]
kpi_code=['LV007010501',
'LV007010502',
'LV007010503',
'LV007010504'

]


tag=['每门诊人次费用（元）',
'每门诊人次药费（元）',
'每住院费用（元）',
'每住院药费（元）'

]



for i in range(len(kpi_code)):
    sql = '''
    ---{tag}
    delete from his_bi.level_master_m where month_id = '202001' and level_code = '{kpi_code}';
    insert into his_bi.level_master_m
    select
    t1.month_id as month_id,
    '{kpi_code}' as level_code ,
    t1.kpi_value  as level_value,
    now() as update_time ,
    t1.kpi_value   as self_value  ,
    null as check_flag  ,
    null as check_comm
    from his_bi.kpi_master_m t1
    where
    t1.month_id=c_monthlist.month_id
    and t1.kpi_code='{key}';
    '''.format(kpi_code = kpi_code[i],key = key[i],tag = tag[i])
    print(sql)
    log.info(sql)