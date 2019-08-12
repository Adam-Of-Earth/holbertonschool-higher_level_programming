#!/usr/bin/python3
"""list all states from a dateabase"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               password=password,
                               db=dbname)
    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    cur.close()
    database.close()
