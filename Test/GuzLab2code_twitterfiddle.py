#TG comment: using JSON in lab 2
import json
#test from http://pymotw.com/2/json/
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print ('DATA:'), repr(data)

data_string = json.dumps(data)
print ('JSON:'), data_string