# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    re_executor_function
   Description :
   Author :       CBH
   date：         2020/6/21 10: 12
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/21 10: 12:
-------------------------------------------------
"""
import re
import pandas as pd
df = pd.read_excel(r'C:\Users\CBH\Desktop\Function_backup2020-06-16.xls')
df['detail']

sub_num=[]
sub_main_table=[]
sub_table=[]

for i in df['detail']:
    try:
        # print(str(i))
        i = i.replace('\n', '')
        i = i.strip()
        pattern_yl = re.compile('insert\s+into\s+.*\s+from\shis_bi.(\w+)|insert\s+into\s+.*\s+st_date\s+FROM\s+his_bi.(\w+)', re.IGNORECASE | re.M)
        result = re.findall(pattern_yl, str(i))
        print(result)
        sub_main_table.append(result)
        #sub_table
        pattern_sub_yl = re.compile('join his_bi.(\w+)', re.IGNORECASE | re.M)
        result_sub_yl = re.findall(pattern_sub_yl, str(i))
        sub_table.append(result_sub_yl)
        #sub_num
        pattern_sub_dnum = re.compile("delete\s+from.*key\s=\s'(D\d{5})'", re.IGNORECASE | re.M)
        sub_num_result = re.findall(pattern_sub_dnum, str(i))
        sub_num.append(sub_num_result)
    except:
        continue

df['sub_main_table'] = pd.DataFrame(sub_main_table)
df['sub_table'] = sub_table
df['sub_num'] = pd.DataFrame(sub_num)

for g in df['detail']:
    g = g.replace('\n', '')
    g = g.strip()
    pattern_ylx = re.compile('insert\s+into\s+.*\s+from\shis_bi.(\w+)|insert\s+into\s+.*\s+st_date\s+FROM\s+his_bi.(\w+)', re.IGNORECASE | re.M)
    print(re.findall(pattern_ylx, g))


text = '''
/***
函数名称：住院患者髋、膝关节置换术打标
    作用：统计某天住院患者中做了髋、膝关节置换术的人
  开发人：肖斌 2020-05-16
命名规范：FUN_模型层级(DWD或者DW)_KPI编码_日期类型D或者M，D表示按天统计，M表示按月统计
 KPI编码：D00174  根据原子指标编码规划来的
    入参：v_start_date，v_end_date  格式均为yyyymmdd，可以一次运行多天的数据

   髋、膝关节置换术
***/
DECLARE
	c_daylist record;
	o_start_date varchar;
	o_end_date varchar;
	i_start_date varchar;
	i_end_date varchar;
	i_count  int4;
BEGIN

  /*如果指标没有历史指标数据，甘肃默认以20200101开始计算*/
	/*住院数据，每次运行当前日期前15天出院的患者，因为病案首页归档有2周左右的延迟*/
  select count(1),to_char(to_date(to_char(now(),'yyyymmdd'),'yyyymmdd') - 15,'yyyymmdd')
         into i_count,i_end_date
	  from his_bi.dwd_inp_medical_d 
	 where key = 'D00174';
	 
  if(i_count = 0)
	  then 
		  i_start_date := '20200101';
			--raise notice '0 i_start_date is: %', i_start_date;
	else if(i_count > 0)
	  then
		  i_start_date := i_end_date;
			--raise notice '1 i_start_date is: %', i_start_date;
  end if;
	end if;
		
  if(length(trim(v_start_date)) = 0 and length(trim(v_end_date)) = 0)
	/*kettle 调用时，如果不设置参数，默认传入 空字符串，那么默认取当前日期后退一天 */
	  then 
	    o_start_date := i_start_date;
	    o_end_date := i_end_date;
			--raise notice '2 o_start_date is: %', o_start_date;
			--raise notice '2 o_end_date is: %', o_end_date;
	else if (length(trim(v_start_date)) <> 0 and length(trim(v_end_date)) <> 0)
	/*PG function 如果参入任何参数，那么以实际入参为准*/
	  then 
		  o_start_date := v_start_date;
	    o_end_date := v_end_date;
			--raise notice '3 o_start_date is: %', o_start_date;
			--raise notice '3 o_end_date is: %', o_end_date;
	end if;
	end if;
	
	for c_daylist in (select day_id from his_bi.dim_date_info where day_id >= o_start_date and day_id <= o_end_date order by day_id)
	loop 
	
	--raise notice '4 c_daylist.day_id is: %', c_daylist.day_id;
	
	delete from his_bi.dwd_inp_medical_d  where st_date = c_daylist.day_id and key = 'D00174';
	
  INSERT into his_bi.dwd_inp_medical_d (key,value,patient_id,visit_id,pai_visit_id,insert_date,
																			 remark,st_date) 
   SELECT
		'D00174' as key,
		count(1) as value,
		pai.patient_id,
		pai.visit_id,
		pai.pai_visit_id,
		Now () as insert_date,
		'重点手术：髋、膝关节置换术' remark ,
		to_char(o.surgerydate,'yyyymmdd') as st_date
	FROM
		his_bi.ods_patient_opertion_info o,
		his_bi.pts_pai_visit pai 
	WHERE
		o.patient_id = pai.patient_id 
		AND o.visit_id = pai.visit_id 
		AND his_bi.has_matched_icd9_rule ('SJGL_DJPS_ZDSS',o.surgerycode,'髋、膝关节置换术')
		AND o.surgerydate >= to_date(c_daylist.day_id,'yyyyMMdd')
		AND o.surgerydate <  to_date(c_daylist.day_id,'yyyyMMdd') + 1 
		GROUP BY
		pai.patient_id,
		pai.visit_id,
		pai.pai_visit_id,
		insert_date,
		remark ,
		st_date
  ; 
 
	 end loop;
   RETURN 'SUCCESS';  
END;
'''

text = text.replace('\n','')
text=text.strip()
text = text.replace('\t','')
pattern = re.compile('delete from (.*).where',re.IGNORECASE)
print(re.findall(pattern,text)) #dwd表名字
pattern_yl = re.compile('insert\s+into\s+.*\s+from\shis_bi.*',re.IGNORECASE|re.M)
print(re.findall(pattern_yl,text))

pattern_ylx = re.compile('insert\s+into\s+.*\s+st_date\s+FROM\s+his_bi.(\w+)',re.IGNORECASE|re.M)
print(re.findall(pattern_ylx,text))


pattern_sub_yl = re.compile('join his_bi.(\w+)',re.IGNORECASE|re.M)
print(re.findall(pattern_sub_yl,text))
#指标值
pattern_sub_dnum = re.compile("delete\s+from.*key\s=\s'(D\d{5})'",re.IGNORECASE|re.M)
print(re.findall(pattern_sub_dnum,text))