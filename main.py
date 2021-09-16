# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import pymysql


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


def print_test(name):
    # Use a breakpoint in the code line below to debug your script.
    print("test, {0}".format(name))


def query_db(name):
    connect = pymysql.connect(
        host="10.1.2.148",
        user='root',
        password='tienssysroot',
        database='lark_order'
    )
    cursor = connect.cursor()
    sql = "select * from trd_order limit 1"
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)

    cursor.close()
    connect.commit()
    connect.close()
    print("sql success")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    query_db("aa")
    # print_test("aaa")
    # for i in range(1,5):
    #     for j in range(1,5):
    #         for g in range(1,5):
    #             if(i != j) and (i != g) and (j != g):
    #                 print (i,j,g)
    # cars = ['bmw', 'audi', 'toyota', 'subaru']
    # print(cars)
    # cars.reverse()
    # print(cars)
    # numbers = list(range(1,6))
    # print numbers
    # squares = []
    # for value in range(1,11):
    #     square = value**2
    #     squares.append(square)
    #
    # print squares
    # print(max(squares))
    # print(min(squares))
    # maxnum = max(squares)
    # if maxnum == 100:
    #     print ("hello")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
