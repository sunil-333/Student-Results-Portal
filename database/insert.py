import sqlite3
from datetime import datetime

from .create import createResultsTable, createStudentsTable, createSubjectsTable
from .heplers import (getNextIndexOfData, parseCSV, parseTableName,
                      stripEmptyCells)


def insertResultsValues(data, tableName, con):
    insertSQL = f'''INSERT INTO {tableName} values {tuple(data)}'''

    cur = con.execute(insertSQL)
    con.commit()


def insertStudentValues(tableName, rollno, name, sgpa, con):
    insertSQL = f'INSERT INTO {tableName}_students values ("{rollno}", "{name}", "{sgpa}")'

    cur = con.cursor()
    try:
        cur.execute(insertSQL)
        con.commit()
    except:
        # Already exists
        pass


def insertSubjectValues(tableName, subjectCode, subjectName, con):
    insertSQL = f'''INSERT INTO {tableName}_subjects VALUES (
        "{subjectCode}", "{subjectName}")'''

    cur = con.cursor()
    try:
        cur.execute(insertSQL)
        con.commit()
    except:
        # Already exists
        pass


def insertMetadataValues(tableName, con):
    cur = con.cursor()
    countSQL = 'SELECT sno FROM metadata ORDER BY sno DESC LIMIT 1'
    cur.execute(countSQL)
    count = cur.fetchone()
    count = count[0] + 1 if count else 1

    date = datetime.now().strftime(r'%d-%m-%Y')
    insertSQL = f'''INSERT INTO metadata VALUES (
        "{count}", "{date}", "{tableName}")'''
    cur = con.cursor()
    cur.execute(insertSQL)
    con.commit()


def insertResultsData(data: list, tableName, con):
    subjects = set()

    index = getNextIndexOfData(data)
    while index < len(data):
        row = stripEmptyCells(data[index])
        name, rollno = row[1], row[3]

        j = index + 2
        while data[j][0] != 'SGPA':
            subjects.add((data[j][0], data[j][1]))
            row = data[j][:9]
            row = [rollno] + row[:1] + row[2:]
            insertResultsValues(row, tableName, con)
            j += 1

        sgpa = stripEmptyCells(data[j])[-1]
        insertStudentValues(tableName, rollno, name, sgpa, con)

        index = getNextIndexOfData(data, j)

    if len(subjects):
        addSubjects(tableName, subjects, con)


def insertNewCSV(tableName, fileName):

    con = sqlite3.connect('results.db')

    insertMetadataValues(tableName, con)

    createResultsTable(tableName, con)
    createStudentsTable(tableName, con)
    createSubjectsTable(tableName, con)

    insertResultsData(parseCSV(fileName), tableName, con)

    return parseTableName(tableName)


def addSubjects(tableName, data, con):
    for subjectCode, subjectName in data:
        insertSubjectValues(tableName, subjectCode, subjectName, con)
