import unittest

class StudentManager:
    def __init__(self):
        self.students = {}  # Inicializa o dicionário de alunos

    def add_student(self, name: str, grades: list):
        if name in self.students:
            raise ValueError(f"Student {name} already exists.")
        if not all(isinstance(grade, (int, float)) for grade in grades):
            raise ValueError("Grades must be a list of numbers.")
        self.students[name] = grades

    def get_average(self, name: str) -> float:
        if name not in self.students:
            raise ValueError(f"Student {name} does not exist.")
        return sum(self.students[name]) / len(self.students[name])

    def is_passed(self, name: str, passing_grade: float = 6.0) -> bool:
        average = self.get_average(name)
        return average >= passing_grade


class TestStudentManager(unittest.TestCase):
    def setUp(self): #Configuração inicial para cada teste
        self.manager = StudentManager()
        
    def test_add_student(self):
        self.manager.add_student("João", [6.0, 10.0, 7.0, 8.0])
        self.assertIn("João", self.manager.students)

    def test_add_student_existing(self):
        self.manager.add_student("João", [6.0, 10.0, 7.0, 8.0])
        with self.assertRaises(ValueError):
            self.manager.add_student("João", [3.0, 9.0])

    def test_average(self):
        self.assertEqual(self.manager.get_average("João"), 7.75)

    def test_passed(self):
        self.assertTrue(self.manager.is_passed("João"))





if __name__ == '__main__':
    unittest.main()
