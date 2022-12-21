import os

path = r'C:\Users\Pini\Downloads'


# dealing with files
def normalize_filename(filename):
    clean = filename.replace('_', ' ').replace('.', ' ').replace('-', ' ')
    return clean.title()


def get_name_or_extention(filename, isExtnetion):
    '''
    get the name out of filename or extention
    :param filename:
    :param isExtnetion: do you want to get only the extention
    :return: name or extention
    '''
    splittuple = os.path.splitext(filename)
    if isExtnetion:
        return splittuple[1].replace('.', '')
    else:
        return splittuple[0]


def get_filename_from_path(path, is_extention):
    '''
    T.return the filename from a given path
    :param path: the path
    :param is_extention: true for returning also the file extenstion
    :return: the file name
    '''
    # extract the filename
    filename = os.path.basename(path)
    # create a tuple from the name and ext
    split_tuple = os.path.splitext(filename)
    if is_extention:
        return filename
    else:
        get_name_or_extention(filename, False)


# dealing with folders
def normalize_filesnames_in_folder(folder_path):
    '''
    normalize all the filenames in a folder
    :param folderpath:
    :return: a list of dict of before: after
    '''
    list_modif = []
    filenames = get_filesnames_from_folder(folder_path)
    for file in filenames:
        extract_name = get_name_or_extention(file, False)
        extention = get_name_or_extention(file, True)
        clean = normalize_filename(extract_name)
        old_name = folder_path + '\\' + file
        new_name = f'{folder_path}\\{clean}{extention}'
        os.rename(old_name, new_name)
        list_modif.append({old_name, new_name})
    return list_modif


def get_filesnames_from_folder(folder_path):
    '''
    return a list of all the filenames in this folder
    :param folder_path:
    :return:
    '''
    return os.listdir(folder_path)


def prepend_line(file_name, line):
    """ Insert given 1 line string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


def prepend_line(file_name, line):
    """ Insert given 1 line string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


def list_subdirectories(rootdir):
    list_dir = []
    for rootdir, dirs, files in os.walk(rootdir):
        for subdir in dirs:
            list_dir.append(os.path.join(rootdir, subdir))
    return list_dir
def prepend_multiple_lines(file_name, list_of_lines):
    """Insert given list of strings as a new lines at the beginning of a file"""
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open given original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Iterate over the given list of strings and write them to dummy file as lines
        for line in list_of_lines:
            write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


def prepend_multiple_lines(file_name, file_copy_from):
    """Insert given list of strings as a new lines at the beginning of a file"""
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open given original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj, open(file_copy_from) as string_to_add:
        # Iterate over the given list of strings and write them to dummy file as lines
        list_of_lines = string_to_add.readlines()
        for line in list_of_lines:
            write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


def prepend_multiple_lines_all_files_in_folder(folder_path, file_copy_from, extention):
    """Insert given text from a file to all the files  in a certain folder with a given extension"""
    list_of_files = get_filesnames_from_folder(folder_path)
    for file in list_of_files:
        ext = get_name_or_extention(file, True)
        if ext == extention:
            file_path = folder_path + '\\' + file
            prepend_multiple_lines(file_path, file_copy_from)


def prepend_multiple_lines_all_files_in_subfolder(folder_path, file_copy_from, extention):
    list_d = list_subdirectories(folder_path)
    for folder in list_d:
        prepend_multiple_lines_all_files_in_folder(folder, file_copy_from, extention)

folder_root = r'C:\Users\Pini\IdeaProjects\iTextPdfTuto'
prepend_multiple_lines_all_files_in_subfolder(folder_root, r'C:\Users\Pini\PycharmProjects\yonitools\tools_os\copyright.txt', 'java')