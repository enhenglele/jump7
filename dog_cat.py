class Dog(object):
    def __init__(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name=value
    def say(self):
        print(self._name+'is making sound wang wang wang....')
class Cat(object):
    def __init__(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name=value
    def say(self):
        print(self._name+'is making sound miu miu miu....')