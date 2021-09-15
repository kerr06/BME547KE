import pytest

#Line below is a decorater, adding functionality to a line. Needs to go on the line right before the function
#duplicate the parameters of the function EXACTLY 
@pytest.mark.parametrize("HDL_Value, expected", [
    (65, "normal"),
    (45, "borderline low"), 
    (15, "low")])
def test_hdl_analysis(HDL_Value, expected): 
	from blood_calculator import hdl_analysis
	answer = hdl_analysis(HDL_Value)
	assert answer == expected

