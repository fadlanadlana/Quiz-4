ListGPA = [2.1,2.5,4,3]
def hadiah(GPA):
    hadiah = GPA*500000
    return hadiah

for GPA in ListGPA:
    if GPA > 2.5 :
       print ("Hadiah anda RP.",hadiah(GPA))
    else :
        print ("maaf") 
    
    
