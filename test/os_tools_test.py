from unittest import TestCase

from tools_os import os_tools


class Test(TestCase):
    def test_get_filename_from_path(self):
        path = r'C:\Users\Pini\Downloads\2013.S06.1080p.BluRay.x265-RARBG-[rarbg.to](1).exe'
        with_ext = os_tools.get_filename_from_path(path, True)
        without = os_tools.get_filename_from_path(path, False)
        self.assertEqual(with_ext, '2013.S06.1080p.BluRay.x265-RARBG-[rarbg.to](1).exe')
        self.assertEqual(without, '2013.S06.1080p.BluRay.x265-RARBG-[rarbg.to](1)')

    def test_get_filesname_from_folder(self):
        folderpath = r'C:\Users\Pini\Documents'
        result = ['desktop.ini', 'My Music', 'My Pictures', 'My Videos', 'test.txt.txt']
        filenames = os_tools.get_filesnames_from_folder(folderpath)
        self.assertEqual(filenames, result)

    def test_normalize_filename(self):
        filename = 'this_is_me.who.speak.pdf'
        clean = os_tools.normalize_filename(filename)
        self.assertEqual(clean, 'This Is Me Who Speak.pdf')

    def test_get_name_or_extention(self):
        filename = 'windows64 Xp.exe'
        name = os_tools.get_name_or_extention(filename, False)
        extention = os_tools.get_name_or_extention(filename, True)
        self.assertEqual(name, 'windows64 Xp')
        self.assertEqual(extention, 'exe')

    def test_prepend_line(self):
        self.fail()

    def test_extract_folder_from_path(self):
        filenamepath = r'C:\Users\Pini\Documents\test.pdf'
        folder = r"C:\Users\Pini\Documents"
        folder_from = os_tools.extract_folder_from_path(filenamepath)
        self.assertEqual(folder_from, folder)
