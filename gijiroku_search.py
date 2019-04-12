import mysql.connector

if __name__ == '__main__':
    # データベースに接続
    connect = mysql.connector.connect(user='hoge', password='hoge', host='hoge', database='hoge', charset='utf8')
    cursor = connect.cursor()

    name = '山田太郎'
    sex = '男'

    # insert
    cursor.execute('insert into student_table (name, sex) values (%s, %s)', (name, sex))

    # select
    cursor.execute('select * from student_table')
    row = cursor.fetchone()

    # 出力
    for i in row:
        print(i)

    # データベースから切断
    cursor.close()
    connect.close()