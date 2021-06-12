# import logging    # first of all import the module

# logging.basicConfig(filename='std.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This message will get logged on to a file')
# logging.error("Have you try to divide a number by zero")


import re
import time
from time import strftime
 

log_file_path = "D:\PythonExercise\std.log"
export_file_path = "D:\PythonExercise\error.txt"
warning_file_path = "D:\PythonExercise\warning.txt"
 
time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
 
# file = "\\" + "Parser Output " + time_now + ".txt"
# export_file = export_file_path + file
 
regex = 'ERROR.*'

regexWarning = 'WARNING.*'
read_line = False
 
with open(log_file_path, "r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line, re.S):
                match_text = match.group()
                match_list.append(match_text)
                print (match_text)
    else:
        data = file.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group();
            match_list.append(match_text)
file.close()
 
with open(export_file_path, "w+") as file:
    # file.write("EXPORTED DATA:\n")
    match_list_clean = list(set(match_list))
    for item in range(0, len(match_list_clean)):
        print (match_list_clean[item])
        file.write(match_list_clean[item] + "\n")
file.close()