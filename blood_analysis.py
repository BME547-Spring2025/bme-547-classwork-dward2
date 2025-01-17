def interface():
    print("Blood Analysis Menu")
    while True:
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter test to analyze: ")
        if choice == "9":
            break
        elif choice == "1":
            hdl_analysis()
    print("Exiting...")
    
def hdl_analysis():
    print("HDL")
    hdl_result = get_hdl_test_result()
    
def get_hdl_test_result():
    hdl_value = input("Enter the HDL test result: ")
    hdl_value = int(hdl_value)
    return hdl_value
        
interface()
