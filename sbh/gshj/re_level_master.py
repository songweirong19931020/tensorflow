# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    re_level_master
   Description :
   Author :       CBH
   date：         2020/7/17 17: 05
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/17 17: 05:
-------------------------------------------------
"""
import re
import pandas as pd

df = pd.read_table(r'C:\Users\CBH\Desktop\work_job\BI\sql.txt')
df = pd.DataFrame(df)
pattern = re.compile('(.*) as level_value',re.IGNORECASE)

df.columns=['name']
replace_after = []
for i in df['name']:
    pattern = re.compile('round(.*) as level_value', re.IGNORECASE)
    # print(re.findall(pattern, i))
    if bool(re.findall(pattern, i)) == True:
        print(re.findall(pattern, i))
        replace_after.append(str(re.findall(pattern, i)).replace('[','').replace(']','').replace("'",''))
    else:
        print('空值')
df1 = pd.DataFrame(replace_after)
df1.to_csv('result.csv')

for i in df['name']:
    pattern = re.compile('(.*) as level_value', re.IGNORECASE)
    # print(re.findall(pattern, i))
    if bool(re.findall(pattern, i)) == True:
        print(re.findall(pattern, i))
        replace_after.append(str(re.findall(pattern, i)).replace('[','').replace(']','').replace("'",''))
    else:
        print('空值')





replace_now=[]
for g in df1[0]:
    print('COALESCE('+g+',0)')
    replace_now.append('COALESCE('+g+',0)')

df3 = pd.read_table(r'C:\Users\CBH\Desktop\work_job\BI\text.xls')
df4 = pd.DataFrame(df3)
df3 = str(df3)
for i in range(len(replace_now)):
    print(re.sub(str(replace_after[i]).replace('[','').replace(']',''), replace_now[i], df3))


def replaceStr(file,ord,new):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        # print(str)
        str1 = re.sub(ord, new, str)
        with open(file,'w', encoding='utf-8') as f:
            f.write(str1)

for i in range(len(replace_now)):
    replaceStr(r'C:\Users\CBH\Desktop\work_job\BI\level_kpi_master_m - 副本.sql','(.*) as level_value', replace_now[i]+' as level_value')


for res in range(len(replace_now)):
    print(df['name'].replace(replace_after[res],replace_now[res],regex=True,inplace=True))
    df['name']= df['name'].replace(replace_after[res],replace_now[res],inplace=True)

df_re = pd.read_csv(r'C:\Users\CBH\PycharmProjects\tensorflow\aasdsd.csv')

for gg in range(len(df_re['name'])):
    df_re['name']=df_re['name'].replace(replace_after[gg], replace_now[gg], inplace=True)


def replaceStr(file,ord,new):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        print(str)
        str1 = re.sub(ord, new, str)
        with open(file,'w', encoding='utf-8') as f:
            f.write(str1)

txt = '''

---LV007010201年门诊人次
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010201';
insert into his_bi.level_master_m
select
t1.month_id,
'LV007010201' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_outp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id and
coalesce(t1.is_tj,0)=0
group by month_id;

---急诊人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010202';
insert into his_bi.level_master_m
select
t1.month_id,
'LV007010202' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_outp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id and
coalesce(t1.is_emergency,0)<>0
group by month_id;


----年住院患者入院人次
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010204';
insert into his_bi.level_master_m
select
replace(left(stat_date::text,7),'-','') as month_id,
'LV007010204' as level_code ,
sum(c_num) as level_value,
now() as update_time ,
sum(c_num) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_dept_work_d t1
where
replace(left(stat_date::text,7),'-','')=c_monthlist.month_id
group by replace(left(stat_date::text,7),'-','');



----年出院人次
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010205';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010205' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
group by t1.month_id;


----年出院患者实际占用总床日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010206';
insert into his_bi.level_master_m
select
replace(left(stat_date::text,7),'-','') as month_id,
'LV007010206' as level_code ,
sum(bed_used) as level_value,
now() as update_time ,
sum(bed_used) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_dept_work_d t1
where
replace(left(stat_date::text,7),'-','')=c_monthlist.month_id
group by replace(left(stat_date::text,7),'-','');


----年住院手术例数（手术患者人数）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010207';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010207' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
and t1.is_sshz = '1'
group by t1.month_id;


----年门诊手术例数（手术患者人数）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010208';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010208' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_outp_patient_amount_m t1
where
t1.month_id=c_monthlist.month_id
and t1.operation_fees >0
group by t1.month_id;

----年分娩产妇数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010210';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV007010210' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.DWD_INP_QUANTITY_D t1
where
left(t1.st_date,6)=c_monthlist.month_id
and t1.key = 'D00159'
group by left(t1.st_date,6);


----年活产数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010211';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV007010211' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_quantity_d t1
where
left(t1.st_date,6)=c_monthlist.month_id
and t1.key = 'D00157'
and t1.value not in ('2','3')
group by left(t1.st_date,6);


---恶性肿瘤手术术前诊断与术后病理诊断符合例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010302';
insert into his_bi.level_master_m
select
replace(left(t2.cyrq::text,7),'-','')  as month_id,
'LV007010302' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from
(select
distinct
patient_id,
visit_id
from
his_bi.dwd_inp_medical_d
where
key = 'D00191')t1 inner join his_bi.ods_patient_medical_record t2 on t1.patient_id = t2.bah and  t1.visit_id = t2.zycs
where
replace(left(t2.cyrq::text,7),'-','')=c_monthlist.month_id
and t2.sqysh = '1'
group by replace(left(t2.cyrq::text,7),'-','') ;


---住院患者死亡人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010303';
insert into his_bi.level_master_m
select
t1.month_id,
'LV007010303' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
and t1.lyfs='5'
group by t1.month_id ;

---住院患者自动出院例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010304';
insert into his_bi.level_master_m
select
t1.month_id,
'LV007010304' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
and t1.lyfs<>'4'
group by t1.month_id ;

---住院手术患者手术人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010305';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010305' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
and t1.is_sshz = '1'
group by t1.month_id;



----住院手术患者手术人次数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010306';
insert into his_bi.level_master_m
select
to_char(t1.cyrq,'yyyymm') as month_id,
'LV007010306' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.ods_patient_medical_record t1
inner join his_bi.ods_patient_opertion_info t2 on t1.brxh = t2.brxh
where
to_char(t1.cyrq,'yyyymm') =c_monthlist.month_id
group by to_char(t1.cyrq,'yyyymm') ;

---住院手术患者死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010307';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010307' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
and t1.is_sshz = '1'
and t1.lyfs='5'
group by t1.month_id;



---住院危重患者抢救人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010308';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010308' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
inner join his_bi.ods_patient_medical_record t2 on t1.patient_id = t2.bah and t1.visit_id = t2.zycs
where
t1.month_id=c_monthlist.month_id
and t1.is_wzhz = '1'
and t2.qjcs<>'0'
group by t1.month_id;


---住院危重患者抢救人次数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010309';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010309' as level_code ,
t2.qjcs as level_value,
now() as update_time ,
t2.qjcs as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
inner join his_bi.ods_patient_medical_record t2 on t1.patient_id = t2.bah and t1.visit_id = t2.zycs
where
t1.month_id=c_monthlist.month_id
and t1.is_wzhz = '1'
and t2.qjcs<>'0';


---住院危重患者死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010310';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010310' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
and t1.is_wzhz = '1'
and t1.lyfs='5'
group by t1.month_id;


---新生儿患者住院死亡率
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010311';
insert into his_bi.level_master_m
select
left(t1.st_date,6),
'LV007010311' as level_code ,
cast((count(case when t1.value = '2' or t1.value = '3' then 1 end)*1.00/count(1)) as decimal(10,5))*100 as level_value,
now() as update_time ,
cast((count(case when t1.value = '2' or t1.value = '3' then 1 end)*1.00/count(1)) as decimal(10,5))*100  as self_value  ,
null as check_flag  ,
null as check_comm
from
his_bi.dwd_inp_quantity_d t1
where
t1.key = 'D00157'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);


----孕产妇危重抢救例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010312';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV007010312' as level_code ,
sum(t2.qjcs) as level_value,
now() as update_time ,
sum(t2.qjcs) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.DWD_INP_QUANTITY_D t1
inner join his_bi.ods_patient_medical_record t2 on t1.patient_id = t2.bah and t1.visit_id = t2.zycs
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00159'
and coalesce(t2.qjcs,0)<>0
group by left(t1.st_date,6);


----孕产妇危重死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010313';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV007010313' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.DWD_INP_QUANTITY_D t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00159'
and t2.is_wzhz = '1'
and coalesce(t2.lyfs::text,'0')='5'
group by left(t1.st_date,6);




---出院患者平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010401';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010401' as level_code ,
sum(t1.in_days)/count(1) as level_value,
now() as update_time ,
sum(t1.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
group by t1.month_id;


---床位使用率
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010403';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010403' as level_code ,
t1.kpi_value as level_value,
now() as update_time ,
t1.kpi_value as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.kpi_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.kpi_code='JX080';


---产后出血
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010101';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702010101' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00105'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---妊娠合并糖尿病
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010201';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702010201' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00114'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---盆腔炎性疾病
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010301';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702010301' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00116'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---异位妊娠
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010401';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702010401' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00113'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---女性生殖器脱垂
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010501';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702010501' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00117'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---重度卵巢过度刺激综合征
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010801';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702010801' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00121'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---重度子痫前期
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010901';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702010901' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00111'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---早产
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011001';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011001' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00106'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---多胎妊娠
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011101';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011101' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00107'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---胎膜早破
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011201';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011201' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00108'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---前置胎盘
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011301';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011301' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00109'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---胎盘早剥
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011401';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011401' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00110'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---新生儿窒息
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011501';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011501' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00127'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---新生儿呼吸窘迫
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011601';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011601' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00128'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---支气管肺炎
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011701';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011701' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00123'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---小儿腹泻病
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011801';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011801' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00124'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---低出生体重儿
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011901';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV00702011901' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00125'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);

---新生儿高胆红素血症
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007020120';
insert into his_bi.level_master_m
select
left(st_date,6) as month_id,
'LV007020120' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d
where
key = 'D00126'
and left(st_date,6) = c_monthlist.month_id
group by left(st_date,6);




---产后出血死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010102';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010102' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00105'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---妊娠合并糖尿病死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010202';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010202' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00114'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---盆腔炎性疾病死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010302';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010302' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00116'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---异位妊娠死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010402';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010402' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00113'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---女性生殖器脱垂死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010502';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010502' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00117'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---重度卵巢过度刺激综合征死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010802';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010802' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00121'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---重度子痫前期死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010902';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010902' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00111'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---早产死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011002';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011002' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00106'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---多胎妊娠死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011102';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011102' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00107'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---胎膜早破死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011202';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011202' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00108'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---前置胎盘死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011302';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011302' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00109'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---胎盘早剥死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011402';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011402' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00110'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---新生儿窒息死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011502';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011502' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00127'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---新生儿呼吸窘迫死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011602';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011602' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00128'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---支气管肺炎死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011702';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011702' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00123'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---小儿腹泻病死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011802';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011802' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00124'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---低出生体重儿死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011902';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011902' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00125'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---新生儿高胆红素血症死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702012022';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702012022' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00126'
and left(t1.st_date,6) = c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);



---产后出血平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010103';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010103' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00105'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---妊娠合并糖尿病平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010203';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010203' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00114'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---盆腔炎性疾病平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010303';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010303' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00116'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---异位妊娠平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010403';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010403' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00113'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---女性生殖器脱垂平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010503';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010503' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00117'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度卵巢过度刺激综合征平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010803';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010803' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00121'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度子痫前期平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010903';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010903' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00111'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---早产平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011003';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011003' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00106'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---多胎妊娠平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011103';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011103' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00107'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎膜早破平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011203';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011203' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00108'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---前置胎盘平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011303';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011303' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00109'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎盘早剥平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011403';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011403' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00110'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿窒息平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011503';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011503' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00127'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿呼吸窘迫平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011603';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011603' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00128'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---支气管肺炎平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011703';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011703' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00123'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---小儿腹泻病平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011803';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011803' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00124'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---低出生体重儿平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011903';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011903' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00125'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿高胆红素血症平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702012023';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702012023' as level_code ,
sum(t2.in_days)/count(1) as level_value,
now() as update_time ,
sum(t2.in_days)/count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00126'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);




---产后出血平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010104';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010104' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00105'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---妊娠合并糖尿病平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010204';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010204' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00114'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---盆腔炎性疾病平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010304';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010304' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00116'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---异位妊娠平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010404';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010404' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00113'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---女性生殖器脱垂平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010504';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010504' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00117'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度卵巢过度刺激综合征平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010804';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010804' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00121'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度子痫前期平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010904';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010904' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00111'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---早产平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011004';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011004' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00106'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---多胎妊娠平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011104';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011104' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00107'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎膜早破平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011204';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011204' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00108'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---前置胎盘平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011304';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011304' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00109'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎盘早剥平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011404';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011404' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00110'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿窒息平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011504';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011504' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00127'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿呼吸窘迫平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011604';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011604' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00128'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---支气管肺炎平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011704';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011704' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00123'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---小儿腹泻病平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011804';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011804' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00124'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---低出生体重儿平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011904';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011904' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00125'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿高胆红素血症平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702012024';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702012024' as level_code ,
round(sum(t2.total_fees)/count(1),4) as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(1),4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.patient_id = t2.patient_id and t1.visit_id = t2.visit_id
where
key = 'D00126'
and left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);


---产后出血15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010106';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010106' as level_code ,
round(coalesce(sum(case when t1.key = 'D00105' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00105' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---妊娠合并糖尿病15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010206';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010206' as level_code ,
round(coalesce(sum(case when t1.key = 'D00114' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00114' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---盆腔炎性疾病15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010306';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010306' as level_code ,
round(coalesce(sum(case when t1.key = 'D00116' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00116' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---异位妊娠15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010406';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010406' as level_code ,
round(coalesce(sum(case when t1.key = 'D00113' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00113' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---女性生殖器脱垂15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010506';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010506' as level_code ,
round(coalesce(sum(case when t1.key = 'D00117' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00117' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度卵巢过度刺激综合征15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010806';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010806' as level_code ,
round(coalesce(sum(case when t1.key = 'D00121' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00121' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度子痫前期15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010906';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010906' as level_code ,
round(coalesce(sum(case when t1.key = 'D00111' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00111' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---早产15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011006';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011006' as level_code ,
round(coalesce(sum(case when t1.key = 'D00106' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00106' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---多胎妊娠15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011106';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011106' as level_code ,
round(coalesce(sum(case when t1.key = 'D00107' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00107' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎膜早破15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011206';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011206' as level_code ,
round(coalesce(sum(case when t1.key = 'D00108' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00108' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---前置胎盘15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011306';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011306' as level_code ,
round(coalesce(sum(case when t1.key = 'D00109' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00109' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎盘早剥15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011406';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011406' as level_code ,
round(coalesce(sum(case when t1.key = 'D00110' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00110' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿窒息15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011506';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011506' as level_code ,
round(coalesce(sum(case when t1.key = 'D00127' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00127' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿呼吸窘迫15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011606';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011606' as level_code ,
round(coalesce(sum(case when t1.key = 'D00128' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00128' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---支气管肺炎15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011706';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011706' as level_code ,
round(coalesce(sum(case when t1.key = 'D00123' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00123' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---小儿腹泻病15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011806';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011806' as level_code ,
round(coalesce(sum(case when t1.key = 'D00124' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00124' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---低出生体重儿15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011906';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011906' as level_code ,
round(coalesce(sum(case when t1.key = 'D00125' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00125' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿高胆红素血症15天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702012026';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702012026' as level_code ,
round(coalesce(sum(case when t1.key = 'D00126' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00126' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00215'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);




---产后出血31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010107';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010107' as level_code ,
round(coalesce(sum(case when t1.key = 'D00105' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00105' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---妊娠合并糖尿病31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010207';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010207' as level_code ,
round(coalesce(sum(case when t1.key = 'D00114' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00114' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---盆腔炎性疾病31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010307';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010307' as level_code ,
round(coalesce(sum(case when t1.key = 'D00116' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00116' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---异位妊娠31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010407';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010407' as level_code ,
round(coalesce(sum(case when t1.key = 'D00113' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00113' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---女性生殖器脱垂31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010507';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010507' as level_code ,
round(coalesce(sum(case when t1.key = 'D00117' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00117' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度卵巢过度刺激综合征31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010807';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010807' as level_code ,
round(coalesce(sum(case when t1.key = 'D00121' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00121' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---重度子痫前期31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702010907';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702010907' as level_code ,
round(coalesce(sum(case when t1.key = 'D00111' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00111' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---早产31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011007';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011007' as level_code ,
round(coalesce(sum(case when t1.key = 'D00106' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00106' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---多胎妊娠31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011107';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011107' as level_code ,
round(coalesce(sum(case when t1.key = 'D00107' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00107' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎膜早破31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011207';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011207' as level_code ,
round(coalesce(sum(case when t1.key = 'D00108' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00108' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---前置胎盘31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011307';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011307' as level_code ,
round(coalesce(sum(case when t1.key = 'D00109' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00109' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---胎盘早剥31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011407';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011407' as level_code ,
round(coalesce(sum(case when t1.key = 'D00110' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00110' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿窒息31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011507';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011507' as level_code ,
round(coalesce(sum(case when t1.key = 'D00127' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00127' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿呼吸窘迫31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011607';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011607' as level_code ,
round(coalesce(sum(case when t1.key = 'D00128' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00128' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---支气管肺炎31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011707';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011707' as level_code ,
round(coalesce(sum(case when t1.key = 'D00123' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00123' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---小儿腹泻病31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011807';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011807' as level_code ,
round(coalesce(sum(case when t1.key = 'D00124' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00124' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---低出生体重儿31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702011907';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702011907' as level_code ,
round(coalesce(sum(case when t1.key = 'D00125' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00125' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---新生儿高胆红素血症31天再住院率（包括计划内及非计划重返）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702012027';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702012027' as level_code ,
round(coalesce(sum(case when t1.key = 'D00126' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as level_value,
now() as update_time ,
round(coalesce(sum(case when t1.key = 'D00126' then 1 end)*1.00/ count(t2.pai_visit_id),0)*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key = 'D00216'
where
left(t1.st_date,6) = c_monthlist.month_id
group by left(t1.st_date,6);

---平均每张床位工作日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010402';
insert into his_bi.level_master_m
select
replace(left(stat_date::text,7),'-','') as month_id,
'LV007010402' as level_code,
sum(bed_used_ending)/(sum(t1.sy_num)/(DATE_PART('days', DATE_TRUNC('month',t1.stat_date)+ '1 MONTH'::INTERVAL
    - '1 DAY'::INTERVAL))) as level_value,
now() as update_time ,
sum(bed_used_ending)/(sum(t1.sy_num)/(DATE_PART('days', DATE_TRUNC('month',t1.stat_date)+ '1 MONTH'::INTERVAL
    - '1 DAY'::INTERVAL)))  as self_value,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_dept_work_d t1
where
replace(left(stat_date::text,7),'-','')  = c_monthlist.month_id
group by (DATE_PART('days', DATE_TRUNC('month',t1.stat_date)+ '1 MONTH'::INTERVAL
    - '1 DAY'::INTERVAL)),replace(left(stat_date::text,7),'-','');

---子宫切除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020101';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020101' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00182'
group by left(t1.st_date,6);

---宫腔镜下宫腔粘连切除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020201';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020201' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00193'
group by left(t1.st_date,6);

---盆底重建术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020301';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020301' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00194'
group by left(t1.st_date,6);

---剖宫产总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020401';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020401' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00183'
group by left(t1.st_date,6);

---产钳助产术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020501';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020501' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00196'
group by left(t1.st_date,6);

---子宫颈根治性切除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020601';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020601' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00197'
group by left(t1.st_date,6);

---腹腔镜下子宫次全切除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020701';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020701' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00198'
group by left(t1.st_date,6);

---腹腔镜下子宫全切除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020801';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020801' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00199'
group by left(t1.st_date,6);

---腹腔镜下子宫肌瘤切除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020901';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020901' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00200'
group by left(t1.st_date,6);

---宫腔镜电切术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021001';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021001' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00201'
group by left(t1.st_date,6);

---阴式子宫肌瘤切除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021101';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021101' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00202'
group by left(t1.st_date,6);

---广泛全子宫清除术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021201';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021201' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00203'
group by left(t1.st_date,6);

---乳腺癌根治术总例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021301';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021301' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00204'
group by left(t1.st_date,6);



---子宫切除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020102';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020102' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00182'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---宫腔镜下宫腔粘连切除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020202';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020202' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00193'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---盆底重建术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020302';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020302' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00194'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---剖宫产死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020402';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020402' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00183'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---产钳助产术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020502';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020502' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00196'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---子宫颈根治性切除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020602';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020602' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00197'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---腹腔镜下子宫次全切除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020702';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020702' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00198'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---腹腔镜下子宫全切除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020802';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020802' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00199'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---腹腔镜下子宫肌瘤切除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020902';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020902' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00200'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---宫腔镜电切术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021002';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021002' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00201'
and t2.lyfs = '5'
group by left(t1.st_date,6);

---阴式子宫肌瘤切除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021102';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021102' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00202'
and t2.lyfs = '5'
group by left(t1.st_date,6);


---广泛全子宫清除术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021202';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021202' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00203'
and t2.lyfs = '5'
group by left(t1.st_date,6);


---乳腺癌根治术死亡例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021302';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021302' as level_code ,
count( distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00204'
and t2.lyfs = '5'
group by left(t1.st_date,6);


---子宫切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020103';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020103' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00182'
group by left(t1.st_date,6);

---宫腔镜下宫腔粘连切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020203';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020203' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00193'
group by left(t1.st_date,6);

---盆底重建术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020303';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020303' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00194'
group by left(t1.st_date,6);

---剖宫产平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020403';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020403' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00183'
group by left(t1.st_date,6);

---产钳助产术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020503';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020503' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00196'
group by left(t1.st_date,6);

---子宫颈根治性切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020603';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020603' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00197'
group by left(t1.st_date,6);

---腹腔镜下子宫次全切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020703';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020703' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00198'
group by left(t1.st_date,6);

---腹腔镜下子宫全切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020803';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020803' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00199'
group by left(t1.st_date,6);

---腹腔镜下子宫肌瘤切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020903';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020903' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00200'
group by left(t1.st_date,6);

---宫腔镜电切术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021003';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021003' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00201'
group by left(t1.st_date,6);

---阴式子宫肌瘤切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021103';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021103' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00202'
group by left(t1.st_date,6);


---广泛全子宫切除术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021203';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021203' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00203'
group by left(t1.st_date,6);


---乳腺癌根治术平均住院日
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021303';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021303' as level_code ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
sum(t2.in_days)/count(distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00204'
group by left(t1.st_date,6);


---子宫切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020104';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020104' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00182'
group by left(t1.st_date,6);

---宫腔镜下宫腔粘连切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020204';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020204' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00193'
group by left(t1.st_date,6);

---盆底重建术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020304';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020304' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00194'
group by left(t1.st_date,6);

---剖宫产平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020404';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020404' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00183'
group by left(t1.st_date,6);

---产钳助产术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020504';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020504' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00196'
group by left(t1.st_date,6);

---子宫颈根治性切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020604';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020604' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00197'
group by left(t1.st_date,6);

---腹腔镜下子宫次全切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020704';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020704' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00198'
group by left(t1.st_date,6);

---腹腔镜下子宫全切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020804';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020804' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00199'
group by left(t1.st_date,6);

---腹腔镜下子宫肌瘤切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020904';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020904' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00200'
group by left(t1.st_date,6);

---宫腔镜电切术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021004';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021004' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00201'
group by left(t1.st_date,6);

---阴式子宫肌瘤切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021104';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021104' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00202'
group by left(t1.st_date,6);


---广泛全子宫切除术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021204';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021204' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00203'
group by left(t1.st_date,6);


---乳腺癌根治术平均住院费用
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021304';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021304' as level_code ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as level_value,
now() as update_time ,
round(sum(t2.total_fees)/count(distinct t1.pai_visit_id),4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00204'
group by left(t1.st_date,6);


---子宫切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020106';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020106' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00182'
group by left(t1.st_date,6);

---宫腔镜下宫腔粘连切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020206';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020206' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00193'
group by left(t1.st_date,6);

---盆底重建术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020306';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020306' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00194'
group by left(t1.st_date,6);

---剖宫产术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020406';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020406' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00183'
group by left(t1.st_date,6);

---产钳助产术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020506';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020506' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00196'
group by left(t1.st_date,6);

---子宫颈根治性切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020606';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020606' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00197'
group by left(t1.st_date,6);

---腹腔镜下子宫次全切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020706';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020706' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00198'
group by left(t1.st_date,6);

---腹腔镜下子宫全切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020806';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020806' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00199'
group by left(t1.st_date,6);

---腹腔镜下子宫肌瘤切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702020906';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702020906' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00200'
group by left(t1.st_date,6);

---宫腔镜电切术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021006';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021006' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00201'
group by left(t1.st_date,6);

---阴式子宫肌瘤切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021106';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021106' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00202'
group by left(t1.st_date,6);


---广泛全子宫切除术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021206';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021206' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00203'
group by left(t1.st_date,6);


---乳腺癌根治术术后非预期重返手术室例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702021306';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021306' as level_code ,
count(distinct t1.pai_visit_id)   as level_value,
now() as update_time ,
count(distinct t1.pai_visit_id)   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on t1.pai_visit_id = t2.pai_visit_id and t2.key in ('D05024','D5025')
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00204'
group by left(t1.st_date,6);



---手术并发症出院人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010403';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702021302' as level_code ,
count(  t1.pai_visit_id)  as level_value,
now() as update_time ,
count(  t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00048'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---手术并发症导致死亡人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040302';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040302' as level_code ,
count(  t1.pai_visit_id)  as level_value,
now() as update_time ,
count(  t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00044'
and left(t1.st_date,6)=c_monthlist.month_id
and t2.lyfs = '5'
group by left(t1.st_date,6);

---手术后伤口裂开、感染人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040303';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040303' as level_code ,
count(  distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00226'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---手术后出血或血肿人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040307';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040307' as level_code ,
count(  distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00227'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);

---手术后呼吸衰竭人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040309';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040309' as level_code ,
count(  distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00229'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);

---新陈代谢紊乱例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040314';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040314' as level_code ,
count(  distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00228'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---新生儿产伤
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040401';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040401' as level_code ,
count(  distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00231'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---新生儿产伤占活产婴儿数比例（%）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040402';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040402' as level_code ,
round((count(t1.pai_visit_id)*1.00 / t2.value)*100,4) as level_value,
now() as update_time ,
round((count(t1.pai_visit_id)*1.00 / t2.value)*100,4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
left join (
    select
left(st_date,6) as month_id,
count(1) as value
from his_bi.dwd_inp_quantity_d
where
key = 'D00157'
and value = '1'
group by left(st_date,6)
    )t2 on left(t1.st_date,6) = t2.month_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00231'
group by left(t1.st_date,6),t2.value;


---非器械辅助阴道分娩产伤占阴道分娩人数比例（%）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040404';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040404' as level_code ,
round((count(t1.pai_visit_id)*1.00 / t2.value)*100,4) as level_value,
now() as update_time ,
round((count(t1.pai_visit_id)*1.00 / t2.value)*100,4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
left join (
    select
left(st_date,6) as month_id,
count(1) as value
from his_bi.dwd_inp_quantity_d
where
key = 'D00161'
and value not in('1','2')
group by left(st_date,6)
    )t2 on left(t1.st_date,6) = t2.month_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00042'
group by left(t1.st_date,6),t2.value;


---器械辅助阴道分娩产伤占阴道分娩人数比例（%）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040406';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040406' as level_code ,
round((count(t1.pai_visit_id)*1.00 / t2.value)*100,4) as level_value,
now() as update_time ,
round((count(t1.pai_visit_id)*1.00 / t2.value)*100,4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
left join (
    select
left(st_date,6) as month_id,
count(1) as value
from his_bi.dwd_inp_quantity_d
where
key = 'D00161'
and value not in('1','2')
group by left(st_date,6)
    )t2 on left(t1.st_date,6) = t2.month_id
where
left(t1.st_date,6) = c_monthlist.month_id
and t1.key = 'D00233'
group by left(t1.st_date,6),t2.value;


---非器械辅助阴道分娩产伤人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040403';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040403' as level_code ,
count(  distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00042'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---器械辅助阴道分娩产伤人数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040405';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040405' as level_code ,
count(  distinct t1.pai_visit_id)  as level_value,
now() as update_time ,
count( distinct t1.pai_visit_id)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dw_inp_patient_info_m t2 on t1.pai_visit_id = t2.pai_visit_id
where
t1.key = 'D00233'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);

---手术后伤口裂开、感染占手术人数比例（%）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040304';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040304' as level_code ,
round(count(  distinct t1.pai_visit_id)*1.00/count(distinct t2.pai_visit_id)*100,4)  as level_value,
now() as update_time ,
round(count(  distinct t1.pai_visit_id)*1.00/count(distinct t2.pai_visit_id)*100,4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00226'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---手术后出血或血肿占手术人数比例（%）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040307';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040307' as level_code ,
round(count(  distinct t1.pai_visit_id)*1.00/count(distinct t2.pai_visit_id)*100,4)  as level_value,
now() as update_time ,
round(count(  distinct t1.pai_visit_id)*1.00/count(distinct t2.pai_visit_id)*100,4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00227'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);



---手术后呼吸衰竭占手术人数比例（%）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040307';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040307' as level_code ,
round(count(  distinct t1.pai_visit_id)*1.00/count(distinct t2.pai_visit_id)*100,4)  as level_value,
now() as update_time ,
round(count(  distinct t1.pai_visit_id)*1.00/count(distinct t2.pai_visit_id)*100,4)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00229'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---重度卵巢过度刺激综合症例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040607';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040607' as level_code ,
count(  distinct t1.pai_visit_id) as level_value,
now() as update_time ,
count(  distinct t1.pai_visit_id) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00121'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---多胎妊娠（非自然）例数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV00702040608';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV00702040608' as level_code ,
count(  distinct t1.pai_visit_id) as level_value,
now() as update_time ,
count(  distinct t1.pai_visit_id) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dwd_inp_medical_d t1
--inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00107'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---每门诊人次费用（元）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010501';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010501' as level_code ,
t1.kpi_value  as level_value,
now() as update_time ,
t1.kpi_value   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.kpi_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.kpi_code='JX03801';

---每门诊人次药费（元）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010502';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010502' as level_code ,
t1.kpi_value  as level_value,
now() as update_time ,
t1.kpi_value   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.kpi_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.kpi_code='JX03901';

---每住院费用（元）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010503';
insert into his_bi.level_master_m
select
    am.month_id as month_id,
    'LV007010503' as level_code,
    round(sum(am.total_fees)/count(distinct am.pai_visit_id),5) as level_value,
    now() as update_time,
    round(sum(am.total_fees)/count(distinct am.pai_visit_id),5) as self_value,
    null as check_flag,
    null as check_comm
    from his_bi.dw_inp_patient_amount_m am
    where 1=1
    and am.month_id = c_monthlist.month_id
    group by am.month_id;

---每住院药费（元）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010504';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV007010504' as level_code ,
t1.kpi_value  as level_value,
now() as update_time ,
t1.kpi_value   as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.kpi_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.kpi_code='JX04101';



---抗菌药处方数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070501';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV0070501' as level_code ,
count(   t1.outp_visit_id) as level_value,
now() as update_time ,
count(   t1.outp_visit_id) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.DWD_OUTP_QUANTITY_D t1
--inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00036'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---门诊处方数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070502';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV0070502' as level_code ,
count(   t1.outp_visit_id) as level_value,
now() as update_time ,
count(   t1.outp_visit_id) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.DWD_OUTP_QUANTITY_D t1
--inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00035'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);



---注射剂处方数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070504';
insert into his_bi.level_master_m
select
left(t1.st_date,6) as month_id,
'LV0070504' as level_code ,
count(   t1.outp_visit_id) as level_value,
now() as update_time ,
count(   t1.outp_visit_id) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.DWD_OUTP_QUANTITY_D t1
--inner join his_bi.dwd_inp_medical_d t2 on left(t1.st_date,6) = left(t2.st_date,6) and t2.key='D00048'
where
t1.key = 'D00037'
and left(t1.st_date,6)=c_monthlist.month_id
--and t2.lyfs = '5'
group by left(t1.st_date,6);


---医疗总收入
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070507';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV0070507' as level_code ,
round(sum(t1.kpi_value)/10000,5)  as level_value,
now() as update_time ,
round(sum(t1.kpi_value)/10000,5) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.kpi_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.kpi_code in('JX02701','JX02901')
group by t1.month_id;


---药费收入
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070506';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV0070506' as level_code ,
round(sum(t1.kpi_value)/10000,5)  as level_value,
now() as update_time ,
round(sum(t1.kpi_value)/10000,5)  as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.kpi_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.kpi_code in('JX03902','JX04102')
group by t1.month_id;


---抗菌药物金额（万元）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070509';
insert into his_bi.level_master_m
select
t1.month_id,
'LV0070509' as level_code ,
round(sum(t1.value+t2.value)/10000,5) as level_value,
now() as update_time ,
round(sum(t1.value+t2.value)/10000,5) as self_value  ,
null as check_flag  ,
null as check_comm
from
(select
left(st_date,6) as month_id,
sum(value) as value
from his_bi.DWD_OUTP_INCOME_D
where key = 'D00025'
group by left(st_date,6))t1 left join
(select
left(st_date,6) as month_id,
sum(value) as value
from his_bi.dwd_inp_income_d
where key = 'D05011'
group by left(st_date,6)) t2 on t1.month_id = t2.month_id
where
t1.month_id=c_monthlist.month_id
group by t1.month_id;




---抗菌药物使用强度
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070514';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV0070514' as level_code ,
t1.kpi_value as level_value,
now() as update_time ,
t1.kpi_value as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.kpi_master_m t1
where
t1.month_id=c_monthlist.month_id
and t1.kpi_code='JX017';


---门诊抗菌药物使用率
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070515';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV0070515' as level_code ,
round((count(case when t1.kjyw_cf_num >0 then 1 end)*1.0/count(distinct t1.outp_visit_id))*100,4) as level_value,
now() as update_time ,
round((count(case when t1.kjyw_cf_num >0 then 1 end)*1.0/count(distinct t1.outp_visit_id))*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from
his_bi.dw_outp_patient_info_m t1
where
COALESCE(is_tj,0)=0
and t1.month_id=c_monthlist.month_id
GROUP BY
t1.month_id;


---急诊患者抗菌药物使用率
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070516';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV0070516' as level_code ,
round((count(case when t1.kjyw_cf_num >0 then 1 end)*1.0/count(distinct t1.outp_visit_id))*100,4) as level_value,
now() as update_time ,
round((count(case when t1.kjyw_cf_num >0 then 1 end)*1.0/count(distinct t1.outp_visit_id))*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from
his_bi.dw_outp_patient_info_m t1
where
COALESCE(is_tj,0)=0
and t1.month_id=c_monthlist.month_id
and is_emergency = 1
GROUP BY
t1.month_id;

---住院患者使用抗菌药使用率
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070517';
insert into his_bi.level_master_m
select
t1.month_id as month_id,
'LV0070517' as level_code ,
round((count(case when t1.is_use_sykjyw >0 then 1 end)*1.0/count(distinct t1.pai_visit_id))*100,4) as level_value,
now() as update_time ,
round((count(case when t1.is_use_sykjyw >0 then 1 end)*1.0/count(distinct t1.pai_visit_id))*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from
his_bi.dw_inp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id
GROUP BY
t1.month_id;




---药费收入占医疗总收入比重（%）
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070508';
insert into his_bi.level_master_m
select
t1.month_id,
'LV0070508' as kpi_code,
round(COALESCE(max(t2.level_value),0)/max(t1.level_value),5)*100 as kpi_value,
now() as update_time,
round(COALESCE(max(t2.level_value),0)/max(t1.level_value),5)*100 as self_value,
null as check_flag,
null as check_comm
from
his_bi.level_master_m t1
left join his_bi.level_master_m t2 on t1.level_code = t2.level_code and t1.month_id = t2.month_id
and t2.level_code='LV0070506'
where
t1.month_id=c_monthlist.month_id
and t1.level_code in('LV0070506','LV0070507')
group by
t1.month_id;



----留观人次
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010203';
insert into his_bi.level_master_m
select
t1.month_id,
'LV007010203' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_outp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id and
t1.is_keep = '1'
group by month_id;



----抗菌药处方数/每百张门诊处方(%)
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070503';
insert into his_bi.level_master_m
select
t1.month_id,
'LV0070503' as kpi_code,
round(COALESCE(max(t2.level_value),0)/max(t1.level_value),5)*100 as level_value,
now() as update_time,
round(COALESCE(max(t2.level_value),0)/max(t1.level_value),5)*100 as self_value,
null as check_flag,
null as check_comm
from
his_bi.level_master_m t1
left join his_bi.level_master_m t2 on t1.level_code = t2.level_code and t1.month_id = t2.month_id
and t2.level_code='LV0070501'
where
t1.month_id=c_monthlist.month_id
and t1.level_code in('LV0070501','LV0070502')
group by
t1.month_id;



----注射剂处方数/每百张门诊处方(%)
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV0070505';
insert into his_bi.level_master_m
select
t1.month_id,
'LV0070505' as kpi_code,
round(COALESCE(max(t2.level_value),0)/max(t1.level_value),5)*100 as level_value,
now() as update_time,
round(COALESCE(max(t2.level_value),0)/max(t1.level_value),5)*100 as self_value,
null as check_flag,
null as check_comm
from
his_bi.level_master_m t1
left join his_bi.level_master_m t2 on t1.level_code = t2.level_code and t1.month_id = t2.month_id
and t2.level_code='LV0070504'
where
t1.month_id=c_monthlist.month_id
and t1.level_code in('LV0070504','LV0070502')
group by
t1.month_id;


----床位周转次数
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010404';
insert into his_bi.level_master_m
select
replace(left(stat_date::text,7),'-','') as month_id,
'LV007010404' as level_code ,
round(((sum(actual_f_num)+sum(to_dept_num))/sum(sy_num))*100,4) as level_value,
now() as update_time ,
round(((sum(actual_f_num)+sum(to_dept_num))/sum(sy_num))*100,4) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_inp_dept_work_d t1
where
replace(left(stat_date::text,7),'-','')=c_monthlist.month_id
group by replace(left(stat_date::text,7),'-','');
'''
txt = txt.replace('\n', '')
txt = txt.strip()
pattern1 = re.compile(r'/\*() as level_value', flags = re.I|re.S)
re.findall(pattern1,txt)
for i in range(len(replace_now)):
    replaceStr(r'C:\Users\CBH\Desktop\work_job\BI\sql.txt','.* as level_value',replace_now[i])
    print(re.sub('.* as level_value', replace_now[i]+' as level_value', txt))


def alter(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)


for  i in range(len(replace_now)):
    alter(r'C:\Users\CBH\Desktop\work_job\BI\sql.txt',replace_after[i], replace_now[i])

a = list(set(replace_after))
b = list(set(replace_now))
with open(r'C:\Users\CBH\Desktop\work_job\BI\sql.txt', "r", encoding="utf-8") as f1, open("%s.bak" % r'C:\Users\CBH\Desktop\work_job\BI\sql.txt', "w", encoding="utf-8") as f2:
    for line in f1:
        for i in range(len(b)):
            if a[i] in line:
                line = line.replace(a[i], b[i])
        f2.write(line)

#解决问题的核心代码
import pandas as  pd
import re
df = pd.read_table(r'C:\Users\CBH\Desktop\work_job\BI\sql.txt')
df = pd.DataFrame(df)
pattern = re.compile('(.*) as level_value',re.IGNORECASE)

df.columns=['name']
replace_after = []
for i in df['name']:
    pattern = re.compile('round(.*) as level_value', re.IGNORECASE)
    # print(re.findall(pattern, i))
    if bool(re.findall(pattern, i)) == True:
        print(re.findall(pattern, i))
        replace_after.append(str(re.findall(pattern, i)).replace('[','').replace(']','').replace("'",''))
    else:
        print('空值')


df1 = pd.DataFrame(replace_after)
replace_now=[]
for g in df1[0]:
    print('COALESCE('+g+',0)')
    replace_now.append('COALESCE('+g+',0)')

df = pd.read_table(r'C:\Users\CBH\Desktop\work_job\BI\替换后sql.sql')
df = pd.DataFrame(df)
df.columns=['name']
df['name1']= df['name'].replace('count(1) as level_value,',replace_now[1],regex=True)

df['col2']=df['name']

i = 0
while i <=231:
    df.loc[df['name'] == replace_after[i] + ' as level_value,', 'col2'] = replace_now[i]+' as level_value,'
    df.loc[df['name'] == replace_after[i] + ' as self_value  ,', 'col2'] = replace_now[i] + ' as self_value,'
    i +=1

del df['name']
df.to_csv('result202007127.txt',encoding='utf-8',index=False)







import re
txt = '''---LV007010201年门诊人次
delete from his_bi.level_master_m where month_id = c_monthlist.month_id and level_code = 'LV007010201';
insert into his_bi.level_master_m
select
t1.month_id,
'LV007010201' as level_code ,
count(1) as level_value,
now() as update_time ,
count(1) as self_value  ,
null as check_flag  ,
null as check_comm
from his_bi.dw_outp_patient_info_m t1
where
t1.month_id=c_monthlist.month_id and
coalesce(t1.is_tj,0)=0
group by month_id;'''

ret = re.sub('\s.*\s+level_value','a',txt)