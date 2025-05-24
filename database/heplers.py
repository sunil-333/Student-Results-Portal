def parseCSV(filename):
    with open(filename) as file:
        res = []
        for line in file:
            res.append(list(map(str.strip, line.split(','))))
        return res


def stripEmptyCells(row: list):
    return [i for i in row if i]


def getBranchName(roll):

    branches = {
        '01': 'Civil Engineering',
        '02': 'Electrical and Electronics Engineering',
        '03': 'Mechanical Engineering',
        '04': 'Electronics and Communication Engineering',
        '05': 'Computer Science and Engineering',
        '12': 'Information Technology',
        '33': 'Artificial Intelligence & Machine Learning',
        '06': 'Data Science',
        '07': 'Cyber Security',
    }

    branchCode = roll[6:8]
    return branches[branchCode]


def parseTableName(name):
    name = name.split('_')[1:]
    course = None
    if name[0] == 'btech':
        course = 'B.Tech'
    elif name[0] == 'mtech':
        course = 'M.Tech'
    else:
        course = name[0].upper()

    exam = name[4].title()
    if name[4] == 'both':
        exam = 'Regular & Supplementary'

    res = f'{course} {name[1]} Year {name[2]} Semester ({name[3]}) {exam} '
    res += f'Examinations, {name[5]} {name[6]}'
    return res


def getNextIndexOfData(data: list, start=0):
    index = start

    while index < len(data):
        if data[index][0].startswith('Name'):
            break
        index += 1

    return index
