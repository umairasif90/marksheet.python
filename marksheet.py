total=425
print("     =====Enter obtained Marks=====    ")
comp = int(input('Enter Computer Marks: '))
chemistry = int(input('Enter Chemistry Marks: '))
pst = int(input('Enter PST Marks:'))
english = int(input('Enter English Marks:'))
sindhi = int(input('Enter Sindhi Marks:'))
sum = comp + chemistry + pst + english + sindhi
print('Your Total Obtained Marks Are:',sum)
percentage = sum / total * 100
print('Your Percentage Is:',percentage)
if percentage >= 80:
    print("Your Grade Is A+")
elif percentage >=70 and percentage <80:
    print("Your Grade Is A")
elif percentage >=60 and percentage <70:
    print("Your Grade Is B")
elif percentage >=50 and percentage <60:
    print("Your Grade Is C")
elif percentage >=40 and percentage <50:
    print("Your Grade Is D")
else:
    print("You Failed.")
