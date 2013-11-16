#!/usr/bin/env python

import sqlite3
import re

conn = sqlite3.connect(':memory:')


def parseFaculty():
    input_filename = "Faculty.txt"
    with open(input_filename, 'r') as f:
        raw_data = f.readlines()

    raw_data = [x.strip() for x in raw_data]  # strip newlines

    for row in raw_data:
        result = dict()
        record = row.split(',')
        record = [x.strip() for x in record]
        record[-1] = record[-1][:-1] # strip trailing period
        result['NAME'] = record[0]

        # some names are two words, some names are three
        some_names = result['NAME'].split(' ')
        if len(some_names) == 2:
            firstname = some_names[0]
            lastname = some_names[1]
            middlename = None
        elif len(some_names) == 3:
            (firstname, middlename, lastname) = some_names

        result['FIRSTNAME'] = firstname
        result['MIDDLENAME'] = middlename
        result['LASTNAME'] = lastname

        result['POSITION'] = record[1]

        # Some universities have a comma in their name,
        # because they are fundamentally bad people.
        index_of_year = 0
        for i in xrange(len(record)):
            if re.match('^\d+\.?$', record[i]):
                index_of_year = i
                break

        result['EDUCATION'] = ', '.join(record[2:index_of_year])
        result['YEAR'] = int(record[index_of_year])
        if index_of_year != len(record) - 1:
            result['INTERESTS'] = ", ".join(record[index_of_year + 1:])
        commit_faculty_row(result)


def parseCourse():
    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    input_filename = "Course.txt"
    with open(input_filename, 'r') as f:
        raw_data = f.readlines()

    raw_data = [x.strip() for x in raw_data]  # strip newlines
    records = chunks(raw_data, 3)

    name_re = r"^(.*?)\."
    hours_re = r"\((\d+)\)$"
    prereq_re = r"Prerequisite: (.*?)\."
    instructor_re = r"Instructor: (.*?)\.$"
    first_matcher = " ".join([name_re, hours_re])
    for record in records:
        result = dict()
        first_line = record[0]
        second_line = record[1]
        match = re.match(first_matcher, first_line)
        if match is not None:
            (name, hours) = match.groups()
            result['COURSE'] = name
            result['CREDIT HOURS'] = hours
        prereq_match = re.search(prereq_re, second_line)
        if prereq_match is not None:
            prereq_to_strip = prereq_match.group(0)
            second_line = second_line.replace(prereq_to_strip, '')
            result['REQUIREMENTS'] = prereq_match.group(1)
        else:
            result['REQUIREMENTS'] = None
        instructor_match = re.search(instructor_re, second_line)
        (result['FIRSTNAME'], result['MIDDLENAME'], result['LASTNAME']) = \
         (None, None, None)
        if instructor_match is not None:
            instructor_to_strip = instructor_match.group(0)
            second_line = second_line.replace(instructor_to_strip, '')
            instructor = instructor_match.group(1)
                        # some names are two words, some names are three
            some_names = instructor.split(' ')
            if len(some_names) == 1:
                result['FIRSTNAME'] = None
                result['MIDDLENAME'] = None
                result['LASTNAME'] = some_names[0]
            elif len(some_names) == 2:
                result['FIRSTNAME'] = some_names[0]
                result['LASTNAME'] = some_names[1]
                result['MIDDLENAME'] = None
            elif len(some_names) == 3:
                (firstname, middlename, lastname) = some_names
                result['FIRSTNAME'] = firstname
                result['MIDDLENAME'] = middlename
                result['LASTNAME'] = lastname

        result['DESCRIPTION'] = second_line
        commit_course_row(result)


