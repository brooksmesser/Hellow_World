# run functions grades

import score_analyzer_functions_messer

students=int(input("How many students are in your class:"))

for i in range(students):
    name=input("What is your students name:")
    numgrade=int(input(f"What is {name}'s number grade:"))
    stu_record=score_analyzer_functions_messer.record_builder(name,numgrade,score_analyzer_functions_messer.grade_analyze(numgrade))
    print(stu_record)
    