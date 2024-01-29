import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations_counted = examinations.groupby(['student_id', 'subject_name']).size().rename('attended_exams')
    return students.merge(subjects, how='cross').merge(examinations_counted, how='left', on=['student_id', 'subject_name'])[
        ['student_id', 'student_name', 'subject_name', 'attended_exams']
    ].sort_values(by=['student_id', 'subject_name']).fillna(value={'attended_exams': 0})
