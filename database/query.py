from math import ceil

from .heplers import parseTableName


def getName(con, rollno, tableName):
    cur = con.cursor()
    # SQL = f'SELECT name FROM {tableName} WHERE rollno="{rollno}"'
    SQL = f'SELECT name FROM {tableName}_students WHERE rollno="{rollno}"'

    cur.execute(SQL)
    return cur.fetchone()[0]


def getSubjectName(con, subjectCode, tableName):
    cur = con.cursor()
    SQL = f'''SELECT subject_name FROM {tableName}_subjects WHERE
            subject_code="{subjectCode}"'''

    cur.execute(SQL)
    return cur.fetchone()[0]


def getSGPA(con, rollno, tableName):
    cur = con.cursor()
    sql = f'SELECT sgpa FROM {tableName}_students WHERE rollno="{rollno}"'
    cur.execute(sql)
    return cur.fetchone()[0]


def getMarks(con, rollno, tableName):
    cur = con.cursor()
    SQL = f'''SELECT
        subject_code,
        internal,
        external,
        total,
        result_status,
        credits,
        grades,
        grade_points from {tableName} WHERE rollno="{rollno}"'''

    index = 1
    totalMarks = 0
    totalCredits = 0

    output = []
    creditsList = []
    gradePoints = []
    for row in cur.execute(SQL):
        row = list(row)
        row.insert(1, getSubjectName(con, row[0], tableName))
        creditsList.append(row[6])
        gradePoints.append(row[8])

        try:
            totalMarks += row[4]
        except:
            pass
        totalCredits += row[6]

        row.insert(0, index)
        output.append(row)
        index += 1

    res = {
        'maxMarks': (index - 1) * 100,
        'totalMarks': totalMarks,
        'totalCredits': totalCredits,
        'sgpa': getSGPA(con, rollno, tableName)
    }
    output.append(res)

    if len(output) == 1:
        raise Exception('No result found')

    return output


def getResultsListCount(con):
    sql = 'SELECT COUNT(*) FROM metadata'

    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]


def getResultsPageNavList(con, perPage, page):
    pages = ceil(getResultsListCount(con) / perPage)
    pages = 1 if not pages else pages

    res = [1]

    if page > 1:
        res.append(None)
        res.append(page)

    if page + 1 < pages:
        res.append(page+1)

    if res[-1] != pages:
        res.append(None)
        res.append(pages)

    return res if len(res) != 1 else []


def getResultsList(con, page, perPage):
    cur = con.cursor()

    count = getResultsListCount(con)
    pages = count // perPage  # this is the number of pages
    offset = (page-1)*perPage  # offset for SQL query

    sql = f'''SELECT * FROM metadata ORDER BY sno DESC LIMIT {perPage}
             OFFSET {offset}'''

    res = []
    for row in cur.execute(sql):
        res.append([*row[:2], parseTableName(row[2])])
    return res


def getTableName(sno, con):
    sql = f'SELECT name FROM metadata WHERE sno={sno}'
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]


def getBranchName(roll):

    branches = {
        '1A01': 'Civil Engineering',
        '1A02': 'Electrical and Electronics Engineering',
        '1A03': 'Mechanical Engineering',
        '1A04': 'Electronics and Communication Engineering',
        '1A05': 'Computer Science and Engineering',
        '1A12': 'Information Technology',
        '1A33': 'Artificial Intelligence & Machine Learning',
        '1A32': 'Data Science',
        '1A35': 'IOT',
        '1A36': 'Cyber Security',
        '1D87': 'Advanced Manufacturing Systems',
        '1D58': 'Computer Science and Engineering',
        '1D82': 'Power Systems',
        '1D57': 'VLSI Design',



    }

    branchCode = roll[4:8]
    return branches.get(branchCode)
