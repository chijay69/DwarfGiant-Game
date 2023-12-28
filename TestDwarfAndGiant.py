import unittest
from main import remove_duplicates, create_employee_pairs, generate_unique_pairs


class MyTestCase(unittest.TestCase):

    # Test case for removing duplicates from the employee list
    def test_remove_duplicates(self):
        employees = [
            {"name": "Alice", "department": "Sales", "age": 25},
            {"name": "Bob", "department": "R&D", "age": 30},
            {"name": "Alice", "department": "Sales", "age": 25},
            {"name": "Charlie", "department": "Support", "age": 35},
        ]
        cleaned_employees = remove_duplicates(employees)
        expected_result = [
            {"name": "Alice", "department": "Sales", "age": 25},
            {"name": "Bob", "department": "R&D", "age": 30},
            {"name": "Charlie", "department": "Support", "age": 35},
        ]
        self.assertEqual(cleaned_employees, expected_result)

    # Test case for creating employee pairs
    def test_create_employee_pairs(self):
        employees = [
            {"name": "Alice", "department": "Sales", "age": 25},
            {"name": "Bob", "department": "R&D", "age": 30},
            {"name": "Charlie", "department": "Support", "age": 35},
            {"name": "Charles", "department": "Support", "age": 45}
        ]
        pairs = create_employee_pairs(employees)
        # Validate the structure and randomness of pairs if necessary
        for pair in pairs:
            self.assertIsInstance(pair, tuple)  # Check if pairs are tuples

            dwarf, giant = pair
            self.assertIsInstance(dwarf, dict)  # Check if dwarf is a dictionary
            self.assertIsInstance(giant, dict)  # Check if giant is a dictionary

            self.assertIn(dwarf, employees)  # Check if dwarf is in the original employee list
            self.assertIn(giant, employees)  # Check if giant is in the original employee list

    # Test case for generating unique pairs
    def test_generate_unique_pairs(self):
        employees = [
            {"name": "Charlie", "department": "Support", "age": 35},
            {"name": "Charlie", "department": "Support", "age": 35},
            {"name": "Charlie", "department": "Support", "age": 35},
            {"name": "Charlie", "department": "Support", "age": 35},
            {"name": "Charlie", "department": "Support", "age": 35},
        ]
        # Validate uniqueness and correct pair generation logic
        unique_pairs = generate_unique_pairs(remove_duplicates(employees))
        # Validate uniqueness
        self.assertEqual(len(unique_pairs), len(set(unique_pairs)), "Duplicates found in pairs")

        # Validate each employee appears exactly once as a dwarf or a giant
        # Flatten the pairs into a single list of all employees
        all_employees = [emp for pair in unique_pairs for emp in pair]
        print("unique pairs", unique_pairs)
        print("flat pairs", all_employees)

        # Count occurrences of each employee
        employee_count = {emp: all_employees.count(emp) for emp in set(all_employees)}

        # Check if every employee occurs at least twice
        for count in employee_count.values():
            self.assertLessEqual(count, 1, "Employee doesn't appear at least twice in pairs")


if __name__ == '__main__':
    unittest.main()
