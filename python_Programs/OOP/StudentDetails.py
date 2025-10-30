from OOP.College import College


class StudentDetails(College) :
    def __init__(self,ColCode, ColName, rollNo, sname, m1, m2, m3 ):
        super().__init__(ColCode, ColName)
        self.__rollNo = rollNo
        self.__sname = sname
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def get_rollNo(self):
        return self.__rollNo
    def set_rollNo(self,rollNo):
        self.__rollNo = rollNo

    def get_sname(self):
        return self.__sname
    def set_sname(self,sname):
        self.__sname = sname

    def get_m1(self):
        return self.__m1
    def set_m1(self,m1):
        self.__m1 = m1

    def get_m2(self):
        return self.__m2
    def set_m2(self,m2):
        self.__m2 = m2

    def get_m3(self):
        return self.__m3
    def set_m3(self,m3):
        self.__m3 = m3


    def Calc_total(self):
        return self.__m1 + self.__m2 + self.__m3

    def calc_avg(self):
        return self.Calc_total() / 3