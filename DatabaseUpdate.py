import pymysql

passwd = input("데이터베이스의 비밀번호를 입력\n")

conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = passwd)
    
cur = conn.cursor()
cur.execute("show databases")
rows = cur.fetchall()


_list = []
for index in rows:
    _list.append(index[0]) # tuple값은 수정이 안되니 리스트로 집어넣어주자

dbexe = input("Project DB에 수정할 명령어 입력 \n")
for row in _list:
    if 'project' in row: # 리스트에 넣은 값 중 project 스트링이 있는것만 골라서 넣자
        cur.execute("use %s;" % row)
        cur.execute(dbexe)
        print(row, "Finish")
