from OOP.College import College


class TeacherDetail(College):
    def __init__(self,ColCode,ColName,TeacherId,TeacherName,Dept):
        super().__init__(ColCode,ColName)
        self.TeacherId = TeacherId
        self.TeacherName = TeacherName
        self.Dept = Dept

    def display(self):
        print(f'{self._ColCode} \t {self._ColName} \n'
              f'{self.TeacherId} \n{self.TeacherName} \n{self.Dept} ')
