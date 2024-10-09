# main function
def main():
    # ask the user for the answer to the Great Question
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    if correct_answer(answer):
        print("Yes")
    else:
        print("No")
# function will evaluate the answer using if statements
def correct_answer(a):
    return True if a == "42" or a == "forty two" or a == "forty-two" else False
main()