def parsePhone():
    input_filename = "Phone.txt"
    with open(input_filename, 'r') as f:
        raw_data = f.readlines()

    raw_data = [x.strip() for x in raw_data]  # strip newlines
    raw_data = raw_data[1:]                   # remove the header line

    name_re = r"^(\w+, \w+)"
    office_re = r"(\w+ \d+\w?)"
    phone_re = r"(\d\-\d\d\d\d)"
    email_re = r"([\w\.@]+)$"
    matcher = " ".join([name_re, office_re, phone_re, email_re]) 
    for row in raw_data:
        match = re.match(matcher, row)
        if match is not None:
            (name, office, phone, email) = re.search(matcher, row).groups()
            firstname = None
            middlename = None
            lastname = None
            some_names = name.split(' ')
            if len(some_names) == 2:
                firstname = some_names[1]
                lastname = some_names[0][:-1]
                middlename = None
            elif len(some_names) == 3:
                (firstname, middlename, lastname) = some_names
                lastname = lastname[:-1]

            result = {'FIRSTNAME':firstname, 'MIDDLENAME':middlename, 'LASTNAME':lastname,
                      'OFFICE':office, 'PHONE':phone, 'EMAIL':email}
            commit_phone_row(result)


def parseOffice():
    input_filename = "Office.txt"
    with open(input_filename, 'r') as f:
        raw_data = f.readlines()

    raw_data = [x.strip() for x in raw_data]  # strip newlines
    raw_data = raw_data[:-1]                  # remove the header line

    name_re = r"^(.*?)"
    office_re = r"\(([\w \d]+)\)$"
    matcher = " ".join([name_re, office_re])

    gathering_hours = False
    hours = ""
    for row in raw_data:
        if not gathering_hours:
            gathering_hours = True
            match = re.match(matcher, row)
            if match is not None:
                (name, office) = match.groups()
            hours = ''
            (name, office) = match.groups()
            # some names are two words, some names are three
            firstname = None
            middlename = None
            lastname = None
            some_names = name.split(' ')
            if len(some_names) == 2:
                firstname = some_names[0]
                lastname = some_names[1]
                middlename = None
            elif len(some_names) == 3:
                (firstname, middlename, lastname) = some_names

        else:
            if row != '':
                hours += row + '\n'
            else:
                gathering_hours = False
                hours = hours.strip()
                result = {'FIRSTNAME':firstname, 'MIDDLENAME':middlename, 
                          'LASTNAME':lastname, 'OFFICE':office, 'HOURS':hours}
                commit_office_row(result)


def commit_faculty_row(row):
    payload = [row['FIRSTNAME'], row['MIDDLENAME'], row['LASTNAME'],
               row['POSITION'], row['EDUCATION'], row['YEAR']]
    if 'INTERESTS' in row:
        payload.append(row['INTERESTS'])
    else:
        payload.append(None);
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Faculty VALUES (?,?,?,?,?,?,?)", payload)
    conn.commit()


def commit_course_row(row):
    payload = [row['COURSE'], row['CREDIT HOURS'], row['DESCRIPTION'],
               row['REQUIREMENTS'], row['FIRSTNAME'], row['MIDDLENAME'],
               row['LASTNAME']]
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Course VALUES (?,?,?,?,?,?,?)", payload)
    conn.commit()


def commit_phone_row(row):
    payload = [row['FIRSTNAME'], row['MIDDLENAME'], row['LASTNAME'],
               row['OFFICE'], row['PHONE'], row['EMAIL']]
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Phone VALUES (?,?,?,?,?,?)", payload)
    conn.commit()


def commit_office_row(row):
    payload = [row['FIRSTNAME'], row['MIDDLENAME'], row['LASTNAME'],
               row['OFFICE'], row['HOURS']]
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Office VALUES (?,?,?,?,?)", payload)
    conn.commit()


