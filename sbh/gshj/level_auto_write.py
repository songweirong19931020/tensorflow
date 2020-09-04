# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    level_auto_write
   Description :
   Author :       CBH
   date：         2020/7/24 17: 50
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/24 17: 50:
-------------------------------------------------
"""

class AutoWrite:
    def __init__(self,value_code,target_code,tag_code):
        self.value_code=value_code,
        self.target_code = target_code,
        self.tag_code = tag_code

    def writeRunLv(self,value_code,target_code,tag_code):
        for i in range(len(target_code)):
            sql = '''
    ---{tag}
delete from his_bi.special_master_m where month_id = c_monthlist.month_id and special_code = '{sp_code}';
insert into his_bi.special_master_m
select
c_monthlist.month_id as month_id,
'{sp_code}' as special_code ,
case when coalesce(t1.level_value,0)=0 then 0 else t1.level_value end as special_value,
now() as update_time ,
case when coalesce(t1.level_value,0)=0 then 0 else t1.level_value end  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.level_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.level_code='{lv_code}';
        '''.format(sp_code=target_code[i], lv_code = value_code[i],tag = tag_code[i])
            print(sql)

    def writeRunJx(self,value_code,target_code,tag_code):
        for i in range(len(target_code)):
            sql = '''
        ---{tag}
    delete from his_bi.special_master_m where month_id = c_monthlist.month_id and special_code = '{sp_code}';
    insert into his_bi.special_master_m
    select
    c_monthlist.month_id as month_id,
    '{sp_code}' as special_code ,
    case when coalesce(t1.kpi_value,0)=0 then 0 else t1.kpi_value end as special_value,
    now() as update_time ,
    case when coalesce(t1.kpi_value,0)=0 then 0 else t1.kpi_value end  as special_value  ,
    null as check_flag  ,
    null as check_comm
    from his_bi.kpi_master_m t1
    where
    t1.month_id=c_monthlist.month_id
    and t1.kpi_code='{lv_code}';
        '''.format(sp_code=target_code[i], lv_code = value_code[i],tag = tag_code[i])
            print(sql)




if __name__ == '__main__':
    value_code=['JX037',
'JX038',
'JX039',
'JX040',
'JX041',

]
    target_code=['SP006080101',
'SP006080102',
'SP006080103',
'SP006080104',
'SP006080105',

]
    tag_code=['医疗收入增幅',
'门诊次均费用增幅',
'门诊次均药品费用增幅',
'住院次均费用增幅',
'住院次均药品费用增幅',

]
    txt = AutoWrite(value_code,target_code,tag_code)
    txt.writeRunJx(value_code,target_code,tag_code)