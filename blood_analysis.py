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
    test_ranges = {"Normal": (60, 1000),
                   "Borderline Low": (40, 59),
                   "Low":(0, 39)}
    hdl_class = analyze_generic_result(hdl_result, test_ranges)
    output_generic_test_result(test_name, hdl_result, hdl_class)
    
    
def get_generic_test_result(test_name):
    test_value = input("Enter the {} test result: ".format(test_name))
    test_value = int(test_value)
    return test_value
        
def analyze_generic_result(test_value, test_ranges):
    for category in test_ranges:
        min_value = test_ranges[category][0]
        max_value = test_ranges[category][1]
        if min_value <= test_value <= max_value:
            return category
    return "Out of Range"

def output_generic_test_result(test_name, test_result, test_class):
    print("For a(n) {} value of {}, the result is {}".format(test_name,
                                                            test_result,
                                                            test_class))
                                                            
def ldl_analysis():
    test_name = "LDL"
    ldl_result = get_generic_test_result(test_name)
    test_ranges = {"Normal": (0, 129),
                   "Borderline High": (130, 159),
                   "High": (160, 189),
                   "Very High": (190, 1000)}
    ldl_class = analyze_generic_result(ldl_result, test_ranges)
    output_generic_test_result(test_name, ldl_result, ldl_class)
    
        
interface()
