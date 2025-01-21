def interface():
    print("Blood Analysis Menu")
    while True:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter test to analyze: ")
        if choice == "9":
            break
        elif choice == "1":
            hdl_analysis()
        elif choice == "2":
            ldl_analysis()
    print("Exiting...")
    
def hdl_analysis():
    print("HDL")
    hdl_result = get_hdl_test_result()
    hdl_class = analyze_hdl_result(hdl_result)
    output_hdl_result(hdl_result, hdl_class)
    
    
def get_hdl_test_result():
    hdl_value = input("Enter the HDL test result: ")
    hdl_value = int(hdl_value)
    return hdl_value
        
def analyze_hdl_result(hdl_value):
    if hdl_value >= 60:
        return "Normal"
    elif 40 <= hdl_value < 60:
        return "Borderline Low"
    else:
        return "Low"
        
def output_hdl_result(hdl_result, hdl_class):
    print("For an HDL value of {}, the result is {}".format(hdl_result,
                                                            hdl_class))
                                                            
def ldl_analysis():
    print("ldl analysis")
                                                            
        
interface()
