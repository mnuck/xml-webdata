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
        instructor_match = re.search(instructor_re, second_line)
        if instructor_match is not None:
            instructor_to_strip = instructor_match.group(0)
            second_line = second_line.replace(instructor_to_strip, '')
            result['INSTRUCTOR'] = instructor_match.group(1)
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
            result = {'FACULTY':name, 'OFFICE':office,
                      'PHONE':phone, 'EMAIL':email}
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
        else:
            if row != '':
                hours += row + '\n'
            else:
                gathering_hours = False
                hours = int(hours.strip())
                result = {'FACULTY':name, 'OFFICE':office, 'HOURS':hours}
                commit_office_row(result)


def commit_faculty_row(row):
    payload = [row['NAME'], row['POSITION'],
               row['EDUCATION'], row['YEAR']]
    if 'INTERESTS' in row:
        payload.append(row['INTERESTS'])
    else:
        payload.append(None);
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Faculty VALUES (?,?,?,?,?)", payload)
    conn.commit()


def commit_course_row(row):
    payload = [row['COURSE'], row['CREDIT HOURS'], row['DESCRIPTION']]
    if 'REQUIREMENTS' in row:
        payload.append(row['REQUIREMENTS'])
    else:
        payload.append(None);
    if 'INSTRUCTOR' in row:
        payload.append(row['INSTRUCTOR'])
    else:
        payload.append(None);        
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Faculty VALUES (?,?,?,?,?)", payload)
    conn.commit()


def commit_phone_row(row):
    payload = [row['FACULTY'], row['OFFICE'],
               row['PHONE'], row['EMAIL']]
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Phone VALUES (?,?,?,?)", payload)
    conn.commit()


def commit_office_row(row):
    payload = [row['FACULTY'], row['OFFICE'], row['HOURS']]
    payload = tuple(payload)
    c = conn.cursor()
    c.execute("INSERT INTO Office VALUES (?,?,?)", payload)
    conn.commit()


def create_tables():
    OfficeTable = '''CREATE TABLE Office 
                     (FACULTY text PRIMARY KEY,
                      OFFICE text NOT NULL,
                      HOURS text)'''
    PhoneTable  = '''CREATE TABLE Phone
                     (FACULTY text PRIMARY KEY,
                      OFFICE text NOT NULL,
                      PHONE text NOT NULL,
                      EMAIL text NOT NULL)'''
    FacultyTable  = '''CREATE TABLE Faculty
                       (NAME text PRIMARY KEY,
                        POSITION text NOT NULL, 
                        EDUCATION text NOT NULL, 
                        YEAR integer, 
                        INTERESTS text)'''
    CourseTable  = '''CREATE TABLE Course
                      (COURSE text PRIMARY KEY,
                       CREDITHOURS integer NOT NULL,
                       DESCRIPTION text NOT NULL, 
                       REQUIREMENTS text,
                       INSTRUCTOR text)'''
    c = conn.cursor()
    for table in [OfficeTable, PhoneTable, FacultyTable, CourseTable]:
        c.execute(table)


def main():
    create_tables()
    parseFaculty()
    parseCourse()
    parsePhone()


if __name__ == "__main__":
    main()