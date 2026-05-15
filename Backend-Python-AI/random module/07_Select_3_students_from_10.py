'''
2. Randomly select 3 students from a list of 10 names for a project.
'''

from typing import List, Tuple
import random

def select_students(students_to_select: int, students: List[str])->List[int]:
    '''
    Choose x students (obviously unique) from total students (eg. 3 from students)
    '''
    if students_to_select>len(students):
        raise ValueError("Students to select should be lesser than or Equal to total students")
    return random.sample(population=students, k=students_to_select)

def get_user_input()->Tuple[int, List[str]]:
    '''
    Take valid inputs
    '''
    try:
        total_students = int(input("Total students: "))
        total_to_select = int(input("Students to select: "))
        return total_to_select, [input() for _ in range(total_students)]
    except ValueError as err:
        raise ValueError("Total students and Students to select must be integers") from err

def main()->None:
    try:
        students_to_select, students = get_user_input()
        result = select_students(students_to_select, students)
        print(f"Selected Students: {result}")
    except ValueError as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()
    
# Total students: 10
# Students to select: 3
# shahwar
# alam
# naqvi
# rahul
# sonia
# priyanka
# swapnil
# yash
# bhaivirendra
# weldon
# Selected Students: ['alam', 'weldon', 'bhaivirendra']

'''
# Key Points (Solution)
- Uses random.sample() to select multiple unique elements.
- Ensures no student is selected more than once.
- Validates that students_to_select ≤ total students.
- Separates input collection, selection logic, and execution.
- Suitable for fair, non-repeating random selection.

# Key Points (Output)
- Output is a list of student names.
- List length equals students_to_select (e.g., 3).
- Selected students are always unique.
- Order of selected students is random.
- Example output: ['alam', 'weldon', 'bhaivirendra']

# Important Note
- random.sample() does NOT modify the original list.
- Ideal when uniqueness is required in random selection.
'''

    
