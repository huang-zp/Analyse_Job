import os
FILE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/app/resources/' + 'index.txt'
tag_list = []
with open(FILE_PATH, 'r') as f:
    for line in f:
        tag_list.append(line.strip())

print(tag_list)