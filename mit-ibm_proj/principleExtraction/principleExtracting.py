class SubjectPrincipleDictionary:
    def __init__(self):
        self.subject_principle_dict = self.create_subject_principle_dict()

    def create_subject_principle_dict(self): 
        file_name = "mit-ibm_proj/principleExtraction/principles.txt" 
        subject_principle_dict = {}
        with open(file_name, 'r') as file:
            lines = file.read().split("Subject: ")
            for line in lines[1:]:
                subject, principle = line.split("Principle:")
                subject_principle_dict[subject.strip()] = principle.strip()
        return subject_principle_dict

    def lookup_principle(self, subject):
        return self.subject_principle_dict.get(subject, "Subject not found in the dictionary.")

        ## instead of no principle, I will change it into a fall back principle
