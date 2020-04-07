import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Duck', 'Daisy','CIS')

    def tearDown(self):
        del self.student

    def test_object_created_required_atrributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'CIS')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'CIS')
        self.assertEqual(self.student.gpa, 0.0)



if __name__ == '__main__':
    unittest.main()