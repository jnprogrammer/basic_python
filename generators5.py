import os, fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files, in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


my_music_files = find_music('music', 'emp3')

error_list = []


for f in find_music('music', 'emp3'):
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:
        error_list.append(f)


print("generating improper mp3 files")
for error_file in error_list:
    print(error_file)
