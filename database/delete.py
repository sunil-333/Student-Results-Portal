from .query import getTableName
from .heplers import parseTableName


def deleteMetadataEntry(con, tableSno):
    deleteSQL = f'DELETE FROM metadata WHERE sno={tableSno}'

    try:
        cur = con.cursor()
        cur.execute(deleteSQL)
        con.commit()
    except:
        pass


def deleteResultsTable(con, tableName):
    dropSQL = f'DROP TABLE {tableName}'

    try:
        cur = con.cursor()
        cur.execute(dropSQL)
        con.commit()
    except:
        pass


def deleteStudentsTable(con, tableName):
    dropSQL = f'DROP TABLE {tableName}_students'

    try:
        cur = con.cursor()
        cur.execute(dropSQL)
        con.commit()
    except:
        pass


def deleteSubjectsTable(con, tableName):
    dropSQL = f'DROP TABLE {tableName}_subjects'

    try:
        cur = con.cursor()
        cur.execute(dropSQL)
        con.commit()
    except:
        pass


def deleteAllTables(con, tableName, tableSno):

    if tableSno:
        deleteMetadataEntry(con, tableSno)
        deleteResultsTable(con, tableName)
        deleteSubjectsTable(con, tableName)
        deleteStudentsTable(con, tableName)

    return parseTableName(tableName)
