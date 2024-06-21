from interview import Interview
import PyPDF2


class Application:
    def __init__(self, applicant, job, interviews, status):
        self.applicant = applicant
        self.job = job
        self.interviews = interviews
        self.status = status

    def schedule_interview(self, interviewer, date, time):
        """
        This method schedules an interview for the applicant.

        Parameters:
        interviewer (str): The name of the interviewer.
        date (str): The date of the interview in the format 'YYYY-MM-DD'.
        time (str): The time of the interview in the format 'HH:MM'.

        Returns:
        tuple: A tuple containing the Interview object and a string message.
               The Interview object contains the details of the scheduled interview.
               The string message provides information about the scheduled interview.
        """

        # Create a new Interview object with the application, interviewer, date, and time
        interview = Interview(self, interviewer, date, time)
        # Add the Interview object to the application's interviews list
        self.interviews.append(interview)
        # Return the Interview object and a message indicating that the interview has been scheduled
        return interview, f"Interview scheduled for {self.applicant.first_name} {self.applicant.last_name} for {self.job.name} at {self.job.company}."

    # PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.

    """

    def read_pdf(file_path):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            num_pages = reader.numPages
            text = ''
            for page in range(num_pages):
                text += reader.getPage(page).extractText()
        return text

    resume_text = read_pdf("lebenslauf_muster_schueler.pdf")

    # Prompt: function to scan CV if applicant should be invited


    """

    def should_invite(self):
        resume_text = self.scan_cv()
        keywords = ['Python', 'Java', 'Software Engineer', 'Developer']  # Add more relevant keywords
        for keyword in keywords:
            if keyword in resume_text:
                return True
        return False

    # further prompts trying to make the function more effective lead to regex and quickly coming to an end with "Oops, no response has returned."