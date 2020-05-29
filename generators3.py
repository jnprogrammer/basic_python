import os

if __name__ == '__main__':

    root = "music"  # type: str

    for path, directory, files, in os.walk(root, topdown=True):
       if files:
           print(path)
           first_split = os.path.split(path)
           print(first_split)
           second_split = os.path.split(path)
           print(second_split)
           for f in files:
               song_details = f[:-5].split(' _ ')
               print(song_details)
           print("@" * 50)


        # print(path)
        # print(directory)
        # print(files)
        # input()
        # for f in files:
        #     print("\t{}".format(f))
