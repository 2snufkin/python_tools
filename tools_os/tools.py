import os

path = r'C:\Users\Pini\Downloads'


def normalize_filename(folder_path):
    # get file list
    file_list = get_filesnames_from_folder(folder_path)
    # loop over it
    for file in file_list:
        path = folder_path + '\\' + file
        filename_no_ext = get_filename_from_path(path, False)
        norm_filename = filename_no_ext.replace('-', ' ').title()

    # for each file rename it


def get_filesnames_from_folder(folder_path):
    return os.listdir(folder_path)


def get_filename_from_path(path, is_extention):
    '''
    return the filename from a given path
    :param path: the path
    :param is_extention: true for returning also the file extenstion
    :return: the file name
    '''
    filename = os.path.basename(path)
    split_tup = os.path.splitext(filename)
    if is_extention:
        return filename
    else:
        return split_tup[0]



path = r'C:\Users\Pini\Downloads\2013.S06.1080p.BluRay.x265-RARBG-[rarbg.to](1).exe'

print(get_filename_from_path(path, False))