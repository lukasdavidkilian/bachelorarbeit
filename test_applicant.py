import unittest
from applicant import Applicant
from job import Job
from company import Company

class TestApplicant(unittest.TestCase):
    def setUp(self):
        self.applicant = Applicant('John', 'Doe', 'john.doe@example.com', 'resume.pdf')
        self.company = Company('Tech Corp', [], [])
        self.job = Job('Software Engineer', self.company, [], None)

    def test_apply(self):
        self.applicant.apply(self.job)
        self.assertIn(self.applicant, self.job.applicants)

    def test_apply_return_message(self):
        application, message = self.applicant.apply(self.job)
        expected_message = f"John Doe has applied to Software Engineer at {self.job.company}."
        self.assertEqual(message, expected_message)

    def test_apply_twice(self):
        self.applicant.apply(self.job)
        self.applicant.apply(self.job)

        # Erwartet 1, da sich ein Bewerber nur einmal auf eine Stelle bewerben kann

        # Zunächst wurde hier aber durch GitHub Copilot die tatsächliche Anzahl an Bewerber ausgegeben

        self.assertEqual(1, self.job.applicants.count(self.applicant))

    def test_applicant_withdraws_application_successfully(self):
        self.applicant.apply(self.job)
        self.applicant.withdraw_application(self.job)
        self.assertNotIn(self.applicant, self.job.applicants)

    def test_applicant_withdraws_application_not_applied(self):
        pass

if __name__ == '__main__':
    unittest.main()
