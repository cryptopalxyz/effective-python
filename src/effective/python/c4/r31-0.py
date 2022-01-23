# -*- coding: utf-8 -*-

from weakref import WeakKeyDictionary


class Grade(object):
    def __init__(self):
        # _value will always make a copy of the reference that could cause memory leak
        # WeakKeyDictionary will fix it
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 200')
        self._value = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99

# OK for one instance
print('Writing', first_exam.writing_grade )
print('Science', first_exam.science_grade )


second_exam = Exam()
second_exam.writing_grade = 75

# the second overwrite the first one because there is only one Grade instance
# need to use a dict to save the Grade instances
print('First', first_exam.writing_grade, 'is Wrong')
print('Second', second_exam.writing_grade, 'is right')

# same as
print('First', Exam.__dict__['writing_grade'].__get__(first_exam, Exam), 'is Wrong')
print('Second', Exam.__dict__['writing_grade'].__get__(second_exam, Exam), 'is right')