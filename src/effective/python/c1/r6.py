# -*- coding: utf-8 -*-

class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grades(self, name):
        grades = self._grades[name]
        return sum(grades)/len(grades)

book = SimpleGradebook()
book.add_student('tod')
book.report_grade('tod', 90)
print(book.average_grades('tod'))

import collections
Grade = collections.namedtuple('Grade', ('score'))

class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(Grade(score))

    def average_grades(self, name):
        sum_score = 0
        for grade in self._grades:
            sum_score += grade.score
        return sum_score/len(self.grades)
