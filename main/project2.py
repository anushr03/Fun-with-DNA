'''------------------------------------------------------
                 Import Modules 
---------------------------------------------------------'''
import dna_tool as dna

'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
print("==========================================")
print("DNA \"Analyzer\" and Patient Management Tool")
print("==========================================\n")
# initializing the list of patients
# list_pat=[]
patients = dna.initialize()
condition = ""  # stores the condition from the user when option 7 is called
while True:
    dna.display_menu()  # displays the menu that contains all the options
    command = input("Command (Enter to exit):")

    if command == "":  # to exit the program
        print("Thanks for using this tool")
        print("Come back soon!\n")
        break

    elif command == "1":  # prints the list of patients in the database
        dna.display(patients, condition)

    elif command == "2":  # prints various statistics via the patient list
        dna.info(patients, condition)

    elif command == "3":  # removes the desired patient from the list
        index = int(input("Who do you want to remove (enter number): "))
        if 1 <= index <= len(patients):
            del(patients[index-1])

    elif command == "4":  # add a new patient to the list
        patients = dna.add_new_patient(patients)

    elif command == "5":  # returns the compared strand between two patients
        index1 = int(input("First patient (enter number): "))
        index2 = int(input("second patient (enter number): "))

        # checking for input actually present in the patients list
        if (0 < index1 <= len(patients)) and (0 < index2 <= len(patients)):
            # send the two type Patient and returns the strand with similar BASE
            new_strand = dna.compare(patients[index1-1], patients[index2-1])
            print("Patients " + str(index1) + " and " + str(index2) + " common strand is " + new_strand)
            percent = dna.check_completeness(new_strand)
            print("They are similar at " + str(percent) + "%")

    elif command == "6":  # calls the compare_all function which compares all patients and prints data
        dna.compare_all(patients)

    elif command == "7":  # accepts a new condtion and makes necessary changees to the Patient List
        condition = input("Which condition are you looking for: ")
        sequence = input("Enter Sequence: ")
        pattern = dna.find_pattern(patients, sequence)
        print("Patients with " + condition + " condition: " + str(pattern/len(patients)*100) + "%")




