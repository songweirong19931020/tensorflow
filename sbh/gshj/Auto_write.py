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
lv_code = ['D00183',
'D00113',
'D00208',
'D00128',
'D00173',
'D00224',
'D00210',
'D00225',



]
sp_code=['SP002080104',
'SP002080304',
'SP002080404',
'SP002080704',
'SP002080204',
'SP002080504',
'SP002080604',
'SP002080804',




]

lv_code1=['SP002070101',
'SP002070201',
'SP002070301',
'SP002070401',
'SP002070501',
'SP002070601',
'SP002070701',
'SP002070801',
'SP002070901',
'SP002071001',
'SP002071101',
'SP002071201',
'SP002071301',
'SP002071401',
'SP002071501',
'SP002071601',
'SP002071701',
'SP002071801',
'SP002071901',
'SP002072001',
]
tag=['剖宫产出院患者术前平均住院日',
'异位妊娠出院患者术前平均住院日',
'宫颈癌出院患者术前平均住院日',
'新生儿呼吸窘迫综合征（NRDS）出院患者术前平均住院日',
'社区获得性肺炎(住院、儿童)出院患者术前平均住院日',
'子宫肌瘤出院患者术前平均住院日',
'艾滋病、梅毒和乙肝母婴传播疾病出院患者术前平均住院日',
'儿童哮喘出院患者术前平均住院日',






]


for i in range(len(sp_code)):
        sql_level = '''
        ---{tag}
delete from his_bi.special_master_m where month_id = c_monthlist.month_id and special_code = '{sp_code}';
insert into his_bi.special_master_m
select
    c_monthlist.month_id,
    '{sp_code}' as special_code ,
    coalesce(sum(t2.sub_days)/max(t3.value),0) as special_value,
    now() as update_time ,
    coalesce(sum(t2.sub_days)/max(t3.value),0) as self_value,
    null as check_flag  ,
    null as check_comm
from
    his_bi.DWD_INP_MEDICAL_D t1
        inner join his_bi.v_cpoe_operate_first t2 on t1.patient_id = t2.bah and t1.visit_id
        = t2.zycs and t1.key='{lv_code}' left join
    (
        select
            left(st_date,6) as month_id,
            count(1) as value
        from his_bi.DWD_INP_MEDICAL_D
        where
                key='{lv_code}'
        GROUP BY left(st_date,6)
    )t3 on left(t1.st_date,6) = t3.month_id
    where
left(t1.st_date,6) = c_monthlist.month_id;
        '''.format(sp_code=sp_code[i], lv_code = lv_code[i],tag = tag[i],lv_code1=lv_code1[i])
        print(sql_level)
#     sql_level = '''
#     ---{tag}
# delete from his_bi.special_master_m where month_id = c_monthlist.month_id and special_code = '{sp_code}';
# insert into his_bi.special_master_m
# select
# c_monthlist.month_id as month_id,
# '{sp_code}' as special_code ,
# case when coalesce(t1.level_value,0)=0 then 0 else t1.level_value end as special_value,
# now() as update_time ,
# case when coalesce(t1.level_value,0)=0 then 0 else t1.level_value end  as self_value  ,
# null as check_flag  ,
# null as check_comm
# from his_bi.level_master_m t1
# where
# t1.month_id=c_monthlist.month_id
# and t1.level_code='{lv_code}';
#     '''.format(sp_code=sp_code[i], lv_code = lv_code[i],tag = tag[i])
#     print(sql_level)
#     sql_jx = '''
#         ---{tag}
#     delete from his_bi.special_master_m where month_id = c_monthlist.month_id and special_code = '{sp_code}';
#     insert into his_bi.special_master_m
#     select
#     c_monthlist.month_id as month_id,
#     '{sp_code}' as special_code ,
#     case when coalesce(t1.kpi_value,0)=0 then 0 else t1.kpi_value end as kpi_value,
#     now() as update_time ,
#     case when coalesce(t1.kpi_value,0)=0 then 0 else t1.kpi_value end  as self_value  ,
#     null as check_flag  ,
#     null as check_comm
#     from his_bi.kpi_master_m t1
#     where
#     t1.month_id=c_monthlist.month_id
#     and t1.kpi_code='{lv_code}';
#         '''.format(sp_code=sp_code[i], lv_code = lv_code[i],tag = tag[i])
#     print(sql_jx)
#     with open('sql.txt','a+',encoding='utf-8') as f:
#         f.write(sql_level)
#         f.close()

