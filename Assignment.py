class Assignment:
    def __init__(self, assignment):
        self.id = assignment['id']
        self.description = assignment['description']
        self.due_at = assignment['due_at']
        self.unlock_at = assignment['unlock_at']
        self.lock_at = assignment['lock_at']
        self.points_possible = assignment['points_possible']
        self.grading_type = assignment['grading_type']
        self.assignment_group_id = assignment['assignment_group_id']
        self.grading_standard_id = assignment['grading_standard_id']
        self.created_at = assignment['created_id']
        self.updated_at = assignment['updated_at']
        self.name = assignment['name']
        self.has_submitted_submissions = assignment['has_submitted_submissions']
        self.due_date_required = assignment['due_date_required']
        self.muted = assignment['muted']
        self.html_url = assignment['html_url']
   
    def show_assignment(self):
        print(self.name)