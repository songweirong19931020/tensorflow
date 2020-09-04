# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    account
   Description :
   Author :       CBH
   date：         2020/5/23 14: 32
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/23 14: 32:
-------------------------------------------------
"""
import psycopg2
import traceback
from sbh.gshj.util.LogUitl import Logger
class PgSQLContextManager:
    """
    pgsQL Context Manager
    """
    def __init__(self, host="192.168.12.106", port=5432, user="postgres", password="postgres", database="postgres"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        """
        上文管理器 返回的结果 会被赋给as 关键字之后的变量
        :return: cursor
        """
        try:
            self.db_conn = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                           database=self.database)
            self.cursor = self.db_conn.cursor()
            return self.cursor
        except Exception as e:
            traceback.print_exc()
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        下文管理器 选择性地处理包装代码块中出现的异常
        :param exc_type: 异常类型 默认为 None,发生异常,参数被填充
        :param exc_val: 异常实例 默认为 None,发生异常,参数被填充
        :param exc_tb: 异常回溯 默认为 None,发生异常,参数被填充
        :return:
        """
        try:
            if exc_type:
                self.db_conn.rollback()
                # 返回False 传播异常
                # 返回True 终止异常 不要这么做
                # 抛出不同的异常 代替 原有异常
                return False
            else:
                self.db_conn.commit()
        except Exception as e:
            raise e
        finally:
            self.cursor.close()
            self.db_conn.close()


if __name__ == '__main__':
    # 根据实际,传入数据库参数
    from sbh.gshj.util.Time_Util import *
    with PgSQLContextManager() as db_cursor:
        today = Get_Day()
        yesterday = (today - datetime.timedelta(days=1)).strftime("%Y%m%d")
        first = today.replace(day=1)
        last_month = (first - datetime.timedelta(days=1)).strftime("%Y%m")
        mon_id = last_month
        #取前两个月日期

        first_2= today.replace(month=int(time.strftime("%m", time.localtime()))-2)
        fist_1= first_2.replace(day=1).strftime("%Y%m%d")
        #mon_id = (datetime.date.today() - relativedelta(months=+1)).strftime("%Y%m")
        select_sql = """
        delete from his_bi.dw_outp_patient_amount_m where month_id = '{mon_id}';
        insert into his_bi.dw_outp_patient_amount_m
select
                '{mon_id}' as month_id,
        t1.patient_id,
        t1.visit_id,
        sum(case when t1.key='D00014' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as total_fees,
        sum(case when t1.key='D00017' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as pham_fees,
        sum(case when t1.key='D00015' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as service_fess,
        sum(case when t1.key='D00016' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as material_fees,
        sum(case when t1.key='D00018' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as inspect_fees,
        sum(case when t1.key='D00019' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as check_fees,
        sum(case when t1.key='D00020' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as cur_fees,
        sum(case when t1.key='D00021' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as examination_fees,
        sum(case when t1.key='D00022' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as western_fees,
        sum(case when t1.key='D00023' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as chinese_patent_fees,
        sum(case when t1.key='D00024' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as herb_fees,
        sum(case when t1.key='D00025' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as anti_pham_fees,
        sum(case when t1.key='D00026' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as support_fess,
        sum(case when t1.key='D00027' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as basic_fess,
        sum(case when t1.key='D00028' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as key_point_fess,
        sum(case when t1.key='D00029' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as non_res_fess,
        sum(case when t1.key='D00030' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as res_fess,
        sum(case when t1.key='D00031' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as special_fess,
        sum(case when t1.key='D00145' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as tj_fess,
        sum(case when t1.key='D00146' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as nurse_fess,
        sum(case when t1.key='D00147' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as operation_fess,
        sum(case when t1.key='D00148' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as tdsp_fess,
        sum(case when t1.key='D00149' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as yntj_fess,
        sum(case when t1.key='D01001' and d1.month_id='{mon_id}' then t1.value else 0 end  ) as other_fees
    from his_bi.dwd_outp_income_d t1 
    left join his_bi.dim_date_info d1 on t1.st_date = d1.day_id and d1.month_id = '{mon_id}'
   where 1=1
     and t1.key in('D00014','D00017','D00015','D00016','D00017','D00015','D00016','D00018',
        'D00019','D00020','D00021','D00022','D00023','D00024','D00025','D00026','D00027','D00028',
        'D00029','D00030','D00031','D00145','D00146','D00147','D00148','D00149','D01001')
     and d1.month_id = '{mon_id}'
   group by
        t1.patient_id,
        t1.visit_id
        """.format(mon_id=mon_id)
        # 执行SQL语句 返回影响的行数
        print(select_sql)
        db_cursor.execute(select_sql)
        # 返回执行结果
        result = db_cursor.fetchall()
        print(result)