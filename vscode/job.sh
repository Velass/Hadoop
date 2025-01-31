import sys
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
current_word = None
current_count= 0
word = None
print()"Entering reducer.py"
for line in sys.stdin:
 line = line.strip()
 parts = line.split('\t', 1)
 if len(parts) < 2:
 continue
 word = parts[0]
 count = parts[1]
 try:
 count = int(count)
 except ValueError:
 continue
 if current_word == word:
 current_count += count
 else:
 if(current_word):
 print("%s\t%s" %(current_word,current_count))
 current_count = count
 current_word = word
if current_word == word:
 print("%s\t%s" %(current_word, current_count))
