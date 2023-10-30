student_index_no = 1
loop_increment = 0
Total_points_array = []
Total_credit_array = []
data_dict = {}

def data_calculate(sub_result, sub_credit): #Calculates total points for a subject and appends it to a list
        sub_result = sub_result.upper()
        if sub_result=="A+":
            Total_points=sub_credit*4
        elif sub_result=="A":
            Total_points=sub_credit*4
        elif sub_result=="A-":
            Total_points=sub_credit*3.7
        elif sub_result=="B+":
            Total_points=sub_credit*3.3
        elif sub_result=="B":
            Total_points=sub_credit*3
        elif sub_result=="B-":
            Total_points=sub_credit*2.7
        elif sub_result=="C+":
            Total_points=sub_credit*2.3
        elif sub_result=="C":
            Total_points=sub_credit*2
        elif sub_result=="C-":
            Total_points=sub_credit*1.7
        elif sub_result=="D+":
            Total_points=sub_credit*1.3
        elif sub_result=="D":
            Total_points=sub_credit*1
        elif sub_result=="E":
            Total_points=sub_credit*0
        else:
            Total_points = 0  
        Total_points_array.append(Total_points)
        Total_credit_array.append(sub_credit)

def input_data(student_index_no, GPA): #input student_index_no and GPA to a dictionary
    data_dict[student_index_no] = GPA
    print("Data inserted to dictionary.")

def search_data(): #search GPA relevant to the inserted index_no from a dictionary
    key = int(input("Enter the student index number to search for: "))
    if key in data_dict:
        print(f"Student Index No '{key}' has a GPA of {data_dict[key]}")
    else:
        print(f"Student Index No '{key}' not found in the dictionary.")

while student_index_no > 0:
    GPA_Decision_select = input("Do you want to calculate GPA (y/n) ").lower()
    if GPA_Decision_select == "y":
        student_index_no = int(input("Enter your index number: "))
        No_of_subjects = int(input("Enter the number of subjects: "))
        
        while No_of_subjects>loop_increment:
            loop_increment += 1
            sub_name = input(f"Enter subject {loop_increment} name: ")
            sub_result = input(f"Enter subject {loop_increment} result (e.g., A+): ")
            sub_credit = float(input(f"Enter subject {loop_increment} credit: "))
            data_calculate(sub_result, sub_credit)

        GPA = sum(Total_points_array) / sum(Total_credit_array)
        print(f"{student_index_no} - GPA: {GPA}")
        input_data(student_index_no, GPA)
    else:
        break

while True: #GPA searching loop
    GPA_Decision_search = input("Do you want to find a GPA (y/n): ").lower()
    if GPA_Decision_search == "y":
        search_data()
    elif GPA_Decision_search == "n":
        print("Exiting search.")
        break
    else:
        print("Invalid choice. Please enter 'y' to search or 'n' to exit.")

