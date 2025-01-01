# contents = ["no comment dh",
#             "contest ugribugri",
#             "kofejto es libego"]
# filenames = ["dh.txt", "fr.txt", "en.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", "w")
#     file.write(content)

# file = open("file.txt", "w")
# text = file.writelines("snail")
# file.close


# newmember = input("Add a new member: ")
# file = open("members.txt", "r")
# content = file.readlines()
# file.close()
#
# content.append(newmember + "\n")
#
# file = open("members.txt", "w")
# file.writelines(content)
# file.close()

# filenames = ['doc.txt', 'report.txt',
#              'presentation.txt']
#
# for names in filenames:
#     file = open(names,"w")
#     file.write("Hello")
#     file.close()

# filenames = ['a.txt', 'b.txt',
#              'c.txt']
#
# for names in filenames:
#     file = open(names,"r")
#     content = file.read()
#     print(content)
#     file.close()

# file = open("data.txt", 'w')
#
# file.write("100.12" + "\n")
# file.write("111.23")
#
# file.close()


# filenames = ['doc', 'report', 'presentation']
# newnames = [f"{names}.txt" for names in filenames]
# print(newnames)

# filenames = ['1.doc', '2.report', '3.presentation']
# newnames = [names.replace(".", "-") + ".txt" for names in filenames]
# print(newnames)

# temperatures = [10, 12, 14]
# temperatures = [str(i) + "\n" for i in temperatures]
#
# file = open("fileone.txt", 'w')
#
# file.writelines(temperatures)
#
# file.close()


#     #pw checker own 1.0
# pw = input("Add pw: ")
# if len(pw) > 6:
#     upp = any(car.isupper() for car in pw)
#     if upp: #no need upp == True
#         nb = any(car.isdigit() for car in pw)
#         if nb: #no need nb == True
#             print("Strong pw")
#         elif nb == False: print("Nb pls")
#     elif upp == False: print("Upp pls")
# elif len(pw) <= 6: print("Need more")


#     #pw checker dict
# result = {}
#
# pw = input("PW: ")
# if len(pw) > 8:
#     result["length"] = True
# else:
#     result["length"] = False
#
# upper = any(p.isupper() for p in pw)
# result["upper"] = upper
#
# number = any(p.isdigit() for p in pw)
# result["number"] = number
#
# print(result)
# if all(result.values()):
#     print("Strong")
# else:
#     print("Weak")


# #avg calc
# def avg_calc():
#     with open("b.txt", "r") as file_local:
#         content = file_local.readlines()
#         new_content = content[1:]
#         new_content = [float(i) for i in new_content]
#         average_local = sum(new_content) / len(new_content)
#     return average_local
#
# print(avg_calc())

# list avg function
# def avg(numbers_list=[]):
#     newnumbers_list = [float(i) for i in numbers_list]
#     result = sum(newnumbers_list) / len(newnumbers_list)
#     return result

# def speed(distance, time):
#     return distance / time
# print(speed(200, 4))


# #feet and inch converter
# feet_inches = input("Enter feet and inches: ")
#
# def parse(feetinches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return feet, inches
#
# def converter(feet, inches):
#     meter = float(feet) * 0.3048 + float(inches) * 0.0254
#     return meter
#
# f, i = parse(feet_inches)
# print(f, i)
# meters = converter(f, i)
# print(meters)
#
# if meters < 1:
#     print("Too small")
# else: print("Ok")


# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(100)
# print(time)

# #check files
# import glob
# myfiles = glob.glob("*.txt")
# print(myfiles)

# #check all txt content
# import glob
# myfiles = glob.glob("*.txt")
# for path in myfiles:
#     with open(path, "r") as file:
#         print(file.read())

# #csv manipulation
# import csv
# with open("../files/weather.csv", "r") as file:
#     data = list(csv.reader(file))
#
# city = input("Write city: ")
#
# for row in data[1:]:
#     if row[0] == city:
#         print(row[1])

# #shutil
# import shutil
# shutil.make_archive("output", "zip", "files")

# #webbroser
# import webbrowser
# user_term = input("search: ")
# webbrowser.open("https://www.google.com/search?q=" + user_term)

# #random number creator
# import random
# low = int(input("Please enter low range: "))
# high = int(input("Please enter high range: "))
# number = random.randrange(low, high)
# print(number)


import FreeSimpleGUI as sg

# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1')],
                       [sg.Text('Left 2')]]

# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Text('Right 2')]]

# Construct the Column widgets
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

# Construct the layout
layout = [[left_column, right_column]]

# Construct and display the window
window = sg.Window('Columns', layout)
window.read()
window.close()