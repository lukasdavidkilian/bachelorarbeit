import unittest
from application import Application
from applicant import Applicant
from job import Job
from company import Company

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.applicant = Applicant('John', 'Doe', 'john.doe@example.com', 'resume.pdf')
        self.company = Company('Tech Corp', [], [])
        self.job = Job('Software Engineer', self.company, [], None)
        self.application = Application(self.applicant, self.job, [], 'Pending')

    def test_schedule_interview(self):
        interviewer = 'Jane Smith'
        date = '2022-12-01'
        time = '10:00'
        interview, message = self.application.schedule_interview(interviewer, date, time)
        self.assertIn(interview, self.application.interviews)
        expected_message = f"Interview scheduled for {self.application.applicant.first_name} {self.application.applicant.last_name} for {self.application.job.name} at {self.application.job.company}."
        self.assertEqual(message, expected_message)

if __name__ == '__main__':
    unittest.main()