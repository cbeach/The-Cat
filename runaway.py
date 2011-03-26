import commands

#    for i in output
if __name__ == "__main__":
    print "hello"
    string1 = commands.getoutput('top -bn 1')
    counter = 0
    tokens = string1.split('\n')    


    for i in tokens:
        print counter, " ", i        
        counter += 1
