
from random import choice, randint
from btu.data import b_names, g_names, last_names, subject

# ქვედა ლუპში ვაგენერირებ 1000 სახელ და გვარს (500 ბიჭი, 500 გოგო)
full_names = []
for count in range(1000):
    if count < 500:   # პირველი ნახევარი ბიჭია
        name = choice(b_names) + " "
        last_name = choice(last_names)
        full_names.append(name + last_name)
    else:   # მეორე ნახევარი გოგოა
        name = choice(g_names) + " "
        last_name = choice(last_names)
        full_names.append(name + last_name)
# print(full_names)


# ქვედა ლუპში ვამაგრებ სტუდენტებს საგნებს და შეფასებებს
students_with_data = []
for count in range(100):  # ტესტირებისთვის გირჩევთ რაოდენობა შეამციროთ ^^
    student = {'full_name': choice(full_names), 'subject': choice(subject), 'score': randint(1, 100)}
    students_with_data.append(student)
print(students_with_data)


# ქვედა ლუპში თითოეული სტუდენტის მონაცემებს ვმერჯავ და ქულებს ვაერთიანებ საგნის ლისთში
students_with_data_organized = []
for student in students_with_data:
    student_all_data_list = list(filter(
        lambda student_dict: student_dict['full_name'] == student['full_name'],
        students_with_data
    ))

    score_per_subject = {}
    for data in student_all_data_list:
        if data['subject'] not in score_per_subject:  # ვამატებ საგანს თუ აქამდე არ იყო დიქშენერში
            score_per_subject[data['subject']] = []

        if data['subject'] in score_per_subject:  # თუ საგანი არსებობს ვამატებ მასში კონკრეტულ შეფასებას
            score_per_subject[data['subject']].append(data['score'])

    student_all_data_list_merged = {'full_name': student['full_name'], 'subject': score_per_subject}
    students_with_data_organized.append(student_all_data_list_merged)
# print(students_with_data_organized)


# ქვედა ლუპში ვითვლი თითოეული სტუდენტის საგნების ქულებიდან საშუალო არითმეტიკულს
students_with_avg = []
for student in students_with_data_organized:
    student['avg'] = {}

    for key, value in student['subject'].items():
        student['avg'][key] = round(sum(value) / len(value))

    students_with_avg.append(student)
# print(students_with_avg)


# ქვედა ლუპში ვთვლი ყველა საგნის საშუალოდან საშუალო არითმეტიკულს (GPA)
students_with_gpa = []
for student in students_with_avg:
    student['gpa'] = round(sum(student['avg'].values()) / len(student['avg'].values()))
    students_with_gpa.append(student)

# print(student_with_gpa)

# ქვედა ლუპში ვინახავ ყველაზე მაღალი საერთო საშუალო ქულის (GPA) მქონე სტუდენტს
student_with_highest_gpa = {'full_name': '', 'gpa': 0}
for student in students_with_gpa:
    if student['gpa'] > student_with_highest_gpa['gpa']:
        student_with_highest_gpa['gpa'] = student['gpa']
        student_with_highest_gpa['full_name'] = student['full_name']

print('ყველაზე მაღალი GPA ის მქონე სტუდენტი: {} GPA: {}'.format(
    student_with_highest_gpa['full_name'], student_with_highest_gpa['gpa']
))
