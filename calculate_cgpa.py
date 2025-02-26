def cgpa(gpa_list, credit_list):
    total_point = 0
    for gpa, credit in zip(gpa_list, credit_list):
        point = gpa * credit
        total_point += point
        
    total_credit = sum(credit_list)
    
    return round( (total_point / total_credit), 2)
    


    
"""
    sub -----      gpa---- credit = gpa * credit
    CSE-101 ----- 3.5 --     3    = 3.5*3 = 10.5
    CSE-102 ----- 4 --       3    = 4*3 =  12 
    
    total point = 10.5+12 = 22.5
    total credit = 3+3 = 6
    cgpa = total point / total credit = 22.5 / 6 = 3.75
"""
