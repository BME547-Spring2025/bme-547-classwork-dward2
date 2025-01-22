print("This is the db_temp module")
print("Python thinks module is called {}".format(__name__))


import blood_analysis as ba
import othercode as oc

HDL = 55
test_ranges = {"Normal": (60, 1000),
                   "Borderline Low": (40, 59),
                   "Low":(0, 39)}
                   
answer = ba.analyze_generic_result(HDL, test_ranges)



print("HDL is {}".format(answer))

my_input = get_generic_test_result("My test")

oc.do_work

