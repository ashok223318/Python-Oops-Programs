class Patient:
    def __init__(self,pat_id,pat_name,pat_age,disease,doc_name):
        self.pat_id = pat_id
        self.pat_name= pat_name
        self.pat_age = pat_age
        self.disease = disease
        self.doc_name = doc_name
        
    def display(self):
        print("\n~~~~~~~ Patient Details ~~~~~~~~~")
        print("Patient ID:",self.pat_id)
        print("Patient Name:",self.pat_name)
        print("Patient Age:",self.pat_age)
        print("Patient Disease:",self.disease)
        print("Doctor:",self.doc_name)
        
    def update_disease(self,new_disease):
        self.disease = new_disease
        print("Disease Updated Successfully")
        print("New Disease is:",self.disease)
        
    def change_doc(self,new_doc):
        self.doc_name = new_doc
        print("Doctor Changed")
        print("New Doctor is:",self.doc_name)
        
    def patient_details(self):
        self.display()
        
        
pat = Patient(241063,"Koushik",20,"Fever","Dr.Samaram")

while True:
    
    print("\n~~~~~~~ Hospital Management System ~~~~~~~~")
    print("1. Display Patient Details")
    print("2. Update Disease")
    print("3. Change Doctor")
    print("4. Patient Full Details")
    print("5. Exit")
    print("6. Thank You")
    
    choice = int(input("Enter Your Choice:"))
    
    if choice == 1:
        pat.display()
        
    elif choice == 2:
        new_dis = input("Enter New Disease:")
        pat.update_disease(new_dis)
        
    elif choice == 3:
        new_doc = input("Enter New Docter Name:")
        pat.change_doc(new_doc)
        
    elif choice ==4:
        pat.patient_details()
        
    elif choice == 5:
        print("Exit")
        
    elif choice == 6:
        print("Thank you")
        break
        
    else:
        print("Invalid Choice")      
                    
    