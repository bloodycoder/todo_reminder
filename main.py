import sys
sys.path.append("/root/bloodycoder/todo_reminder/")
sys.path.append("/root/bloodycoder/todo_reminder/memorycurv")
import PicardMail
import hello
joblist = hello.get_joblist()
contentstr = ''
for job in joblist:
    contentstr+=job

robot = PicardMail.PicardSendMail()
robot.Login()
robot.SendAnEmail(email= contentstr,subject=str(len(joblist))+" remain",destination="510297127@qq.com")
robot.Quit()
