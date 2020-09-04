# -*- coding: utf-8 -*-
# @File: function_auto_write.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/14  15:04




from NTRMYY.Auto_Write.Auto_write_model import *
a =auto_write_list()



for i in range(len(key_total)):
    # print(i)
    a = condition[i].replace('\\r','\n')
    print(a)
    txt1 = '''CREATE OR REPLACE FUNCTION "dwd"."fun_dwd_'''
    key = key_total[i]
    txt2 = '''_d"("v_start_date" varchar, "v_end_date" varchar)
      RETURNS "pg_catalog"."varchar" AS $BODY$
    /***
    函数名称：住院患者患者{remark}
        作用：统计某天住院患者{remark}
      开发人：leslie 2020-08-17
    命名规范：FUN_模型层级(DWD或者DW)_KPI编码_日期类型D或者M，D表示按天统计，M表示按月统计
     KPI编码：{key}  根据原子指标编码规划来的
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
    '''.format(key = key_total[i],remark=remark[i])
    condition1 = condition[i].replace('\\r','\n')
    end_str = '''     END LOOP;
       RETURN 'SUCCESS';
    END;
      $BODY$
      LANGUAGE plpgsql VOLATILE
      COST 100'''
    txt = txt1+key+txt2+condition1+end_str
    print(txt)
    with open('fun_dwd_'+key_total[i]+'_d.sql','a+',encoding='utf-8') as f:
        f.write(txt)
        f.close()


#将本地function写入pg
from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.LogUitl import *
import os
list_dir = os.listdir(r'C:\Users\CBH\Desktop\work_job\南通项目\function_job\20200825')
path = r'C:\Users\CBH\Desktop\work_job\南通项目\function_job\20200825'
for i in list_dir:
    with open(os.path.join(path,i),'r',encoding='utf-8') as f:
        with PgSQLContextManager() as db_cursor:
            db_cursor.execute(f.read())
            a = f.read()
            print(a)

    print(i)


'''
批量处理框架思路：
1；将原始function读取
2；进行正则提取
3；应该甘肃和南通的编码关系
4；
'''
import pandas  as pd
import re
df = pd.read_csv(r'C:\Users\CBH\Desktop\Function_backup2020-08-11.csv')

kpi_code=[]
func_name=[]
remark = []

for i in df['detail']:
    # print(i)
    text = i.replace('\n', '')
    text = text.replace('\t',' ')
    text = text.strip()
    # print(text)
    patten_code1 = re.compile("(delete.*)\s+end loop", re.I)
    print(re.findall(patten_code1, text)) #函数内容
    func_name.append(re.findall(patten_code1, text))
    patten_code = re.compile("delete\s+from.*key\s=\s'(D\d{5})", re.I)
    kpi_code.append(re.findall(patten_code, text))  # 指标编码
    patten_code2 = re.compile("函数名称：(.*)\s+作用",re.I)
    remark.append(re.findall(patten_code2, text))


df1 = pd.DataFrame()
df1['kpi_code']  = kpi_code
df1['func_detail'] = func_name
df1['remark'] = remark
df1.to_csv(r'regsfy.csv')

#根据remark判断old区间
find_condition = ['是否下转患者',
'是否手术患者',
'是否择期手术',
'是否日间手术',
'是否微创手术患者',
'是否四级手术患者',
'是否手术并发症患者',
'是否I类切口感染',
'是否I类切口手术',
'是否危重患者',
'是否病危患者',
'是否自动离院',
'是否死亡',
'当天重返（国家标准）',
'2-15天重返（国家标准）',
'16-31天重返（国家标准）',
'1-31天重返（国家标准）',
'2-31天重返（国家标准）',]
remark = []
result = []

