
def create_employee():
    id = int(input("Enter Employee Id -> "))
    name = input("Enter employee name -> ")
    daily_wrk_hrs = []
    # DAILY WORKING HOURS
    for day in range(1, 8):
        while True:
                try:
                    hrs = int(input(f"Enter Working Hours for day-{day}"))
                    if(hrs < 0):
                        raise ValueError("hours Can't be negative")
                except ValueError:
                    print("Not a integer Value")
                else:
                    daily_wrk_hrs.append(hrs)
                    break

    # WAGE PER HOURS
    while True:
        try:
            sal_per_hrs = int(input("Enter Salary/hrs ->"))
            if sal_per_hrs < 0:
                raise ValueError("Wage Cant Be Less negative")
        except ValueError:
                print("Not a integer value")
        else:
            break

    empl_dict = {
        "id": id,
        "name":name,
        "daily_wrk_hrs":daily_wrk_hrs,
        "sal_per_hrs":sal_per_hrs
    }

    return empl_dict

def wage_calculater(emplyee_list):
    pass



if __name__=="__main__":

    emp_nums = int(input("Enter number of Employees\n"))
    empl_list = []
    for i in range(emp_nums):
        emp_details_dict = create_employee()
        empl_list.append(emp_details_dict)

    wage_calculater(empl_list)






