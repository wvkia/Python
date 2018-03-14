class Student(object):
    def __init__(self,name,score):
        self.__name=name    #属性的“__XX”表示为私有属性
        self.__score=score
    def print_score(self):
        print('%s : %s ' % (self.__name,self.__score))

bart=Student('aa',89)
bart.print_score()