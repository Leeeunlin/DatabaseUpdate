import pymysql

conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = "hyena!!")
    
cur = conn.cursor()
cur.execute("show databases")
rows = cur.fetchall()


_list = []
for index in rows:
    _list.append(index[0])

dbexe = input("Project DB에 수정할 명령어 입력 \n")
for row in _list:
    if 'project' in row:
        cur.execute("use %s;" % row)
        cur.execute(dbexe)
        print(row, "Finish")
