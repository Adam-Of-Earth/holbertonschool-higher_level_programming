#!/usr/bin/python3
"""script to filter states"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    sname = argv[4]

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=dbname)

    cur = database.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name \
        LIKE BINARY '{}' ORDER BY id ASC".format(sname))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()
