 
"""f1 = int(input("maths marks : "))
f2 = int(input("hindi marks : "))
f3 = int(input("science marks : "))
f4 = int(input("english marks : "))
f5 = int(input("sst marks : "))
f6 = int(input("computer marks : "))
f7 = int(input("music marks : "))
a = [f1,f2,f3,f4,f5,f6,f7]
b = sum(a)
c = (b/700) * 100
print(f"here your percentage: {c}")"""


subjects = ["Maths", "Hindi", "Science", "English", "SST", "Computer", "Music"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = int(input(f"{subject} marks: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

total = sum(marks)
percentage = (total / 700) * 100
print(f"Here is your percentage: {percentage:.2f}%")


