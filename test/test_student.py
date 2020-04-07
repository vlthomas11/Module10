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

    def test_student_str(self):
        p = s.Student('Duck','Daisy','CIS',4.0)
        self.assertEqual(str(p),"Duck, Daisy has major CIS with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        pass

    def test_object_not_created_error_last_name(self):
        pass


if __name__ == '__main__':
    unittest.main()