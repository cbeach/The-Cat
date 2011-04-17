import commands

class sshSessions():

    def __init__(self):
        self.netgroups = []
        self.processes = []

    def getComputers(self):
        linuxLogin = commands.getoutput("netgrouplist linux-login-sys")
	csServer = commands.getoutput("netgrouplist cs-server-sys")
        eceGeneral = commands.getoutput("netgrouplist ece-general-sys")
        catService = commands.getoutput("netgrouplist cat-service-sys")
        catServer = commands.getoutput("netgrouplist cat-server-sys")


#	linuxLogin.translate(None,'n\\')
        self.netgroups.extend(linuxLogin.split(' '))
        self.netgroups.extend(csServer.split(' '))
        self.netgroups.extend(eceGeneral.split(' '))
        self.netgroups.extend(catService.split(' '))
        self.netgroups.extend(catServer.split(' '))
        
	
        return self.netgroups

    def getPS(self):
        for i in self.netgroups:
            print commands.getoutput("ssh " + i + "ps -eo pid,pcpu,pmem,args,time").split(' ')
            
 

    if __name__=="__main__":
        s = sshSession();
        print netgroups
        
