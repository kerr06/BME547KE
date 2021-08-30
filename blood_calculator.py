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
        else :
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
    if HDL_Value >= 60:
        hdl_char = "Normal"
    elif ((HDL_Value < 60) & (HDL_Value >= 40)):
        hdl_char = "Borderline Low"
    elif HDL_Value < 40:
        hdl_char = "Low"     
        
    return hdl_char
    
def hdl_output(HDL_Value,HDL_Character): 
    print("At an HDL Value of ", HDL_Value, ", your cholesterol is ",HDL_Character)) 
   
    
HDL_Driver() 
interface() 