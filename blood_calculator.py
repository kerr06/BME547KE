def interface(): 
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("9 = Quit")
        choice = int(input("Make a choice: "))
        #The input would be a string, so converting it to an integer to do comparisons
        if choice == 9:
            keep_running = False 
        elif 
            HDL_Driver()
        
    
    print(choice)
    return choice
    
def HDL_Driver(): 
    HDL_Value = hdl_input()
    HDL_Character = hdl_analysis(HDL_Value)
    hdl_output(HDL_Value, HDL_Character)
    
def hdl_input(): 
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value
	
def hdl_analysis(HDL_Value): 
    if HDL_Value >= 60
        return "Normal"
    elif HDL_Value < 60 && HDL_Value >=40 
        retun "Borderline Low"
    elif HDL_Value < 40 
        return "Low" 
    
    
interface() 