import os
import sys
start = int(sys.argv[1])
end = int(sys.argv[2])

with open('names_refined.txt') as names:
     for i, line in enumerate(names):
         if  start <= i <= end:
            print line
            os.system("cd $graph; matlab -nodisplay -nosplash -nodesktop -r \"run_all('{}','{}','{}');exit;\"".format('aaaa', '8', line.strip()))

