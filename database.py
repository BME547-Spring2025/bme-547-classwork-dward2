def load_patient_data_file(filename):
    in_file = open(filename, 'r')
    data = in_file.readlines()
    in_file.close()
    return data
    

def load_patient_data_file_singles(filename):
    with open(filename, 'r') as in_file:
        data = []
        headers = in_file.readline()
        for line in in_file:
            data.append(line)
    return data
    
    
def main():
    data = load_patient_data_file_singles("patient_data.txt")
    print(data)
    
    
if __name__ == "__main__":
    main()
