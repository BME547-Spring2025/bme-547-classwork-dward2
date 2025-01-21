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
    test_name = "HDL"
    hdl_result = get_generic_test_result(test_name)
    hdl_class = analyze_hdl_result(hdl_result)
    output_generic_test_result(test_name, hdl_result, hdl_class)
    
    
def get_generic_test_result(test_name):
    test_value = input("Enter the {} test result: ".format(test_name))
    test_value = int(test_value)
    return test_value
        
def analyze_hdl_result(hdl_value):
    if hdl_value >= 60:
        return "Normal"
    elif 40 <= hdl_value < 60:
        return "Borderline Low"
    else:
        return "Low"
        
def output_generic_test_result(test_name, test_result, test_class):
    print("For a(n) {} value of {}, the result is {}".format(test_name,
                                                            test_result,
                                                            test_class))
                                                            
def ldl_analysis():
    test_name = "LDL"
    ldl_result = get_generic_test_result(test_name)
    ldl_class = analyze_ldl_result(ldl_result)
    output_generic_test_result(test_name, ldl_result, ldl_class)
    
def analyze_ldl_result(ldl_value):
    if ldl_value < 130:
        return "Normal"
    elif 130 <= ldl_value < 160:
        return "Borderline High"
    elif 160 <= ldl_value < 190:
        return "High"
    else:
        return "Very High"
        
        
interface()
