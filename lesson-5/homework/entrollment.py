universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats():
    students = [ uni[1] for uni in universities]
    tuition = [ uni[2] for uni in universities]
    return students, tuition
def mean(values):
    return sum(values) / len(values)
def median(values):
    sorting = sorted(values)
    n = len(sorting)
    middle = n // 2
    if n % 2 == 0:
        return (sorting[middle] + sorting[middle-1]) / 2
    else:
        return sorting[middle]


students, tuition = enrollment_stats()
total_students = sum(students)
total_tuiition = sum(tuition)
mean_of_stud = mean(students)
mean_of_tui = mean(tuition)
median_of_stud = median(students)
median_of_tui = median(tuition)
print(f"""
          total students: {total_students}
          total tuition fee: ${total_tuiition}

          mean of students: {mean_of_stud:.2f}
          median of students: {median_of_stud}
          

          mean of tuition fee: ${mean_of_tui:.2f}
          median of tuition fee: ${median_of_tui} 
 """)