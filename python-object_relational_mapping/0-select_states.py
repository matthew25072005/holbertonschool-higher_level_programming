#!/usr/bin/python3
"""
    script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query to retrieve states sorted by ID
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

        # Close the database connection
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()