for index,i in enumerate(df1['remark']):
    # print(str(i))
    for cond in find_condition:
        # print(cond)
        if cond in str(i):
            print(str(i).replace("['","").replace("']",""))
            remark.append(str(i).replace("['","").replace("']","").replace('\t',''))
            print(index)
            print(str(df1['func_detail'][index]).replace('''["''',"").replace('''"]''',""))
            result.append(str(df1['func_detail'][index]).replace('''["''',"").replace('''"]''',"").replace('\t','').replace("to_date(c_daylist.day_id,'yyyyMMdd'))",'v_StDate_to'))
        else :
            pass

df2 = pd.DataFrame()
df2['remark'] = remark
df2['result'] = result
df2.to_csv('pipeijieguo.csv')
df2 = df2.drop_duplicates()
df_cls = pd.read_excel(r'C:\Users\CBH\Desktop\work_job\南通项目\code_module.xlsx')
#判断映射关系


r_code=[]
r_name = []
ao = lambda x,y: str(x) in str(y)
for index,i in enumerate(df_cls['remark']):
    for cond in df2['remark']:
        # print(cond)
        if str(i) in str(cond) :
            # print(df_cls['code'][index])
            # r_code.append(df_cls['code'][index])
            print(cond)
            r_name.append(cond)
        else:
            pass


##读取函数文档
df4 = pd.read_excel(r'C:\Users\CBH\Desktop\work_job\南通项目\Auto_write_model.xlsx')
df4 = pd.DataFrame(df4)
patten_1 = re.compile("(delete.*)\s+end loop", re.I)
gg = []
for index,i in enumerate(df4['condition']):
    print(i)
    patten_1 = re.compile("(D\d{5})", re.I)
    # gg.append(re.findall(patten_1,i))
    gg.append(re.sub(patten_1,df4['code'][index],i))
# gg = set(gg)
# temp = []
# [temp.append(i) for i in gg if i not in temp]
df4['gg'] = gg
df4.to_csv('abcMe.csv')

