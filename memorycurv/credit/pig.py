from prettytable import PrettyTable
import os
def main():
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
    while(1):
    	f = open(pwd+'data/score')
    	score = int(f.read())
    	f.close()
        os.system('clear')
        print welcome_info
    	try:
    	    x = raw_input()
            if(x=='q'):
                return 0
            x = int(x)
    	    if(x<0 or x>4):
    	    	print('please input a number between 1 and 3')
    	    	continue;
    	    f = open(pwd+'data/job')
    	    jobs = f.readlines()
            if(jobs[len(jobs)-1][-1]!='\n'):
                jobs[len(jobs)-1] = jobs[len(jobs)-1] +'\n'
    	    f.close()
            if(x == 4):
                os.system('clear')
                print('............job_list...........')
                joblist_info = PrettyTable(["job id","job name","credit"])
                joblist_info.align['job id'] = 'l'
                joblist_info.align['job name'] = 'l'
                joblist_info.align['credit'] = 'l'
                for i in range(len(jobs)):
                    x = jobs[i].split(',')
                    if(x[0]>30):
                        x[0] = x[0][0:30]
                    joblist_info.add_row([i+1,x[0],x[1]])
                print joblist_info
                raw_input()
                print('............job_list...........')
    	    if(x == 1):
    	    	job_name = raw_input("please tell me the job name.")
    	    	job_credit = input("input the credit(<=3) unless some big project")
                if(job_credit>3 or job_credit<0):
                    print('too much credit.bro')
                else:
    	    	    new_line = job_name +','+str(job_credit)+'\n'
    	    	    jobs.append(new_line)
    	    	    f = open(pwd+'data/job','w+')
    	    	    f.writelines(jobs)
                    f.close()
    	except:
    		print('please input a number')
        if(x==3):
            os.system('clear')
            print('now you can spend your credit and have fun.')
            print('you have '+ str(score)+' credit')
            f = open(pwd+'data/happy','r')
            fun = f.readlines()
            f.close()
            print('.............happy list...............')
            happylist_info = PrettyTable(["happy id","happy name","happy credit"])
            for item in range(len(fun)):
                single = fun[item].split(',')
                happylist_info.add_row([item+1,single[0],single[1]])
            print happylist_info
            print('.............happy list...............')
            acti_id = raw_input('tell me what activity you want to order.q to quit')
            if(acti_id == 'q'):
                continue
            acti_id = int(acti_id)
            single = fun[acti_id-1]
            single = single.split(',')
            if(score<int(single[1])):
                print('you dont have enough credit.failed')
            else:
                print('you have ordered '+ single[0]+','+'costing '+single[1]+' credit')
                score -= int(single[1])
                f = open(pwd+'data/score','w+')
                f.write(str(score))
                f.close()
            raw_input()
        if(1):
            if(x == 2):
                code1 = input("input the job id")
                code2 = raw_input("are you sure the id is "+str(code1)+"?(y/n)")
                if(code2 =='y'):
                    item = jobs[code1-1]
                    item = item.split(',')
                    job_name = item[0]
                    item = int(item[1])
                    f = open(pwd+'data/score','w+')
                    score += item
                    f.write(str(score))
                    f.close()
                    print('your job '+job_name+' is finished!And you have gotten '+str(item)+' credit!')
                    del jobs[code1-1]
                    f = open(pwd+'data/job','w+')
                    f.writelines(jobs)
                    f.close()
        if(x == 0):
            return;
main()