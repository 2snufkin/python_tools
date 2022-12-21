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
        return splittuple[1]
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

def delete_folder(path):
    pass

list_modif = normalize_filesnames_in_folder(r'C:\Users\Pini\Downloads')
print(list_modif)





