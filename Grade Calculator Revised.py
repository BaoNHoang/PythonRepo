def user_input():
    grade_cat_and_grade = {}
    grade_category = []
    data = True
    n = 0
    num = 0
    while data:
        n += 1
        grade_cat = input(f'Enter grade category {n}: ')
        grade_category.append(grade_cat)
        grade = (input(f' Enter the grade(s) within (Do not use commas) {grade_cat}: '))
        gradeList = grade.split()
        grade_in_cat = [float(i) for i in gradeList]
        grade_cat_and_grade[grade_category[num]] = grade_in_cat
        continuinty = input('Would you like to add another category? (Yes or No) ')
        continuinty.lower()
        if continuinty == 'yes':
            data = True
            num += 1
        else:
            data = False
    return grade_cat_and_grade
def calculations():
    inputs = user_input()
    grades = []
    finalPercentWorths = []
    for i in inputs:
        grade = sum(inputs[i]) / len(inputs[i])
        print(f'Grade Category: {i} Average Grade: {grade:.2f}%')
        percentWorth = float(input(f'How much is {i} weighed? '))
        finalPercentWorths.append(percentWorth)
        finalPercentKeys = grade * (percentWorth / 100)
        grades.append(finalPercentKeys)
    finalGrade = (sum(grades) / sum(finalPercentWorths)) * 100
    return f'{finalGrade:.2f}%'

def letter_association():
    pass

if __name__ == '__main__':
    print(f"{'|Class Grade Calculator|' : ^50}")
    print('How to use:')
    print('Enter the categories of your grade book followed by a series of grades separated by a space.')
    print('Once all have been entered, add the percentage weight of the following(s) to complete the calculation.')
    user_choice = input('Hello user, would you like to begin? (Yes or No)\n ')
    user_choice.lower()
    if user_choice == 'yes':
        print(f'Final Grade: {calculations()}')
    else:
        print('Have a good day!')
