# functions grades

def grade_analyze(grade):
    if grade>=90: 
        return "A"
    elif grade>=80:
        return "B"
    elif grade>=70:
        return "C"
    else:
        return "F"
    
def record_builder(name,numgrade,lettergrade):
    student_record=[name,numgrade,lettergrade]
    return student_record
        
        




