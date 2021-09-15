def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("9 = Quit")
        print("1 = HDL Analysis")
        print("2 = LDL Analysis")
        choice = int(input("Make a choice: "))
        # The input would be a string, so converting it to an integer to do comparisons
        if choice == 9:
            keep_running = False
        elif choice == 1 :
            HDL_Driver()
        elif choice == 2 :
            LDL_Driver()
    
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
        hdl_char = "normal"
    elif ((HDL_Value < 60) & (HDL_Value >= 40)):
        hdl_char = "borderline low"
    elif HDL_Value < 40:
        hdl_char = "low"
    return hdl_char
    
def hdl_output(HDL_Value,HDL_Character):
    print("At an HDL Value of ",HDL_Value,", your cholesterol is ",HDL_Character)

def LDL_Driver():
    LDL_Value = ldl_input()
    LDL_Character = ldl_analysis(LDL_Value)
    ldl_output(LDL_Value, LDL_Character)
    
def ldl_input():
    ldl_value = int(input(("Enter LDL Value: ")))
    return ldl_value

def ldl_analysis(LDL_Value):
    if LDL_Value >= 190:
        ldl_char = "very high"
    elif ((LDL_Value > 160) & (LDL_Value <= 189)):
        ldl_char = "high"
    elif ((LDL_Value >= 130) & (LDL_Value <= 159)):
        ldl_char = "borderline high"
    elif LDL_Value < 130:
        ldl_char = "normal"
        
    return ldl_char
    
def ldl_output(LDL_Value,LDL_Character):
    print("At an LDL Value of ",LDL_Value, ", your cholesterol is ",LDL_Character)
   
if __name__ == "__main__":
    interface()
    
