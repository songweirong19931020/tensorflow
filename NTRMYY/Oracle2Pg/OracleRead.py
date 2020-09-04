# -*- coding: utf-8 -*-
# @File: OracleRead.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/20  13:48
from NTRMYY.util.Connect_oracle import *
from NTRMYY.util.account import *
import pandas as pd
import numpy as np
import itertools
import multiprocessing
import datetime as dt
start_time = dt.datetime.now()
print("开始时间:%s"%start_time)
with OracleSQLContextManager() as db_cursor:
    sql='''SELECT *
FROM ( SELECT OUTP_VISIT_ID
FROM PTS.OUTP_PATIENT_VISIT SAMPLE (0.1)
WHERE (OUTP_VISIT_ID IS NOT NULL)  ORDER BY DBMS_RANDOM.VALUE)
WHERE ROWNUM <= 100 ORDER by OUTP_VISIT_ID ASC'''
    db_cursor.execute(sql)
    result = db_cursor.fetchall()
    dataframe = pd.DataFrame(result)
    list_a = dataframe.values.tolist()
    out = list(itertools.chain.from_iterable(list_a))#将内嵌列表转为一个列表

    '''select * from PTS.OUTP_PATIENT_VISIT  where  (3364670 <= OUTP_VISIT_ID AND OUTP_VISIT_ID <= 3369803) '''
    querry_total=[]
    for index,i in enumerate(out):
        print(index)
        try:
            if index == 0 :
                sql = '''select "OUTP_VISIT_ID","REG_SEQUENCE","PATIENT_ID","VISIT_ID","PATI_NAME","OUTP_DATE","OUTP_SPECIAL_ID","OUTP_SPECIAL_NAME","OUTP_DURATION_CODE","DEPT_CODE","TITLE_CODE","EMP_NO","OUTP_TYPE_CODE","FEE_FLAG","KEEP_FLAG","ARREARS_REASON","REG_FEE","REG_FEE_CODE","CHECKUPS_FEE","CHECKUPS_FEE_CODE","FEE","REGISTRY_FLAG","REGISTRY_RESOURCE","REGISTERING_TIME","OPERATOR","VISIT_TYPE_CODE","CHARGE_TYPE_CODE","DISEASE_TYPE_CODE","REG_SORT_NO","MASTER_OR_ATIME_ID","ATIME_FLAG","PROOF_PRINT_NO","HOSPITAL_AREA_CODE","PATI_SEX","PATI_AGE","PATI_AGE_STRING","VISIT_BEGIN_DATE","VISIT_END_DATE","PAY_MODE","ADMISSION_DOCTOR","BIRTH_DATE","TRIAGE_STATUS","POOL_ID","RETURN_VISIT","TIME_QUANTUM","REK_ID","CURRENT_YEAR_ACCOUNT","OVER_YEAR_ACCOUNT","FUND_PAYMENT","EMERGENCY_FEE","ORG_INPUT_CODE","ORG_INPUT_NAME","DOCTOR_TREAT_TEAM_ID","COLLECTION","TRIAGE_NO","CARE_BABY_NO","COMMUNITY_FLAG","SICK_DATE","EMERGENCY_TYPE","INEMERGENCY_DATE","OUTEMERGENCY_DATE","HEIGHT","WEIGHT","REG_SORT_NO_STR","CURRENT_DOCTOR_ID","GREEN_CHANNEL_CODE","GUARANTEE_TYPE","EMERGENCY_BED","EMERGENCY_OPERATOR","GUARANTEE_NAME","REFERRAL","REFERRAL_REASON","GREEN_CHANNEL_TIME","NCOV_INFO" from PTS.OUTP_PATIENT_VISIT where ({start} <= OUTP_VISIT_ID and OUTP_VISIT_ID < {end})'''\
                    .format(start=out[index],end=out[index+1])
                print(sql)
                querry_total.append(sql)
                sqla = '''select "OUTP_VISIT_ID","REG_SEQUENCE","PATIENT_ID","VISIT_ID","PATI_NAME","OUTP_DATE","OUTP_SPECIAL_ID","OUTP_SPECIAL_NAME","OUTP_DURATION_CODE","DEPT_CODE","TITLE_CODE","EMP_NO","OUTP_TYPE_CODE","FEE_FLAG","KEEP_FLAG","ARREARS_REASON","REG_FEE","REG_FEE_CODE","CHECKUPS_FEE","CHECKUPS_FEE_CODE","FEE","REGISTRY_FLAG","REGISTRY_RESOURCE","REGISTERING_TIME","OPERATOR","VISIT_TYPE_CODE","CHARGE_TYPE_CODE","DISEASE_TYPE_CODE","REG_SORT_NO","MASTER_OR_ATIME_ID","ATIME_FLAG","PROOF_PRINT_NO","HOSPITAL_AREA_CODE","PATI_SEX","PATI_AGE","PATI_AGE_STRING","VISIT_BEGIN_DATE","VISIT_END_DATE","PAY_MODE","ADMISSION_DOCTOR","BIRTH_DATE","TRIAGE_STATUS","POOL_ID","RETURN_VISIT","TIME_QUANTUM","REK_ID","CURRENT_YEAR_ACCOUNT","OVER_YEAR_ACCOUNT","FUND_PAYMENT","EMERGENCY_FEE","ORG_INPUT_CODE","ORG_INPUT_NAME","DOCTOR_TREAT_TEAM_ID","COLLECTION","TRIAGE_NO","CARE_BABY_NO","COMMUNITY_FLAG","SICK_DATE","EMERGENCY_TYPE","INEMERGENCY_DATE","OUTEMERGENCY_DATE","HEIGHT","WEIGHT","REG_SORT_NO_STR","CURRENT_DOCTOR_ID","GREEN_CHANNEL_CODE","GUARANTEE_TYPE","EMERGENCY_BED","EMERGENCY_OPERATOR","GUARANTEE_NAME","REFERRAL","REFERRAL_REASON","GREEN_CHANNEL_TIME","NCOV_INFO" from PTS.OUTP_PATIENT_VISIT where ({start} <= OUTP_VISIT_ID and OUTP_VISIT_ID < {end})''' \
                    .format(start=out[index+1], end=out[index + 2])
                print(sqla)
                querry_total.append(sqla)
            elif index != 0 & index != 99:
                sql_f = '''select "OUTP_VISIT_ID","REG_SEQUENCE","PATIENT_ID","VISIT_ID","PATI_NAME","OUTP_DATE","OUTP_SPECIAL_ID","OUTP_SPECIAL_NAME","OUTP_DURATION_CODE","DEPT_CODE","TITLE_CODE","EMP_NO","OUTP_TYPE_CODE","FEE_FLAG","KEEP_FLAG","ARREARS_REASON","REG_FEE","REG_FEE_CODE","CHECKUPS_FEE","CHECKUPS_FEE_CODE","FEE","REGISTRY_FLAG","REGISTRY_RESOURCE","REGISTERING_TIME","OPERATOR","VISIT_TYPE_CODE","CHARGE_TYPE_CODE","DISEASE_TYPE_CODE","REG_SORT_NO","MASTER_OR_ATIME_ID","ATIME_FLAG","PROOF_PRINT_NO","HOSPITAL_AREA_CODE","PATI_SEX","PATI_AGE","PATI_AGE_STRING","VISIT_BEGIN_DATE","VISIT_END_DATE","PAY_MODE","ADMISSION_DOCTOR","BIRTH_DATE","TRIAGE_STATUS","POOL_ID","RETURN_VISIT","TIME_QUANTUM","REK_ID","CURRENT_YEAR_ACCOUNT","OVER_YEAR_ACCOUNT","FUND_PAYMENT","EMERGENCY_FEE","ORG_INPUT_CODE","ORG_INPUT_NAME","DOCTOR_TREAT_TEAM_ID","COLLECTION","TRIAGE_NO","CARE_BABY_NO","COMMUNITY_FLAG","SICK_DATE","EMERGENCY_TYPE","INEMERGENCY_DATE","OUTEMERGENCY_DATE","HEIGHT","WEIGHT","REG_SORT_NO_STR","CURRENT_DOCTOR_ID","GREEN_CHANNEL_CODE","GUARANTEE_TYPE","EMERGENCY_BED","EMERGENCY_OPERATOR","GUARANTEE_NAME","REFERRAL","REFERRAL_REASON","GREEN_CHANNEL_TIME","NCOV_INFO" from PTS.OUTP_PATIENT_VISIT where ({start} <= OUTP_VISIT_ID and OUTP_VISIT_ID < {end})''' \
                    .format(start=out[index+1], end=out[index+2])
                querry_total.append(sql_f)
        except:
            continue

    # sql1 = '''select "OUTP_VISIT_ID","REG_SEQUENCE","PATIENT_ID","VISIT_ID","PATI_NAME","OUTP_DATE","OUTP_SPECIAL_ID","OUTP_SPECIAL_NAME","OUTP_DURATION_CODE","DEPT_CODE","TITLE_CODE","EMP_NO","OUTP_TYPE_CODE","FEE_FLAG","KEEP_FLAG","ARREARS_REASON","REG_FEE","REG_FEE_CODE","CHECKUPS_FEE","CHECKUPS_FEE_CODE","FEE","REGISTRY_FLAG","REGISTRY_RESOURCE","REGISTERING_TIME","OPERATOR","VISIT_TYPE_CODE","CHARGE_TYPE_CODE","DISEASE_TYPE_CODE","REG_SORT_NO","MASTER_OR_ATIME_ID","ATIME_FLAG","PROOF_PRINT_NO","HOSPITAL_AREA_CODE","PATI_SEX","PATI_AGE","PATI_AGE_STRING","VISIT_BEGIN_DATE","VISIT_END_DATE","PAY_MODE","ADMISSION_DOCTOR","BIRTH_DATE","TRIAGE_STATUS","POOL_ID","RETURN_VISIT","TIME_QUANTUM","REK_ID","CURRENT_YEAR_ACCOUNT","OVER_YEAR_ACCOUNT","FUND_PAYMENT","EMERGENCY_FEE","ORG_INPUT_CODE","ORG_INPUT_NAME","DOCTOR_TREAT_TEAM_ID","COLLECTION","TRIAGE_NO","CARE_BABY_NO","COMMUNITY_FLAG","SICK_DATE","EMERGENCY_TYPE","INEMERGENCY_DATE","OUTEMERGENCY_DATE","HEIGHT","WEIGHT","REG_SORT_NO_STR","CURRENT_DOCTOR_ID","GREEN_CHANNEL_CODE","GUARANTEE_TYPE","EMERGENCY_BED","EMERGENCY_OPERATOR","GUARANTEE_NAME","REFERRAL","REFERRAL_REASON","GREEN_CHANNEL_TIME","NCOV_INFO" from PTS.OUTP_PATIENT_VISIT
    # where ({start} <= OUTP_VISIT_ID and OUTP_VISIT_ID <={end})''' \
    #     .format(start=out[98], end=out[99])
    sql2 = '''select "OUTP_VISIT_ID","REG_SEQUENCE","PATIENT_ID","VISIT_ID","PATI_NAME","OUTP_DATE","OUTP_SPECIAL_ID","OUTP_SPECIAL_NAME","OUTP_DURATION_CODE","DEPT_CODE","TITLE_CODE","EMP_NO","OUTP_TYPE_CODE","FEE_FLAG","KEEP_FLAG","ARREARS_REASON","REG_FEE","REG_FEE_CODE","CHECKUPS_FEE","CHECKUPS_FEE_CODE","FEE","REGISTRY_FLAG","REGISTRY_RESOURCE","REGISTERING_TIME","OPERATOR","VISIT_TYPE_CODE","CHARGE_TYPE_CODE","DISEASE_TYPE_CODE","REG_SORT_NO","MASTER_OR_ATIME_ID","ATIME_FLAG","PROOF_PRINT_NO","HOSPITAL_AREA_CODE","PATI_SEX","PATI_AGE","PATI_AGE_STRING","VISIT_BEGIN_DATE","VISIT_END_DATE","PAY_MODE","ADMISSION_DOCTOR","BIRTH_DATE","TRIAGE_STATUS","POOL_ID","RETURN_VISIT","TIME_QUANTUM","REK_ID","CURRENT_YEAR_ACCOUNT","OVER_YEAR_ACCOUNT","FUND_PAYMENT","EMERGENCY_FEE","ORG_INPUT_CODE","ORG_INPUT_NAME","DOCTOR_TREAT_TEAM_ID","COLLECTION","TRIAGE_NO","CARE_BABY_NO","COMMUNITY_FLAG","SICK_DATE","EMERGENCY_TYPE","INEMERGENCY_DATE","OUTEMERGENCY_DATE","HEIGHT","WEIGHT","REG_SORT_NO_STR","CURRENT_DOCTOR_ID","GREEN_CHANNEL_CODE","GUARANTEE_TYPE","EMERGENCY_BED","EMERGENCY_OPERATOR","GUARANTEE_NAME","REFERRAL","REFERRAL_REASON","GREEN_CHANNEL_TIME","NCOV_INFO" from PTS.OUTP_PATIENT_VISIT 
    where ((OUTP_VISIT_ID < {start}) OR ({end} <= OUTP_VISIT_ID)) ''' \
        .format(start=out[0], end=out[99])
    sql3 = '''select "OUTP_VISIT_ID","REG_SEQUENCE","PATIENT_ID","VISIT_ID","PATI_NAME","OUTP_DATE","OUTP_SPECIAL_ID","OUTP_SPECIAL_NAME","OUTP_DURATION_CODE","DEPT_CODE","TITLE_CODE","EMP_NO","OUTP_TYPE_CODE","FEE_FLAG","KEEP_FLAG","ARREARS_REASON","REG_FEE","REG_FEE_CODE","CHECKUPS_FEE","CHECKUPS_FEE_CODE","FEE","REGISTRY_FLAG","REGISTRY_RESOURCE","REGISTERING_TIME","OPERATOR","VISIT_TYPE_CODE","CHARGE_TYPE_CODE","DISEASE_TYPE_CODE","REG_SORT_NO","MASTER_OR_ATIME_ID","ATIME_FLAG","PROOF_PRINT_NO","HOSPITAL_AREA_CODE","PATI_SEX","PATI_AGE","PATI_AGE_STRING","VISIT_BEGIN_DATE","VISIT_END_DATE","PAY_MODE","ADMISSION_DOCTOR","BIRTH_DATE","TRIAGE_STATUS","POOL_ID","RETURN_VISIT","TIME_QUANTUM","REK_ID","CURRENT_YEAR_ACCOUNT","OVER_YEAR_ACCOUNT","FUND_PAYMENT","EMERGENCY_FEE","ORG_INPUT_CODE","ORG_INPUT_NAME","DOCTOR_TREAT_TEAM_ID","COLLECTION","TRIAGE_NO","CARE_BABY_NO","COMMUNITY_FLAG","SICK_DATE","EMERGENCY_TYPE","INEMERGENCY_DATE","OUTEMERGENCY_DATE","HEIGHT","WEIGHT","REG_SORT_NO_STR","CURRENT_DOCTOR_ID","GREEN_CHANNEL_CODE","GUARANTEE_TYPE","EMERGENCY_BED","EMERGENCY_OPERATOR","GUARANTEE_NAME","REFERRAL","REFERRAL_REASON","GREEN_CHANNEL_TIME","NCOV_INFO" from PTS.OUTP_PATIENT_VISIT 
    where OUTP_VISIT_ID IS NULL'''
    # print(sql1)
    print(sql2)
    # querry_total.append(sql1)
    querry_total.append(sql2)
    querry_total.append(sql3)




