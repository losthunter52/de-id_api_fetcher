import getopt, sys
from src.run import Run

argumentList = sys.argv[1:]
options = "ha:p:"

try:
    arguments, values = getopt.getopt(argumentList, options)
    archive = False
    threads = False
    run = False
     
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h"):
            print ("""python main.py -h <= Help
               -a <Str:Arqchive> <= Input Database File (JSON extension)
               -p <Str:Processors> <= Number of Threads""")
             
        elif currentArgument in ("-a"):
            archive = currentValue
             
        elif currentArgument in ("-p"):
            threads = currentValue
    
    if archive:
        if threads:
            Run(archive, threads)
        else:
            print("Need threads")    
    else:
        print("Need archive")
             
except getopt.error as err:
    print (str(err))


