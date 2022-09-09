#Import modules
from Patient import Patient
import random

#initialize global variable
random.seed(5)  # random seed used for reproducibility
LENGTH_DNA=20


########################
##### Functions ########
########################

def display_menu():
    """ Display all the options, no input, no output """
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")


def random_base():
    """select the letter A,C,G,T at random, output (String) """
    bases=["A", "C", "G", "T"]
    return random.choice(bases)


### to complete
def random_strand():
    """returns a random str dna by calling random_base()"""
    d = ""
    for i in range(LENGTH_DNA):
        d += random_base()
    return d

def initialize():
    """Initializing the first 16 patients in the list"""
    name = "Andrea"
    age = "37"
    dna = random_strand()
    p1 = Patient(name, age, dna)

    name = "Bob"
    age = 28
    dna = random_strand()
    p2 = Patient(name, age, dna)

    name = "Brooke"
    age = 34
    dna = random_strand()
    p3 = Patient(name, age, dna)

    name = "Connor"
    age = 27
    dna = random_strand()
    p4 = Patient(name, age, dna)

    name = "James"
    age = 25
    dna = random_strand()
    p5 = Patient(name, age, dna)

    name = "Jenna"
    age = 44
    dna = random_strand()
    p6 = Patient(name, age, dna)

    name = "John"
    age = 45
    dna = random_strand()
    p7 = Patient(name, age, dna)

    name = "Julie"
    age = 37
    dna = random_strand()
    p8 = Patient(name, age, dna)

    name = "Kate"
    age = 48
    dna = random_strand()
    p9 = Patient(name, age, dna)

    name = "Keith"
    age = 28
    dna = random_strand()
    p10 = Patient(name, age, dna)

    name = "Kelly"
    age = 25
    dna = random_strand()
    p11 = Patient(name, age, dna)

    name = "Luke"
    age = 33
    dna = random_strand()
    p12 = Patient(name, age, dna)

    name = "Mark"
    age = 34
    dna = random_strand()
    p13 = Patient(name, age, dna)

    name = "Pat"
    age = 26
    dna = random_strand()
    p14 = Patient(name, age, dna)

    name = "Taylor"
    age = 30
    dna = random_strand()
    p15 = Patient(name, age, dna)

    name = "Tony"
    age = 55
    dna = random_strand()
    p16 = Patient(name, age, dna)

    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]



def display(patients, condition):
    """displaying the list of patients in the list"""
    j = 1
    print("\tName\tage\tDNA-strand (20 length)\t",condition)
    print("----------------------------------------------------------------")

    if not condition:  # will not print out condition column if its empty
        for i in patients:
            print(str(j) + "\t" + i.name + "\t" + str(i.age) + "\t" + i.strand)
            j += 1
    else:
        for i in patients:
            print(str(j)+"\t"+i.name+"\t"+str(i.age)+"\t"+i.strand + "\t" + str(i.has_condition))
            j += 1


def info(patients, condition):
    """prints out the percentage of patients in each age gap"""
    u20 = 0
    twenty = 0
    thirty = 0
    fourty = 0
    fifty = 0
    o60 = 0
    sum_age = 0
    l = len(patients)
    for i in patients:
        sum_age += int(i.age)
        if int(i.age) < 20:
            u20 += 1
        elif 20 <= int(i.age) < 30:
            twenty += 1
        elif 30 <= int(i.age) < 40:
            thirty += 1
        elif 40 <= int(i.age) < 50:
            fourty += 1
        elif 50 <= int(i.age) < 60:
            fifty += 1
        elif int(i.age) >= 60:
            o60 += 1

    #  Calculating the percentage of each age group
    u20f = float((u20/l)*100)
    twentyf = float((twenty/l) * 100)
    thirtyf = float((thirty / l) * 100)
    fourtyf = float((fourty / l) * 100)
    fiftyf = float((fifty / l) * 100)
    o60f = float((o60 / l) * 100)

    #  printing the info
    print("#Patients " + str(len(patients)))
    print("<20: " + str(u20f) + "%")
    print("20's: " + str(twentyf) + "%")
    print("30's: " + str(thirtyf) + "%")
    print("40's: " + str(fourtyf) + "%")
    print("50's: " + str(fiftyf) + "%")
    print(">=60: " + str(o60f) + "%\n")
    print("Age Mean: " + str(float(sum_age/l)))

    #  to get the number of patients with the condtions and print out the number
    if condition:
        count = 0
        for i in patients:
            if i.has_condition:
                count += 1
        print(condition + ":", str(count/len(patients)*100), "%")


