# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print "My name is %s" % self.name

tak = Person("Takuya")
print tak.name
tak.greet()
