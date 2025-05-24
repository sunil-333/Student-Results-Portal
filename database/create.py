import sqlite3


def createResultsTable(tableName, con):
    cur = con.cursor()
    createSQL = f'''CREATE TABLE {tableName} (
        rollno text,
        subject_code text,
        internal integer,
        external integer,
        total integer,
        result_status text,
        credits integer,
        grades text,
        grade_points integer
    )'''
    cur.execute(createSQL)
    con.commit()


def createStudentsTable(tableName, con):
    createSQL = f'''CREATE TABLE {tableName}_students (
        rollno text PRIMARY KEY,
        name text,
        sgpa text
    )'''

    cur = con.cursor()
    cur.execute(createSQL)
    con.commit()


def createSubjectsTable(tableName, con):
    createSQL = f'''CREATE TABLE {tableName}_subjects (
        subject_code text PRIMARY KEY,
        subject_name text
    )'''

    cur = con.cursor()
    cur.execute(createSQL)
    con.commit()


def createMetadataTable(con):
    createSQL = '''CREATE TABLE metadata(
        sno integer PRIMARY KEY,
        date text,
        name text NOT NULL UNIQUE
    )'''
    cur = con.cursor()
    cur.execute(createSQL)
    con.commit()


# def createBranchesTable(con):
#     createSQL = '''CREATE TABLE branches (
#         branch_code text PRIMARY KEY,
#         branch_name text
#     )'''

#     cur = con.cursor()
#     cur.execute(createSQL)
#     con.commit()


def createAllTables():
    con = sqlite3.connect('results.db')

    # createStudentTable(con)
    # createSubjectTable(con)
    createMetadataTable(con)
    # createBranchesTable(con)


if __name__ == '__main__':
    createAllTables()
