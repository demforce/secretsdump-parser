# Taken two files, matches user with cleartext pwd
import sys, os

def usage():
    print ("[+] Usage: " + sys.argv[0] + " secretsdump crackedhashes outfile")
    print("secretsdump must be: Path to file containing user:id:domainHash:userHash\n""crackedhashes must be: Path to file containing hash:cleartextPwd\n""outfile: path to output file")
    print("Examples:\nsecretsdump: Administrator:12131:aad3b435b51404eeaad3b435b51404ee:8846F7EAEE8FB117AD06BDD830B7586C::: ")
    print("crackedhashes: 8846F7EAEE8FB117AD06BDD830B7586C:password ")
    
def readfile():                                                             # import 3 files 
    file_hash = sys.argv[1]
    file_clear = sys.argv[2]
    outfile = sys.argv[3]

    f1 = open(file_hash,"r")
    lines1 = f1.readlines()                                                 # user:id:domainhash:hash..
    f1.close()
    
    f2 = open(file_clear,"r")
    lines2 = f2.readlines()                                                 # hash:cleartext
    f2.close()
    
    return lines1, lines2, outfile

def main():
        
    if os.path.exists(readfile()[2]):
        os.remove(readfile()[2])

    f3 = open(readfile()[2], "a")                                           # open outfile for writing
    
    for y in readfile()[1]:                                                 # read lines of file_hash
        for i in readfile()[0]:                                             # read lines of file_clear    
            if y.split(":")[0].lower() == i.split(":")[3].lower():          # if hash == hash substitute with cleartext
                #print (i.split(":")[0] + ":" + y.split(":")[1], end ="")
                f3.write(i.split(":")[0] + ":" + y.split(":")[1])           # write to outfile

    f3.close()            

if len(sys.argv) > 3:
    main()
else:
    usage()