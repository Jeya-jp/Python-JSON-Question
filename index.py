def insertContent():
        f = open("Data.json", "a")

        print("Enter the id: ")
        id = input()
        f.write("{\n")
        f.write(R'"id": "' + id + R'",')

        print("Enter the question: ")
        question = input()
        f.write("\n")
        f.write(R'"question": "' + question + R'",')
        f.write("\n" + R'"options": ' + "\n{")

        print("Enter the option [ A ]: ")   
        A = input()
        f.write("\n")
        f.write(R'"A": "' + A + R'",')

        print("Enter the option [ B ]: ")
        B = input()
        f.write("\n")
        f.write(R'"B": "' + B + R'",')

        print("Enter the option [ C ]: ")
        C = input()
        f.write("\n")
        f.write(R'"C": "' + C + R'",')

        print("Enter the option [ D ]: ")
        D = input()
        f.write("\n")
        f.write(R'"D": "' + D + R'"' + "\n},")

        print("Choose the correct answer: ")
        answer = input()
        f.write("\n")
        f.write(R'"answer": "' + answer + R'",')

        print("Enter the explanation: ")
        explain = input()
        f.write("\n")
        f.write(R'"explanation": "' + explain + R'"' + "\n},\n")

        f.close()
print("Enter how many questions: ")
num = int(input())
for i in range (num):
    insertContent()