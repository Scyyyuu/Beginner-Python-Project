def compute_average(*average):
    Total = 0
    for x in average:
        Total += x
    count = len(average)
    return Total /count 


def get_remark(average):
    if average >= 75:
        return "Passed"
    return "Failed"


def report_card(name, *grades, **info):
    average = compute_average(*grades)

    print("Name:", name)
    for key, value in info.items():
        print(f"{key.title()}: {value}")
    print("Grades:", *grades)
    print("Average:", average)
    print("Remark:", get_remark(average))

report_card("Paul", 90, 85, 78, 92, course="BSIT", section="IT1C")