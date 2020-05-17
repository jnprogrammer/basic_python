import os

listing = os.walk('.')
for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)
    for file in files:
        print(file)