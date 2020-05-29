import os

if __name__ == '__main__':

    root = "/music"  # type: str

    for path, directory, files, in os.walk(root, topdown=True):
        print(path)
        print(directory)
        print(files)
        input()
        # for f in files:
        #     print("\t{}".format(f))
