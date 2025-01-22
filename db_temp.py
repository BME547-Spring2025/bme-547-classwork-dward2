print("This is the db_temp module")
print("Python thinks module is called {}".format(__name__))



import blood_analysis


HDL = 55
test_ranges = {"Normal": (60, 1000),
                   "Borderline Low": (40, 59),
                   "Low":(0, 39)}
                   
answer = blood_analysis.analyze_generic_result(HDL, test_ranges)

print("HDL is {}".format(answer))
