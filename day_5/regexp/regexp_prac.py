import re


def find_digit(str_val):
    pattern = re.compile("\\d+")
    val = pattern.findall(str_val)
    print(val)


def prac_q_1(date_str):
    """
    Input: "2026-01-19"
    Output: year=2026, month=01, day=19
    """
    pattern = r"([\d]{4})-([\d]{2})-([\d]{2})"
    matched = re.search(pattern, date_str)
    year, month, day = matched.groups()
    print(f"year={year}, month={month},day={day}")

def prac_q_2(ph_num):
    pattern = r"\+([\d]{2})-([\d]{10})"
    matched = re.search(pattern,ph_num)
    country,number = matched.groups()
    print(f"country={country}, number={number}")

def prac_q_3(link):
    pattern = r"(?P<ip>[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}):(?P<port>[\d]{4,4})"
    matched = re.search(pattern,link)
    print(matched.groupdict())
if __name__=="__main__":
    # find_digit("12afdv34 3")
    #prac_q_1("2026-01-19")
    #prac_q_2("+91-9876543210")
    prac_q_3("192.168.1.1:8080")

