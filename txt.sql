delete from his_bi.dwd_inp_income_d where st_date = c_daylist.day_id and key = 'DI1008';
 
  INSERT into his_bi.dwd_inp_income_d(key,value,patient_id,visit_id,pai_visit_id,insert_date,
                    remark,st_date) 
 select 
    'DI1008',
    coalesce(sum(t.charges),0),
    t.patient_id,
    t.visit_id,
    t.pai_visit_id,
    now(),
   '住院患者床位费',
   to_char(t.enter_date,'yyyymmdd') AS st_date
 from ods.his_bms_bill_item t
 left join ods.his_pts_pai_visit t1 on t.pai_visit_id = t1.pai_visit_id
 where t.enter_date >= to_date(c_daylist.day_id,'yyyyMMdd')
 and t.enter_date <  to_date(c_daylist.day_id,'yyyyMMdd')+1
 and t.in_out_flag = 'I' --只统计住院患者
 and t.subj_code = 'C01'
 and t.charges<>0
 group by to_char(t.enter_date,'yyyymmdd'),
     t.patient_id,
     t.visit_id,
     t.pai_visit_id
 having coalesce(sum(t.charges),0)<>0    
     ;
 
 