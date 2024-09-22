#!/usr/bin/env

import sys

#Task 1

def q1_sum(s):
    output = 0
    for w in s:
        for n in w:
            if int(n) % 2 == 0:
                output += int(n)
    print (output)

#Task 2

def move_vow(s):
    vowels = "aeiouAEIOU"
    output = ""
    consonants = ""
    for ch in s:
        if ch in vowels:
            output += ch
        else:
            consonants += ch
    print (output + consonants)

#Task 3

class Memories(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def remember(self, s):
        print (getattr(self, s, False))

#Task 4

class Test(object):

    def __init__(self, subject_name, correct_answers, passing_mark):
        self.subject_name = subject_name
        self.correct_answers = correct_answers
        self.passing_mark = passing_mark

class Student(object):

    def __init__(self, name):
        self.name = name

    def take_test(self, Test, answers):
        max = len(answers)
        score = 0
        for an in answers:
            if an in Test.correct_answers:
                score += 1
        total = float((score / max) * 100)
        if total >= int(Test.passing_mark.strip("%")):
            print (f"{self.name} passed the {Test.subject_name} Test with the score {total}%")
        else:
            print (f"{self.name} failed the {Test.subject_name} Test")

#Task 5

def histogram(ls, char):
    for s in ls:
        print(int(s) * char)
    return 0

#Task 6

def filter_star(dict, int):
    output = "No result found!"
    for k, v in dict.items():
        if len(v) == int:
            output = f"{{'{k}':'{v}'}}"
    return 0