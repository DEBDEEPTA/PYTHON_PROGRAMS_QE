import csv
def prac_q_1(csv_path,filterred_csv_path):
    """Read employees.csv and create it_employees.csv containing only employees from IT department."""
    filtered_data = []
    with open(csv_path, "r") as file_obj:
        reader_data = csv.DictReader(file_obj)

        for rows in reader_data:
            if(rows["department"] == "IT"):
                filtered_data.append(rows)



if __name__=="__main__":
    csv_path = "employee.csv"
    new_csv_path = "it_employee.csv"
    prac_q_1(csv_path,new_csv_path)