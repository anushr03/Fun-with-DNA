####### Class Patient ######## 
class Patient:
    def __init__(self, name=None, age=None, dna=None, condition=False):  # initializing the constructor patient
        self.name=name
        self.age =age
        self.strand=dna
        self.has_condition=condition