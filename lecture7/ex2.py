performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

avg_scores = {}
department_averages = {}

print("Summary Report:")

for department, employees in performance_data.items():
    print(f"Department: {department}")
    avg_scores[department] = {}
    total_score = 0
    count = 0
    top_employee = None
    top_score = 0
    
    for employee, scores in employees.items():
        avg = sum(scores) / len(scores)
        avg = round(avg, 2)
        avg_scores[department][employee] = avg
        print(f"{employee}: Average Score = {avg:.2f}")
        
        if avg > top_score:
            top_score = avg
            top_employee = employee
        total_score += avg
        count += 1
        
    dept_avg = total_score / count
    department_averages[department] = dept_avg
    print(f"Top Performer: {top_employee} with Average Score = {top_score:.2f}\n")
    
best_dept = max(department_averages, key=department_averages.get)
best_avg = department_averages[best_dept]
print(f"Best Department: {best_dept} with Average Score = {best_avg:.2f}")
