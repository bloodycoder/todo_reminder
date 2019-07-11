from prettytable import PrettyTable
import os
def get_joblist():
    pwd = '/Users/apple/Desktop/pythonCode/credit/'
    welcome_info = PrettyTable(["command id","command name"])
    welcome_info.align["command id"] = 'l'
    welcome_info.align["command name"] = 'l'
    welcome_info.padding_width = 2
    welcome_info.add_row(["1","add job"])
    welcome_info.add_row(["2","finish a job"])
    welcome_info.add_row(["3","apply time for fun"])
    welcome_info.add_row(["4","job list"])
    welcome_info.add_row(["q","quit"])
    f = open(pwd+'data/score')
    score = int(f.read())
    f.close()
    os.system('clear')
    x = 4
    f = open(pwd+'data/job')
    jobs = f.readlines()
    if(jobs[len(jobs)-1][-1]!='\n'):
        jobs[len(jobs)-1] = jobs[len(jobs)-1] +'\n'
    f.close()
    return jobs