def querry(qj1,num):
    for i in range(0,len(qj1)):
        print(qj1[i])
        with OracleSQLContextManager() as db_cursor:
            sql = qj1[i]
            db_cursor.execute(sql)
            result = db_cursor.fetchall()
            data1 = pd.DataFrame(result)
            # data1 = data1.fillna(0)
            data1.to_csv(r"C:\Users\CBH\Desktop\oracle\outp_visit\outp_visit_"+str(num)+".csv", index=None)
        with PgSQLContextManager() as pg_cursor:
            file_path = r"C:\Users\CBH\Desktop\oracle\outp_visit\outp_visit_"+str(num)+".csv"
            with open(file_path, 'r', encoding='utf-8') as f:
                insert_sql = """COPY ods.tmp_pts_outp_patient_visit FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
        escape '\t',
        header true,
        quote '"')"""
                pg_cursor.copy_expert(insert_sql, f)

# def querry2(qj2):
#     for i in range(0,len(qj2)):
#         print(qj2[i])
#         with OracleSQLContextManager() as db_cursor:
#             sql = qj2[i]
#             db_cursor.execute(sql)
#             result = db_cursor.fetchall()
#             data1 = pd.DataFrame(result)
#             # data1 = data1.fillna(0)
#             data1.to_csv(r"C:\Users\CBH\Desktop\oracle\outp_visit\outp_visit_2.csv", index=None)
#         with PgSQLContextManager() as pg_cursor:
#             file_path = r"C:\Users\CBH\Desktop\oracle\outp_visit\outp_visit_2.csv"
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 insert_sql = """COPY ods.tmp_pts_outp_patient_visit FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
#         escape '\t',
#         header true,
#         quote '"')"""
#                 pg_cursor.copy_expert(insert_sql, f)
#
# def querry3(qj3):
#     for i in range(0,len(qj3)):
#         print(qj3[i])
#         with OracleSQLContextManager() as db_cursor:
#             sql = qj3[i]
#             db_cursor.execute(sql)
#             result = db_cursor.fetchall()
#             data1 = pd.DataFrame(result)
#             # data1 = data1.fillna(0)
#             data1.to_csv(r"C:\Users\CBH\Desktop\oracle\outp_visit\outp_visit_3.csv", index=None)
#         with PgSQLContextManager() as pg_cursor:
#             file_path = r"C:\Users\CBH\Desktop\oracle\outp_visit\outp_visit_3.csv"
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 insert_sql = """COPY ods.tmp_pts_outp_patient_visit FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
#         escape '\t',
#         header true,
#         quote '"')"""
#                 pg_cursor.copy_expert(insert_sql, f)


