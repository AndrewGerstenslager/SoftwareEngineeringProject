class Course:
    def __init__(self, course):
        self.id = course['id']
        self.name = course['name']
        self.account_id = course['account_id']
        self.uuid = course['uuid']
        self.start_at = course['start_at']
        self.grading_standard_id = course['grading_standard_id']
        self.is_public = course['is_public']
        self.created_at = course['created_at']
        self.course_code = course['course_code']
        self.default_view = course['default_view']
        self.root_account_id = course['root_account_id']
        self.enrollment_term_id = course['enrollment_term_id']
        self.license = course['license']
        self.grade_passback_setting = course['grade_passback_setting']

    def show_course(self):
        print(self.name)

    