def add_new_patient(patients):
    """returns a new patient list with the new patient attributes"""
    name = input("Enter Name: ")
    while True:
        try:
            age = int(input("Enter Age:"))
        except ValueError:
            continue
        else:
            break
    count = 0

    while True:
        strand = input("DNA strand: ")
        for i in strand:
            if i == 'A' or i == 'G' or i == 'T' or i == 'C':
                count += 1
        if count == LENGTH_DNA:
            break
        else:
            print("Bad input! -length must be 20")
    p_new = Patient(name, age, strand)

    return patients+[p_new]

def compare(p1, p2):
    """Compares the two strands and returns a new strand"""
    temp_strand = ""
    p1_strand = p1.strand
    p2_strand = p2.strand
    for i in range(len(p1.strand)):
        # Simply comparing the character at position i of one strand with the character at the same position in strand 2
        if p1_strand[i] == p2_strand[i]:
            temp_strand += p1_strand[i]
        else:
            temp_strand += 'x'

    return temp_strand

def check_completeness(strand):
    """returns the similarity percentage of the new_strand. """
    count = 0
    for i in strand:
        if i == 'x':
            count += 1

    count = LENGTH_DNA - count  #  subtracting the number of x's from the actual length, which are the total number of equal bases
    return float((count/len(strand)) * 100)

def compare_all(p):
    """Compares each patient with another and prints the similarity if <33%"""
    for i in range(len(p)):
        for j in range(i):
            simi_strand = compare(p[i], p[j])  # stores the value of the compared string b/w patients at index i and j
            comparision_percent = check_completeness(simi_strand)  # stores the percent b/w the two patients from the previous line
            if comparision_percent > 33:
                print(p[i].name, "vs", p[j].name, comparision_percent,"%")

def find_pattern(p_list, sequence):
    """Looks for the sequence in each strand, sets the has_attribute condition for Patient object and returns the count"""
    count = 0
    for i in range(len(p_list)):
        for j in range(LENGTH_DNA):
            if p_list[i].strand[j:j+3] == sequence:
                p_list[i].has_condition = True
                count += 1
                break
            else:
                p_list[i].has_condition = False


    return count


##########################
########## Main Function #  to uncomment step by step fo testing
##########################
                
def main():
    print("TEST FOR OPTION 1")
    print("\n****TEST the random_strand function****")
    print(random_strand())

    #################### TEST FOR OPTION 1
    print("\n****TEST the class Patient****")
    patient=Patient("Tom",20,random_strand())
    print(patient.name,patient.age,patient.strand)
    
    #################### TEST FOR OPTION 1
    print("\n****TEST the display function****")
    patients=[patient,Patient()]
    patients[1].name="Lucy"
    patients[1].age=25
    patients[1].strand="TCTTGTAAACTCGGAAACTG"
    display(patients)

    #################### TEST FOR OPTION 2
    print("\n****TEST the info function****")
    info(patients)

    # ##################### TEST for OPTION 4
    # print("\n****TEST the add_new_patient function****")
    # patients=add_new_patient(patients)
    # display(patients)
    
    ##################### TEST for OPTION 5
    print("\n****TEST the compare function****")
    common_strand=compare(patients[0],patients[1])
    print(common_strand)

    ##################### TEST for OPTION 5
    print("\n****TEST the check_completness function****")
    print(check_completeness(common_strand))

    


if __name__=="__main__":
    main()
    
