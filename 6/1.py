class Student:
    def __init__(self, name, group, grades:list, tel_number):
        self._name = name
        self._group = group
        self._grades = grades
        self._tel_number = tel_number

    def add_grade(self, grade):
        self._grades.append(grade)
        
    def get_average(self):
        res = 0
        for g in self._grades:
            res += g
        l = len(self._grades) or 1

        return res / l
    
    def info(self):
        return {
            'name': self._name,
            'group': self._group,
            'grades': self._grades,
            'tel_number': self._tel_number
        }

st = Student("Rustam", "36-63", [], "+788888888")
print(st.get_average())
st.add_grade(5)
st.add_grade(3)
st.add_grade(4)
st.add_grade(7)
print(st.get_average())
print(st.info().get("name"))