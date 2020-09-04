CREATE OR REPLACE FUNCTION "dwd"."fun_dwd_DI0006_d"("v_start_date" varchar, "v_end_date" varchar)
      RETURNS "pg_catalog"."varchar" AS $BODY$
    /***
    函数名称：住院患者患者住院患者是否四级手术患者(0 否 1是)（国家标准）   
        作用：统计某天住院患者住院患者是否四级手术患者(0 否 1是)（国家标准）   
      开发人：leslie 2020-08-17
    命名规范：FUN_模型层级(DWD或者DW)_KPI编码_日期类型D或者M，D表示按天统计，M表示按月统计
     KPI编码：DI0006  根据原子指标编码规划来的
        入参：v_start_date，v_end_date  格式均为yyyymmdd，可以一次运行多天的数据
    ***/
    
    DECLARE
      v_StDate_to   DATE;
      v_date_f DATE;
      v_date_t DATE;
     BEGIN
        v_date_f := to_date(v_start_date, 'yyyymmdd');
        v_date_t := to_date(v_end_date, 'yyyymmdd'); 
     WHILE v_date_f <= v_date_t LOOP
       v_date_f := v_date_f +1;
       v_StDate_to := v_date_f -1;
    delete from his_bi.dwd_inp_medical_d  where st_date = c_daylist.day_id and key = 'DI0006';   INSERT into his_bi.dwd_inp_medical_d (key,value,patient_id,visit_id,pai_visit_id,insert_date,                    remark,st_date)   select distinct      'DI0006',      1,     a.bah as patient_id,     a.zycs as visit_id,     pt.pai_visit_id,     now(),     '是否四级手术患者(0 否 1是)',     to_char(a.cyrq,'yyyymmdd') as st_date   from his_bi.ods_patient_medical_record a  inner join ods.his_pts_pai_visit pt on a.bah = pt.patient_id and a.zycs = pt.visit_id  inner join his_bi.ods_patient_opertion_info t on t.brxh =a.brxh   where 1=1   and exists(select 1 from his_bi.dim_3_4_oper_info m         where t.surgerycode = m.icd9_code)    and a.cyrq >= to_date(c_daylist.day_id,'yyyyMMdd')    and a.cyrq <  to_date(c_daylist.day_id,'yyyyMMdd') + 1  ;      END LOOP;
       RETURN 'SUCCESS';
    END;
      $BODY$
      LANGUAGE plpgsql VOLATILE
      COST 100