import os
global sub
sub = []

dir  = 'C:\\Users\\stmwr\\Downloads\\entrepreneurs-audio'

for file in os.listdir(dir):
    afile = file
    if file.startswith(('1-','2-','3-','4-','5-','6-','7-','8-','9-',)):
        file = ''.join(('0',file))
    os.rename(afile, file)
    sub.append(file)
    print(file)


for folder in range(len(sub)):
    subpath = ''.join((dir, '\\', sub[folder]))
    dir = subpath
    for file in os.listdir(dir):
        if file.startswith(('1-', '2-', '3-', '4-', '5-', '6-', '7-', '8-', '9-',)):
            file = ''.join(('0', file))