#批量替换表名
old_name = ['his_bi.bds_bds_icd10',
'his_bi.bds_bds_icd9',
'his_bi.bds_hrp_account_unit',
'his_bi.bms_bill_item',
'his_bi.bms_bill_item_history',
'his_bi.bms_fi_fo_emp',
'his_bi.bms_mips_apportion_info',
'his_bi.bms_mips_charge_type_vs_insur_t',
'his_bi.bms_mips_dict',
'his_bi.bms_mips_dict_class',
'his_bi.bms_mips_insurance_type_dict',
'his_bi.bms_mips_pati_visit_info',
'his_bi.bms_mips_rek_rel_settlement_info',
'his_bi.bms_mips_settlement_info',
'his_bi.bms_pay',
'his_bi.bms_pay_paymode',
'his_bi.bms_prepayment_overdraft_reserve',
'his_bi.bms_refund_apply',
'his_bi.bms_refund_apply_detail',
'his_bi.bms_rek',
'his_bi.bms_rel_tran_inv',
'his_bi.dms_goods_apply_plan',
'his_bi.dms_goods_apply_plan_sub',
'his_bi.dms_goods_basic_info',
'his_bi.dms_goods_class_manager_type_rel',
'his_bi.dms_goods_clinic_type_dict',
'his_bi.dms_goods_docu_detail',
'his_bi.dms_goods_docu_detail_and_notice_r',
'his_bi.dms_goods_docu_head',
'his_bi.dms_goods_extends_info',
'his_bi.dms_goods_financing_pay_info',
'his_bi.dms_goods_financing_pay_tictet',
'his_bi.dms_goods_hmcs_apply',
'his_bi.dms_goods_hmcs_apply_detail',
'his_bi.dms_goods_inside_code_dict',
'his_bi.dms_goods_inventory',
'his_bi.dms_goods_inventory_entity_detail',
'his_bi.dms_goods_inventory_physical',
'his_bi.dms_goods_inventory_sub',
'his_bi.dms_goods_stock_in_audit_bill',
'his_bi.dms_goods_stock_in_audit_detail',
'his_bi.dms_goods_stock_onway_table',
'his_bi.dms_goods_stock_snapshot',
'his_bi.dms_goods_stock_snapshot_detail',
'his_bi.dms_goods_stock_table',
'his_bi.dms_goods_store_class_dict',
'his_bi.dms_goods_store_manage_level_dict',
'his_bi.dms_goods_supplier_catalog',
'his_bi.dms_inside_code_dict',
'his_bi.dms_pds_inp_pham_apply_detail',
'his_bi.dms_pds_inp_pham_apply_master',
'his_bi.dms_pds_supply',
'his_bi.dms_pds_supply_detail',
'his_bi.dms_pds_supply_pro',
'his_bi.dms_pham_attribute_info',
'his_bi.dms_pham_basic_info',
'his_bi.dms_pham_docu_detail',
'his_bi.dms_pham_docu_head',
'his_bi.dms_pham_org',
'his_bi.dms_pham_pay_notice_info',
'his_bi.dms_pham_stock_onway_table',
'his_bi.dms_pham_stock_snapshot',
'his_bi.dms_pham_stock_snapshot_detail',
'his_bi.dms_pham_stock_table',
'his_bi.dms_pham_stock_table_sub',
'his_bi.dms_pham_cust_def_cont',
'his_bi.pts_pai_visit',
'his_bi.pts_pts_basic_org_medi_team',
'his_bi.emr_cp_exe_item',
'his_bi.emr_cp_exe_pathway',
'his_bi.emr_cp_exe_pathway_additionalinfo',
'his_bi.emr_cpoe_app',
'his_bi.emr_cpoe_app_and_ord_rel',
'his_bi.emr_cpoe_app_ca_rel_vst',
'his_bi.emr_cpoe_app_common_deta',
'his_bi.emr_cpoe_app_report_lis',
'his_bi.emr_cpoe_app_report_opt',
'his_bi.emr_cpoe_app_report_pacs',
'his_bi.emr_cpoe_basic_dict_apply_alias',
'his_bi.emr_cpoe_basic_dict_inspec_sample',
'his_bi.emr_cpoe_dict_apply_catalog_new',
'his_bi.emr_cpoe_dict_apply_chec_rel_new',
'his_bi.emr_cpoe_dict_apply_insp_rel_new',
'his_bi.emr_cpoe_dict_apply_new',
'his_bi.emr_cpoe_in_ord_exec_plan',
'his_bi.emr_cpoe_ord',
'his_bi.emr_cpoe_ord_clinic_item',
'his_bi.emr_cpoe_outp_app_and_herb_rel',
'his_bi.emr_cpoe_outp_pacs_lis_treat',
'his_bi.emr_cpoe_outp_pacs_lis_treat_exec',
'his_bi.emr_cpoe_outp_presc',
'his_bi.emr_cpoe_outp_presc_exec',
'his_bi.emr_cpoe_outp_presc_item',
'his_bi.emr_fc_pati_allergic_record',
'his_bi.emr_fc_pati_diag',
'his_bi.emr_mrms_hp_basic_business',
'his_bi.emr_mrms_hp_datarecord',
'his_bi.emr_mrms_pai_basic_additional_info',
'his_bi.emr_mrms_pai_info',
'his_bi.emr_ord_operation_scheduling_info',
'his_bi.emr_sde_export_mrms_data',
'his_bi.pts_bed_info',
'his_bi.pts_outp_patient_reserve',
'his_bi.pts_outp_patient_visit',
'his_bi.pts_outp_patient_visit_cancel',
'his_bi.pts_outp_reg_master',
'his_bi.pts_outp_special_clinic',
'his_bi.pts_outp_special_clinic_price',
'his_bi.pts_pts_basic_org_medi_team_deta',]
new_name = ['ods.his_bds_bds_icd10',
'ods.his_bds_bds_icd9',
'ods.his_bds_hrp_account_unit',
'ods.his_bms_bill_item',
'ods.his_bms_bill_item_history',
'ods.his_bms_fi_fo_emp',
'ods.his_bms_mips_apportion_info',
'ods.his_bms_mips_charge_type_vs_insur_t',
'ods.his_bms_mips_dict',
'ods.his_bms_mips_dict_class',
'ods.his_bms_mips_insurance_type_dict',
'ods.his_bms_mips_pati_visit_info',
'ods.his_bms_mips_rek_rel_settlement_info',
'ods.his_bms_mips_settlement_info',
'ods.his_bms_pay',
'ods.his_bms_pay_paymode',
'ods.his_bms_prepayment_overdraft_reserve',
'ods.his_bms_refund_apply',
'ods.his_bms_refund_apply_detail',
'ods.his_bms_rek',
'ods.his_bms_rel_tran_inv',
'ods.his_dms_goods_apply_plan',
'ods.his_dms_goods_apply_plan_sub',
'ods.his_dms_goods_basic_info',
'ods.his_dms_goods_class_manager_type_rel',
'ods.his_dms_goods_clinic_type_dict',
'ods.his_dms_goods_docu_detail',
'ods.his_dms_goods_docu_detail_and_notice_r',
'ods.his_dms_goods_docu_head',
'ods.his_dms_goods_extends_info',
'ods.his_dms_goods_financing_pay_info',
'ods.his_dms_goods_financing_pay_tictet',
'ods.his_dms_goods_hmcs_apply',
'ods.his_dms_goods_hmcs_apply_detail',
'ods.his_dms_goods_inside_code_dict',
'ods.his_dms_goods_inventory',
'ods.his_dms_goods_inventory_entity_detail',
'ods.his_dms_goods_inventory_physical',
'ods.his_dms_goods_inventory_sub',
'ods.his_dms_goods_stock_in_audit_bill',
'ods.his_dms_goods_stock_in_audit_detail',
'ods.his_dms_goods_stock_onway_table',
'ods.his_dms_goods_stock_snapshot',
'ods.his_dms_goods_stock_snapshot_detail',
'ods.his_dms_goods_stock_table',
'ods.his_dms_goods_store_class_dict',
'ods.his_dms_goods_store_manage_level_dict',
'ods.his_dms_goods_supplier_catalog',
'ods.his_dms_inside_code_dict',
'ods.his_dms_pds_inp_pham_apply_detail',
'ods.his_dms_pds_inp_pham_apply_master',
'ods.his_dms_pds_supply',
'ods.his_dms_pds_supply_detail',
'ods.his_dms_pds_supply_pro',
'ods.his_dms_pham_attribute_info',
'ods.his_dms_pham_basic_info',
'ods.his_dms_pham_docu_detail',
'ods.his_dms_pham_docu_head',
'ods.his_dms_pham_org',
'ods.his_dms_pham_pay_notice_info',
'ods.his_dms_pham_stock_onway_table',
'ods.his_dms_pham_stock_snapshot',
'ods.his_dms_pham_stock_snapshot_detail',
'ods.his_dms_pham_stock_table',
'ods.his_dms_pham_stock_table_sub',
'ods.his_dms_pham_cust_def_cont',
'ods.his_pts_pai_visit',
'ods.his_pts_pts_basic_org_medi_team',
'ods.his_emr_cp_exe_item',
'ods.his_emr_cp_exe_pathway',
'ods.his_emr_cp_exe_pathway_additionalinfo',
'ods.his_emr_cpoe_app',
'ods.his_emr_cpoe_app_and_ord_rel',
'ods.his_emr_cpoe_app_ca_rel_vst',
'ods.his_emr_cpoe_app_common_deta',
'ods.his_emr_cpoe_app_report_lis',
'ods.his_emr_cpoe_app_report_opt',
'ods.his_emr_cpoe_app_report_pacs',
'ods.his_emr_cpoe_basic_dict_apply_alias',
'ods.his_emr_cpoe_basic_dict_inspec_sample',
'ods.his_emr_cpoe_dict_apply_catalog_new',
'ods.his_emr_cpoe_dict_apply_chec_rel_new',
'ods.his_emr_cpoe_dict_apply_insp_rel_new',
'ods.his_emr_cpoe_dict_apply_new',
'ods.his_emr_cpoe_in_ord_exec_plan',
'ods.his_emr_cpoe_ord',
'ods.his_emr_cpoe_ord_clinic_item',
'ods.his_emr_cpoe_outp_app_and_herb_rel',
'ods.his_emr_cpoe_outp_pacs_lis_treat',
'ods.his_emr_cpoe_outp_pacs_lis_treat_exec',
'ods.his_emr_cpoe_outp_presc',
'ods.his_emr_cpoe_outp_presc_exec',
'ods.his_emr_cpoe_outp_presc_item',
'ods.his_emr_fc_pati_allergic_record',
'ods.his_emr_fc_pati_diag',
'ods.his_emr_mrms_hp_basic_business',
'ods.his_emr_mrms_hp_datarecord',
'ods.his_emr_mrms_pai_basic_additional_info',
'ods.his_emr_mrms_pai_info',
'ods.his_emr_ord_operation_scheduling_info',
'ods.his_emr_sde_export_mrms_data',
'ods.his_pts_bed_info',
'ods.his_pts_outp_patient_reserve',
'ods.his_pts_outp_patient_visit',
'ods.his_pts_outp_patient_visit_cancel',
'ods.his_pts_outp_reg_master',
'ods.his_pts_outp_special_clinic',
'ods.his_pts_outp_special_clinic_price',
'ods.his_pts_pts_basic_org_medi_team_deta',]

