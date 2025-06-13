# KIERAN WHITE - DIRECT ACCESS TABLE - CS 110A

""" UNDERSTAND:

Given a student ID and list, create an algorithm to access the given student's
information as productively as possible.


inputs: student ID, student information list
output: specific student information dependent on the ID number
match: min/max/mean assignment, digit swap assignment

    PLAN:
1. Isolate the student ID index through %
2. Call student information through the newly found index
"""

#ALGORITHM:
#1 - isolate the index - index - student_id % 10000
#2 - call the students information - return f'{records[index]}'

#SAMPLE OUTPUT:
#Enter Student ID: 10012
#[10012, '05/21/2001', 'May', 'CS']

#RUN TIME:
#O(1)

#SPACE:
#O(n)

def calculate_student_info(student_id, records):
    """Calculates the index of a given student ID"""
    index = student_id % 10000
    records.insert(0, index)


def main():
    student_id = int(input('Enter Student ID: '))

    records = [[10000, "11/21/2002", "Jack", "CS"], [10001, "11/29/2003", "Jill", "CS"],
               [10002, "5/01/2006", "Ken", "CNIT"], [10003, "10/20/2001", "Ben", "PHYC"],
               [10004, "09/05/2000", "Jen", "CS"], [10005, "10/31/2002", "Jon", "CS"],
               [10006, "01/21/2000", "Ron", "MAT"], [10007, "11/29/2002", "Jack", "CNIT"],
               [10008, "12/11/2001", "Kat", "CNIT"], [10009, "12/21/2005", "Ana", "CS"],
               [10010, "01/25/2005", "Nina", "CS"], [10011, "03/24/2004", "Ben", "CNIT"],
               [10012, "05/21/2001", "May", "CS"], [10013, "8/27/2003", "Fe", "CS"],
               [10014, "11/21/2000", "Bill", "CS"], [10015, "11/21/2002", "Max", "CS"],
               [10016, "06/24/2003", "Pat", "CNIT"], [10017, "10/11/2000", "Kuma", "CS"],
               [10018, "03/21/2006", "Lily", "CS"], [10019, "12/21/2002", "Suz", "CS"]]

    calculate_student_info(student_id, records)
    print(records[0])


if __name__ == '__main__':
    main()





