import random

questions = {
    "name": "What is your name? ",
    "age": "How old are you? ",
    "color": "What is your favorite color? ",
    "food": "What is your favorite food? ",
    "city": "Which city do you live in? ",
    "shs": "Which SHS did you attend? ",
    "team": "What is your favorite soccer team? ",
    "hobby": "What is your favorite hobby? ",
    "movie": "What's your favorite movie? ",
    "book": "What's your favorite book? "
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
    name = answers.get('name', 'Friend')
    age = answers.get('age', 'N/A')
    city = answers.get('city', 'somewhere')
    color = answers.get('color', 'N/A')
    food = answers.get('food', 'N/A')
    shs = answers.get('shs', 'an SHS')
    team = answers.get('team', 'a team')
    hobby = answers.get('hobby', 'a hobby')
    movie = answers.get('movie', 'N/A')
    book = answers.get('book', 'N/A')

    summary = (
        "==============================\n"
        "       PERSONAL SUMMARY\n"
        "==============================\n\n"
        f"Hello, {name}!\n"
        f"You are {age} years old and live in {city}.\n"
        f"Your favorite color is {color}, and you enjoy eating {food}.\n"
        f"You attended {shs} and support {team}.\n"
        f"In your free time, you enjoy {hobby}.\n"
        f"Your favorite movie is '{movie}', and your favorite book is '{book}'.\n"
    )
    return summary

def get_rating():
    while True:
        try:
            rating = int(input("How would you rate this assistant? (1 to 5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(summary)
            file.write(f"\nRating: {rating} star{'s' if rating > 1 else ''}\n")
        print(f"\nSummary saved to '{filename}'.")
    except Exception as e:
        print(f"Failed to save file: {e}")

def main():
    while True:
        print("\nWelcome to the Profile Assistant\n")
        answers = ask_questions()
        summary = create_summary(answers)

        print("\nHere is your personalized summary:\n")
        print(summary)

        rating = get_rating()

        save = input("Do you want to save this summary to a .txt file? (yes/no): ").strip().lower()
        if save == "yes":
            save_to_file(answers["name"], summary, rating)
        else:
            print(f"\nYour rating ({rating}/5) has been noted. Thank you!")

        restart = input("\nDo you want to restart the process? (yes/no): ").strip().lower()
        if restart != "yes":
            print("\nThank you for using the assistant. Goodbye!")
            break

if __name__ == "__main__":
    main()
