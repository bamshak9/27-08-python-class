students_scores = {
            "Aisha": 95,
                "David": 82,
                    "Mary": 99,
                        "John": 78,
                            "Sarah": 65,
                                "Paul": 88,
                                    "Grace": 100,
                                        "James": 73,
                                            "Ruth": 84,
                                                "Daniel": 90,
                                                    "Michael": 67,
                                                        "Esther": 59,
                                                            "Tunde": 48,
                                                                "Ngozi": 34,
                                                                    "Chinedu": 27,
                                                                        "Hauwa": 72,
                                                                            "Ibrahim": 41,
                                                                                "Femi": 53,
                                                                                    "Victoria": 68,
                                                                                        "Samuel": 38
                                                                                        }
running = 0
keys=list(students_scores.keys())
A_students={}
B_students={}
C_students={}
D_students={}
E_students={}
F_students={}
while running< len(keys):
    if students_scores[keys[running]]>=70 and students_scores[keys[running]]<=100:
        A_students[keys[running]]=students_scores[keys[running]]
    elif students_scores[keys[running]]>=60 and students_scores[keys[running]]<=69:
        B_students[keys[running]]=students_scores[keys[running]]
    elif students_scores[keys[running]]>=50 and students_scores[keys[running]]<=59:
         C_students[keys[running]]=students_scores[keys[running]]
    elif students_scores[keys[running]]>=40 and students_scores[keys[running]]<=49:
         D_students[keys[running]]=students_scores[keys[running]]
    elif students_scores[keys[running]]>=30 and students_scores[keys[running]]<=39:
         E_students[keys[running]]=students_scores[keys[running]]
    else:
        F_students[keys[running]]=students_scores[keys[running]]
    running +=1
print(f'''
        The A rank students are {A_students}
        The B rank students are {B_students}
        The C rank students are {C_students}
        The D rank students are {D_students}
        The E rank students are {E_students}
        The F rank students are {F_students}
        ''')