# print(f'执行完成时间为：{(end_date-start_time).seconds}s')
if __name__ == '__main__':
    # p1 = multiprocessing.Process(target=querry1)
    # p2 = multiprocessing.Process(target=querry2)
    # p3 = multiprocessing.Process(target=querry3)
    # # 启动子进程
    # p1.start()
    # p2.start()
    # p3.start()
    n = 20
    list_result = [querry_total[i:i + n] for i in range(0, len(querry_total), n)]
    ag1 = [list_result[i] for i in range(0,5)]
    lst_finaly=[]
    ag2 = [i for i in range(1,6)]
    points_tulpe = list(zip(ag1, ag2))

    # for index,i in enumerate(ag1):
    #     print('('+str(i)+','+str(index+1)+')')
    #     lst_finaly.append('('+str(i)+','+str(index+1)+')')
    # for index,i in enumerate(ag1):
    #     print('({list},{index})'.format(list=i,index=index+1))
    #     lst_finaly.append(('({list},{index})'.format(list=i,index=index+1)).replace('\\',''))

    # for gg in lst_finaly:
    #     print(gg)
    # arg_lst = [(list_result[0],1),(list_result[1],2),(list_result[2],3),(list_result[3],4),(list_result[4],5),
    #            (list_result[5], 6),(list_result[6],7),(list_result[7],8),(list_result[8],9),(list_result[9],10),
    #            (list_result[10], 11), (list_result[11], 12), (list_result[12], 13), (list_result[13], 14), (list_result[14], 15),
    #            (list_result[15], 16), (list_result[16], 17), (list_result[17], 18), (list_result[18], 19), (list_result[19], 20),
    #            ]
    p_lst = []
    for arg in points_tulpe:
        print(arg)
        p = multiprocessing.Process(target=querry,args=arg)
        p.start()
        p_lst.append(p)

    for p in p_lst:
        p.join()
    end_date = dt.datetime.now()
    print("结束时间:%s" % end_date)