resyua = []
for cond in df4['gg']:
    for index,rg in enumerate(old_name):
        if rg in cond:
            cond = str(cond).replace(rg,new_name[index])
            print(cond)
        else:
            pass
    resyua.append(cond)

df4['resyua'] = resyua
df4.to_csv('gxhb.csv')




#写入sql脚本
import os
for index,i in enumerate(df4['resyua']):
    print(i)
    with open(str(df4['code'][index])+'.sql','a+',encoding='utf-8') as f:
        f.write(i)
        f.close()

txt='''delete from his_bi.dwd_inp_income_d where st_date = c_daylist.day_id and key = 'DI1001';\r \r  INSERT into his_bi.dwd_inp_income_d(key,value,patient_id,visit_id,pai_visit_id,insert_date,\r                    remark,st_date) \r select \r    'DI1001',\r    coalesce(sum(t.charges),0),\r    t.patient_id,\r    t.visit_id,\r    t.pai_visit_id,\r    now(),\r   '住院患者总费用',\r   to_char(t.enter_date,'yyyymmdd') AS st_date\r from ods.his_bms_bill_item t\r left join ods.his_pts_pai_visit t1 on t.pai_visit_id = t1.pai_visit_id\r where t.enter_date >= to_date(c_daylist.day_id,'yyyyMMdd')\r   and t.enter_date <  to_date(c_daylist.day_id,'yyyyMMdd')+1\r   and t.in_out_flag = 'I' --只统计住院患者\r   and t.charges<>0 \r group by to_char(t.enter_date,'yyyymmdd'),\r     t.patient_id,\r     t.visit_id,\r     t.pai_visit_id\r     having coalesce(sum(t.charges),0)<>0 ;\r \r '''
with open(r'C:\Users\CBH\PycharmProjects\tensorflow\DI1003_d.sql','r',encoding='utf-8') as f:
    print(f.read().replace('\r','\n'))
    f.close()


fo =  open(r'C:\Users\CBH\PycharmProjects\tensorflow\DI1002_d.txt','r',encoding='utf-8')

for i in fo:
    print(i+'\n')