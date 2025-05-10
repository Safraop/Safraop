 



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