# for i in  querry_total:
#     sql = i
#     insert_q = '''INSERT INTO ods.tmp_pts_outp_patient_visit ("outp_visit_id","reg_sequence","patient_id","visit_id","pati_name","outp_date","outp_special_id","outp_special_name","outp_duration_code","dept_code","title_code","emp_no","outp_type_code","fee_flag","keep_flag","arrears_reason","reg_fee","reg_fee_code","checkups_fee","checkups_fee_code","fee","registry_flag","registry_resource","registering_time","operator","visit_type_code","charge_type_code","disease_type_code","reg_sort_no","master_or_atime_id","atime_flag","proof_print_no","hospital_area_code","pati_sex","pati_age","pati_age_string","visit_begin_date","visit_end_date","pay_mode","admission_doctor","birth_date","triage_status","pool_id","return_visit","time_quantum","rek_id","current_year_account","over_year_account","fund_payment","emergency_fee","org_input_code","org_input_name","doctor_treat_team_id","collection","triage_no","care_baby_no","community_flag","sick_date","emergency_type","inemergency_date","outemergency_date","height","weight","reg_sort_no_str","current_doctor_id","green_channel_code","guarantee_type","emergency_bed","emergency_operator","guarantee_name","referral","referral_reason","green_channel_time","ncov_info") VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''\
#     +i
#     print(insert_q)

