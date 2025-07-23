import random


questions = {
    "name": "What is your name? ",
    "age": "How old are you? ",
    "color": "What is your favorite color? ",
    "food": "What is your favorite food? ",
    "city": "Which city do you live in? ",
    "shs": "Which SHS did you attend? ",
    "team": "What is your favorite soccer team? "
}

def ask_questions():
    keys = list(questions.keys())
    random.shuffle(keys)  

    answers = {}
    for key in keys:
        answer = input(questions[key])
        answers[key] = answer
    return answers

def create_summary(answers):
    summary = (
        f"\nHello, {answers['name']}! You are {answers['age']} years old, "
        f"You love the color {answers['color']}, and enjoy eating {answers['food']}. "
        f"Life must be awesome in {answers['city']}!\n"
        f"You attended {answers['shs']} and support {answers['team']}.\n"
    )
    return summary

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    with open(filename, 'w') as file:
        file.write(summary)
        file.write(f"Rating: {rating} stars\n")
    print(f"✅ Summary saved to {filename}\n")

def main():
    while True:
        print("\n🎉 Welcome to the Fun Profile Assistant 🎉")
        answers = ask_questions()
        summary = create_summary(answers)
        print("\n📋 Here's your summary:")
        print(summary)

        save = input("Do you want to save this summary to a .txt file? (yes/no): ").strip().lower()
        if save == "yes":
            while True:
                try:
                    rating = int(input("Rate this assistant from 1 to 5 stars: "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            save_to_file(answers["name"], summary, rating)

        restart = input("Do you want to restart the process? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thanks for using the assistant. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
