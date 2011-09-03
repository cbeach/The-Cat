import commands
import string

class sshSessions:

    def __init__(self):
        self.netgroups = []
        self.processes = []

    def getComputers(self):
	    temp = []
        linuxLogin = commands.getoutput("netgrouplist linux-login-sys")
	    csServer = commands.getoutput("netgrouplist cs-server-sys")
        eceGeneral = commands.getoutput("netgrouplist ece-general-sys")
        catService = commands.getoutput("netgrouplist cat-service-sys")
        catServer = commands.getoutput("netgrouplist cat-server-sys")

        temp.extend(linuxLogin.split(' '))
        temp.extend(csServer.split(' '))
        temp.extend(eceGeneral.split(' '))
        temp.extend(catService.split(' '))
        temp.extend(catServer.split(' '))

        for i in temp:
            self.netgroups.extend(i.split('\n'))
	
        return self.netgroups

    def getPS(self):
        for i in self.netgroups:
            print commands.getoutput("ssh " + i + " ps -eo pid,pcpu,pmem,args,time").split(' ')
           
    if __name__=="__main__":
        s = sshSessions();
        print netgroups
        
