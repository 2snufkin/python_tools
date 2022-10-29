from unittest import TestCase
import  tools

class Test(TestCase):
    def test_get_filename_from_path(self):
        path = r'C:\Users\Pini\Downloads\2013.S06.1080p.BluRay.x265-RARBG-[rarbg.to](1).exe'
        with_ext = tools.get_filename_from_path(path, True)
        without = tools.get_filename_from_path(path, False)
        self.assertEqual(with_ext, '2013.S06.1080p.BluRay.x265-RARBG-[rarbg.to](1).exe')
        self.assertEqual(without, '2013.S06.1080p.BluRay.x265-RARBG-[rarbg.to](1)')

    def test_get_files_name(self):
        folderpath = r'C:\Users\Pini\Documents'
        result = ['desktop.ini', 'My Music', 'My Pictures', 'My Videos', 'test.txt.txt']
        filenames = tools.get_filesnames_from_folder(folderpath)
        self.assertEqual(filenames, result)