def create_tables():
    OfficeTable = '''CREATE TABLE Office 
                     (FIRSTNAME text NOT NULL,
                      MIDDLENAME text,
                      LASTNAME text NOT NULL,
                      OFFICE text NOT NULL,
                      HOURS text)'''
    PhoneTable  = '''CREATE TABLE Phone
                     (FIRSTNAME text NOT NULL,
                      MIDDLENAME text,
                      LASTNAME text NOT NULL COLLATE NOCASE,
                      OFFICE text NOT NULL,
                      PHONE text NOT NULL,
                      EMAIL text NOT NULL)'''
    FacultyTable  = '''CREATE TABLE Faculty
                       (FIRSTNAME text NOT NULL,
                        MIDDLENAME text,
                        LASTNAME text NOT NULL COLLATE NOCASE,
                        POSITION text NOT NULL, 
                        EDUCATION text NOT NULL, 
                        YEAR integer, 
                        INTERESTS text)'''
    CourseTable  = '''CREATE TABLE Course
                      (COURSE text PRIMARY KEY,
                       CREDITHOURS integer NOT NULL,
                       DESCRIPTION text NOT NULL, 
                       REQUIREMENTS text,
                       FIRSTNAME text,
                       MIDDLENAME text,
                       LASTNAME text COLLATE NOCASE)'''
    c = conn.cursor()
    for table in [OfficeTable, PhoneTable, FacultyTable, CourseTable]:
        c.execute(table)
    conn.commit()


def query1():
    query = '''SELECT FIRSTNAME, MIDDLENAME, LASTNAME, OFFICE 
               FROM Office'''
    with open('query1.out', 'w') as f:
        for row in conn.execute(query):
            if row[1] is None:
                output = "%s %s, %s" % (row[0], row[2], row[3])
            else:
                output = "%s %s %s, %s" % row
            f.write(output + "\n")


def query2():
    query = '''SELECT FIRSTNAME, MIDDLENAME, LASTNAME, OFFICE 
               FROM Office'''
    with open('query2.out.html', 'w') as f:
        for row in conn.execute(query):
            if row[1] is None:
                output = "<b>%s %s</b>, <i>%s</i><br>" % (row[0], row[2], row[3])
            else:
                output = "<b>%s %s %s</b>, <i>%s</i><br>" % row
            f.write(output + "\n")


def query3():
    with open('query3.out', 'w') as f:
        query = """SELECT f.FIRSTNAME, f.LASTNAME, p.EMAIL, f.INTERESTS
                   FROM Faculty AS f, Phone AS p 
                   ON f.FIRSTNAME = p.FIRSTNAME AND f.LASTNAME = p.LASTNAME
                   WHERE f.POSITION = 'Assistant Professor' AND f.YEAR > 1990"""
        for row in conn.execute(query):
            output = "%s %s, %s\n%s\n\n" % row
            f.write(output)


def query4():
    with open('query4.out', 'w') as f:
        query = """SELECT f.FIRSTNAME, f.LASTNAME, f.POSITION, 
                          f.INTERESTS, c.COURSE
                   FROM Faculty AS f, Course AS c
                   ON  f.LASTNAME = c.LASTNAME
                   WHERE f.INTERESTS LIKE '%artificial intelligence%' 
                      OR f.INTERESTS LIKE '%databases%'"""
        for row in conn.execute(query):
            output = "%s %s, %s, %s\n%s\n\n" % row
            f.write(output)

def query5():
    # Profs who do office hours by appointment
    with open('query5.out', 'w') as f:
        query = """SELECT f.FIRSTNAME, f.LASTNAME
                   FROM Faculty AS f, Office AS o
                   ON f.LASTNAME = o.LASTNAME
                   WHERE o.HOURS LIKE '%by appointment%'"""
        for row in conn.execute(query):
            output = "%s %s\n" % row
            f.write(output)

def query6():
    # Phone numbers of profs who teach classes
    with open('query6.out', 'w') as f:
        query = """SELECT DISTINCT p.FIRSTNAME, p.PHONE
                   FROM Phone as p, Course as c
                   ON p.LASTNAME = c.LASTNAME"""
        for row in conn.execute(query):
            output = "%s %s\n" % row
            f.write(output)


def main():
    create_tables()
    parseFaculty()
    parseCourse()
    parsePhone()
    parseOffice()

    query1()
    query2()
    query3()
    query4()
    query5()
    query6()


if __name__ == "__main__":
    main()