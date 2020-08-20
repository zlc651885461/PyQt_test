"""
人员类:
    角色名称;
    操作任务;
    计划用时;
    完成时间记录;
    实际用时;

"""
import pickle as pk
import json

class Grade(object):

    def __init__(self,name):
        self.name = name

class Group(Grade):

    def __init__(self,name):
        self.name = name
        self.grade = None

class Person(Group):

    def __init__(self):
        self.name = None
        self.grade = None
        self.group = None
        self.work = None
        self.time_plan = None
        self.time_real = None
        self.time_cost = None
    def __str__(self):

        # strs = self.work[0]+"->完成时间:"+self.time_real[0]
        strs = dict(grade=self.grade,group=self.group,name=self.group,work=self.work,complete=self.time_real)
        return str(strs)

if __name__ == '__main__':
    per = Person()
    # task = Task()
    per.grade = '电气'
    per.group = '高配'
    per.name = 'A'
    per.work = ['能源中控室值班待命',]
    per.time_real = ['17:30:20',]
    # js = json.dumps(per)
