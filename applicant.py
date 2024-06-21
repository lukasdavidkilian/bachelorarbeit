from application import Application


class Applicant:
    def __init__(self, first_name, last_name, email, resume):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.resume = resume

    # Kommentar: "function: has already applied"

    def has_already_applied(self, job):
        return self in job.applicants

    # Funktion apply war bereits gegeben

    def apply(self, job):

        """
            This method allows an applicant to apply for a job.

            Parameters:
            job (Job): The job object that the applicant is applying to.

            Returns:
            tuple: A tuple containing the Application object and a string message.
                   The Application object is returned if the applicant has not already applied for the job.
                   The string message provides information about the applicant and the job.
            """

        if not self.has_already_applied(job):
            job.applicants.append(self)
            application = Application(self, job, [], 'Pending')
            return application, f"{self.first_name} {self.last_name} has applied to {job.name} at {job.company}."
        else:
            return None, f"{self.first_name} {self.last_name} has already applied to {job.name} at {job.company}."

    # Prompt: function for withdrawing an application as an applicant

    def withdraw_application(self, job):
        """
        This method allows an applicant to withdraw an application for a job.

        Parameters:
        job (Job): The job object that the applicant wants to withdraw the application from.

        Returns:
        str: A string message providing information about the withdrawal status.
             If the applicant has an application for the job, the application is removed and the message indicates that the applicant has withdrawn the application.
             If the applicant has no application for the job, the message indicates so.
        """

        # Iterate over all applications for the job
        for applicants in job.applicants:
            # If the applicant of the application is the current applicant
            if applicants == self:
                # Remove the application from the job's applications list
                job.applicants.remove(applicants)
                # Change the status of the application to 'Withdrawn'
                applicants.status = 'Withdrawn'
                # Return a message indicating that the applicant has withdrawn the application
                return f"{self.first_name} {self.last_name} has withdrawn the application for {job.name} at {job.company}."
        # If the applicant has no application for the job, return a message indicating so
        return f"{self.first_name} {self.last_name} has no application for {job.name} at {job.company}."