def create_database_entry(patient_name, id_no, age): 
    new_patient = [patient_name, id_no, age, []] #leaves a space for a list within the list for testing 
    return new_patient
   

def print_database(db): 
    locations = ["room 1", "room 4", "ER", "Post-op"]
    for patient, location in zip(db, locations):
       print("{} - {}".format(patient, location))
       
       
def age_comp(db): 
    for patient in db:
        if patient[2] > age:
            print(patient[0])

def get_patient(db,id_no): 
    for patient in db:
        if patient[1] == id_no:
            return patient

def main(): 
    db = []
    x = create_database_entry("Ann Ables",1,30)
    db.append(x)
    x = create_database_entry("Bob Boyles",2,10)
    db.append(x)
    x = create_database_entry("Chris Chou",3,33)
    db.append(x)
    x = create_database_entry("David Dinkins",4,33)
    db.append(x)
    
   
    #y = db[1] #what is the second entry in database
    #g = db[-1] #What is the last entry in the database 
    #z = db[0:2] #elements one to three, not including three
    
    #How to append data from a test to a specific patient
    patient_id_tested = 2 
    test_done = ("HDL", 65)
    patient = get_patient(db,patient_id_tested)
    patient[3].append(test_done)
    print_database(db)
    
    
if __name__ == "__main__":
    main() 
    