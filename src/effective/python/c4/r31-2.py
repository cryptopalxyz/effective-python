# -*- coding: utf-8 -*-

from weakref import WeakKeyDictionary


class Grade(object):
    def __init__(self):
        # _value will always make a copy of the reference that could cause memory leak
        # WeakKeyDictionary will fix it
        self._value = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._value.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 200')
        self._value[instance] = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75

print('First', first_exam.writing_grade, 'is right')
print('Second', second_exam.writing_grade, 'is right')
print(first_exam.__dict__)
# same as
print('First', first_exam.__dict__['writing_grade'], 'is right')
print('Second', second_exam.__dict__['writing_grade'], 'is right')