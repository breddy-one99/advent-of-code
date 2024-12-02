# day 2 part 1

with open('input.txt', 'r') as file:
    puzzle_data = [list(map(int, line.split())) for line in file if line.strip()]

safe_reports = 0

for report in puzzle_data:
    safe_num = 0
    if sorted(report) == report:
        for i in range(0, len(report) - 1):
            if report[i + 1] - report[i] >= 1 and report[i + 1] - report[i] <= 3:
                safe_num += 1
        if safe_num == len(report) - 1:
            safe_reports += 1 

    if sorted(report, reverse=True) == report:
        for i in range(0, len(report) - 1):
            if report[i] - report[i+1] >= 1 and report[i] - report[i+1] <= 3:
                safe_num += 1
        if safe_num == len(report) - 1:
            safe_reports += 1 
                
            
print(safe_reports)