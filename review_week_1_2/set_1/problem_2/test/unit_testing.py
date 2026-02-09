import unittest
from string import whitespace

from review_week_1_2.set_1.problem_2.emp_exceptions.employee_exceptions import EmailError
from review_week_1_2.set_1.problem_2.validators.employee_validators import validate_email, validate_phone
from review_week_1_2.set_1.problem_2.employee_email_phone_verifty import Employee
class EmployeeUnits(unittest.TestCase):
    def test_email_validater(self):
        t1 = validate_email("deep.o8@co.in")
        t2 = validate_email(".dev.com")
        self.assertEqual(t1,True,"t1_email failed")  # message only shows for failed test cases
        self.assertEqual(t2, False,"t2_email failed")

    def test_phone_validator(self):
        t1 = validate_phone(8001334960)
        t2 = validate_phone(32422212442)

        self.assertTrue(t1)
        self.assertFalse(t2)

    def test_email_setter_validator(self):
        with self.assertRaises(EmailError):
            e1 = Employee("07JAN26","SASHANK",".shk@gmail.com",9153561430)

if __name__=="__main__":
    unittest.main()

