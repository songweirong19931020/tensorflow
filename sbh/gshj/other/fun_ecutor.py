# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    fun_ecutor
   Description :
   Author :       CBH
   date：         2020/6/12 20: 11
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/12 20: 11:
-------------------------------------------------
"""
import psycopg2
import pandas as pd
from io import StringIO

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="192.168.4.205", port="5432")
cursor=conn.cursor()
mon_id = 202005
sql = '''
DELETE from his_bi.dw_inp_patient_info_m where month_id='{mon_id}';
insert into his_bi.dw_inp_patient_info_m
select 
'{mon_id}',
a.brxh,
t1.patient_id,
t1.pai_visit_id,
t1.visit_id,
a.brxm,
cast(split_part(cast(age(CURRENT_DATE,a.csrq) as text),' ',1) as numeric) as pati_age,
split_part(cast(age(CURRENT_DATE,a.csrq) as text),' ',2) as age_flag,
cast(a.xb as NUMERIC) as sex,
t1.hospital_area,
t1.team_id,  --诊疗组ID
tm.team_name,  --诊疗组名称
t1.doctor_chief as doctor_chief, --主任医生编码(部分直接存储为姓名)
us1.people_name as doctor_chief_name, --主任医生编码
t1.doctor_attending as doctor_attending, --主治医生编码(部分直接存储为姓名)
us2.people_name as doctor_attending_name, --主治医生编码
t1.admission_dept, ---入院科室编码
t6.name,
t1.discharge_dept, --- 出院科室编码
t7.name,
a.ryrq,  --入院时间
a.cyrq, ---出院时间
t8.diagdiseasecode,
t8.diagdiseasename,
a.zyts,---住院天数
md.is_zqss,  --是否择期手术
md.is_xzhz,  --是否下转患者
md.is_sshz,  --是否手术患者(0 否 1是)
md.is_ylqk_gr,  --是否I类切口感染(0 否 1是)
md.is_ylqk_sh,  --是否I类切口手术(0 否 1是)
md.is_wzhz,  --是否危重患者(0 否 1是)
md.is_wxzl,
md.is_wswsj,  --是否微生物检验样本送检
md.is_use_sykjyw,  --是否使用抗菌药物
md.is_use_fxzjkjyw,  --是否使用非限制级抗菌药物
md.is_use_xzjkjyw,  --是否使用限制级抗菌药物
md.is_use_tsjkjyw,  --是否使用特殊级抗菌药物
mq.kjyw_ddd_sum,  --抗菌药物累计DDD数
mq.fxzj_kjyw_ddd_sum,  --非限制级抗菌药物累计DDD数
mq.xzj_kjyw_ddd_sum,  --限制级抗菌药物累计DDD数
mq.tsj_kjyw_ddd_sum,  --特殊级抗菌药物DDD数使用强度
md.wc_num,
md.sjss_num,
md.qj_num,
md.hxnj_num,
md.xhnj_num,
md.rjss_num,
md.ssbf_num,
a.lyfs,
mq.is_die,
case when a.lyfs='4' then 1 else 0 end  as is_zdly,
0 as lcljglxh,
a.lcybl,
a.fsybl,
a.sqysh,
a.md5
from his_bi.ods_patient_medical_record a
inner join his_bi.pts_pai_visit t1 on (a.bah = t1.patient_id and a.zycs = t1.visit_id)
left join his_bi.bds_bds_organization t6 on (t1.admission_dept = t6.code )
left join his_bi.bds_bds_organization t7 on (t1.discharge_dept = t7.code )
left join his_bi.ods_patient_diag_info t8 on (a.bah = t8.patient_id and a.zycs = t8.visit_id and t8.main_diag='1')
left join 
(
    select
    md.pai_visit_id,
    max(case when md.key = 'D00044' then md.value end) as ssbf_num,
    max(case when md.key = 'D00045' then md.value end) as is_zqss,  --是否择期手术
    max(case when md.key = 'D00046' then md.value end) as is_xzhz,  --是否下转患者
    max(case when md.key = 'D00047' then md.value end) as is_rjss,  --是否日间手术患者
    max(case when md.key = 'D00048' then md.value end) as is_sshz,  --是否手术患者(0 否 1是)
    max(case when md.key = 'D00049' then md.value end) as is_wchz,  --是否微创手术患者(0 否 1是)
    max(case when md.key = 'D00050' then md.value end) as is_sjss,  --是否四级手术患者(0 否 1是)
    max(case when md.key = 'D00051' then md.value end) as is_ylqk_gr,  --是否I类切口感染(0 否 1是)
    max(case when md.key = 'D00052' then md.value end) as is_ylqk_sh,  --是否I类切口手术(0 否 1是)
    max(case when md.key = 'D00053' then md.value end) as is_wzhz,  --是否危重患者(0 否 1是)
    max(case when md.key = 'D00092' then md.value end) as is_wswsj,  --是否微生物检验样本送检
    max(case when md.key = 'D00088' then md.value end) as is_use_sykjyw,  --是否使用抗菌药物
    max(case when md.key = 'D00089' then md.value end) as is_use_fxzjkjyw,  --是否使用非限制级抗菌药物
    max(case when md.key = 'D00090' then md.value end) as is_use_xzjkjyw,  --是否使用限制级抗菌药物
    max(case when md.key = 'D00091' then md.value end) as is_use_tsjkjyw,  --是否使用特殊级抗菌药物
    max(case when md.key = 'D00207' then md.value end) as is_wxzl,
    sum(case when md.key = 'D00242' then md.value end) as wc_num,
    sum(case when md.key = 'D00243' then md.value end) as sjss_num,
    sum(case when md.key = 'D00244' then md.value end) as qj_num,
    sum(case when md.key = 'D00245' then md.value end) as hxnj_num,
    sum(case when md.key = 'D00246' then md.value end) as xhnj_num,
    sum(case when md.key = 'D00247' then md.value end) as rjss_num
    from his_bi.dwd_inp_medical_d md
    inner join his_bi.dim_date_info d1 on md.st_date = d1.day_id and d1.month_id ='{mon_id}'
    where md.key in ('D00044','D00045','D00046','D00047','D00048','D00049','D00050','D00052','D00053','D00092','D00088','D00089','D00090','D00091','D00207','D00242','D00243','D00244','D00245','D00246','D00247')
    group by md.pai_visit_id
)md on t1.pai_visit_id = md.pai_visit_id
left join 
(
    select
    mq.pai_visit_id,
    sum(case when mq.key = 'D00093' then mq.value end) as kjyw_ddd_sum,  --抗菌药物累计DDD数
    sum(case when mq.key = 'D00094' then mq.value end) as fxzj_kjyw_ddd_sum,  --非限制级抗菌药物累计DDD数
    sum(case when mq.key = 'D00095' then mq.value end) as xzj_kjyw_ddd_sum,  --限制级抗菌药物累计DDD数
    sum(case when mq.key = 'D00096' then mq.value end) as tsj_kjyw_ddd_sum,  --特殊级抗菌药物DDD数使用强度
    max(case when mq.key = 'D00155' then  mq.value end) as is_die
    from his_bi.dwd_inp_quantity_d mq
    inner join his_bi.dim_date_info d1 on mq.st_date = d1.day_id and d1.month_id = '{mon_id}'
    where mq.key in ('D00093','D00094','D00095','D00096','D00155')
    group by mq.pai_visit_id
)mq on t1.pai_visit_id = mq.pai_visit_id
left join his_bi.pts_pts_basic_org_medi_team tm on t1.team_id = tm.team_id
left join his_bi.uum_uum_user us1 on t1.doctor_chief = us1.user_name
left join his_bi.uum_uum_user us2 on t1.doctor_attending = us2.user_name
where 1=1
and t1.discharge_dept_date >= to_date('{mon_id}','yyyymm')
and t1.discharge_dept_date <  to_date('{mon_id}','yyyymm') + interval '1 month';  
'''.format(mon_id=mon_id)
cursor.execute(sql)
result = cursor.fetchall()
table_name ='his_bi.dw_outp_patient_amount_m'
data1 = pd.DataFrame(result)
# dataframe类型转换为IO缓冲区中的str类型
output = StringIO()
data1.to_csv(output, sep='\t', index=False, header=False)
output1 = output.getvalue()
cursor.copy_from(StringIO(output1), table_name)
conn.commit()
cursor.close()
conn.close()