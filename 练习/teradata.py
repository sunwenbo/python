# import teradatasql
#
# with teradatasql.connect ('{"host":"192.168.10.5","user":"dbc","password":"dbc"}') as con:
#     with con.cursor () as cur:
#         cur.execute ("create volatile table voltab (c1 integer, c2 varchar(100)) on commit preserve rows")
#
#         cur.execute ("insert into voltab (?, ?)", [
#             [1, "abc"],
#             [2, "def"],
#             [3, "ghi"]])
#
#         cur.execute ("select * from voltab order by 1")
#         #[ print (row) for row in cur.fetchall () ]



import teradatasql
import pandas as pd

with teradatasql.connect(host='192.168.10.5', user='dbc', password='dbc') as connect:
    #data = pd.read_sql('select top 5 * from stella_test.order_info;', connect)
    with connect.cursor() as cur:
        for i in range(1,10000):
            sql = "insert into stella_test.test_data_csv VALUES(%d, 'Mike', 'James', '1980-01-05', '2005-03-27', 1)" % (i)
            #sql = "INSERT INTO stella_test.test_data_csv(CensusTract, State, County, TotalPop, Men, Women, Hispanic, White, Black, Native, Asian, Pacific, Citizen, Income, IncomeErr, IncomePerCap, IncomePerCapErr, Poverty, ChildPoverty, Professional, Service, Office, Construction, Production, Drive, Carpool, Transit, Walk, OtherTransp, WorkAtHome, MeanCommute, Employed, PrivateWork, PublicWork, SelfEmployed, FamilyWork, Unemployment) VALUES(1001020100	Alabama	Autauga	1948	940	1008	0	87	7	2	2	0	1223	-31412	31123	12123	15704	4554	8	34	17	21	11	15	90	4	0	0	2	2	25	943	77	18	4	0	5', 1001020100, 1001020100, 1001020100, 23236, 23236, 23236, 23236, 23236, 23236, 1001020100, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 23236, 1001020100, 23236, 23236, 23236, 23236, 23236)" % (i)
            cur.execute(sql)