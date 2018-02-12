# Trivia Challenge
# Trivia game that reads a plain text file
#Teresa Luz miller
import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode,encoding='utf-8')
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    point_value = 0
    question = next_line(the_file)
    
    answers = []
    answers.append(next_line(the_file))

    if( answers[0]=="True\n"):
        answers.append(next_line(the_file))
    else:
        for i in range(4):
            answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        point_value = (int)(next_line(the_file).strip())
    explanation = next_line(the_file) 

    return category, question, answers, correct, score, explanation, point_value

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, score, explanation, point_value = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        i=0
        for a in answers:
            print ("\t", i + 1, "-", a)
            i = i + 1        # get answer

        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, score, explanation, point_value = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

main() 
input("\n\nPress the enter key to exit.")
