flavors = ["Strawberry", "Mango Sorbet", "Chocolate", "Vanilla"]
scores = [0, 0, 0, 0]  

def get_valid_input(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ['a', 'b', 'c', 'd']:
            return answer
        else:
            print("Invalid input. Please enter only a, b, c, or d.")

def ask_questions():
    print("Welcome to the Ice Cream Flavor Matcher!")
    print("Answer these fun summer questions to find your perfect summer ice cream match!\n")

    # Question 1
    print("1. What’s your favorite summer activity?")
    print("a) Swimming")
    print("b) Biking")
    print("c) Playing video games")
    print("d) Reading")
    q1 = get_valid_input("Your choice (a/b/c/d): ").lower()
    if q1 == "a":
        scores[0] += 1
    elif q1 == "b":
        scores[1] += 1
    elif q1 == "c":
        scores[2] += 1
    elif q1 == "d":
        scores[3] += 1

    # Question 2
    print("\n2. What’s your ideal summer vacation?")
    print("a) A trip to the beach")
    print("b) Camping in the forest")
    print("c) Stay home and play games")
    print("d) A quiet mountain getaway")
    q2 = get_valid_input("Your choice (a/b/c/d): ").lower()
    if q2 == "a":
        scores[0] += 1
    elif q2 == "b":
        scores[1] += 1
    elif q2 == "c":
        scores[2] += 1
    elif q2 == "d":
        scores[3] += 1

    # Question 3
    print("\n3. What’s your favorite summer fruit?")
    print("a) Strawberry")
    print("b) Mango")
    print("c) Cherry")
    print("d) Banana")
    q3 = get_valid_input("Your choice (a/b/c/d): ").lower()
    if q3 == "a":
        scores[0] += 1
    elif q3 == "b":
        scores[1] += 1
    elif q3 == "c":
        scores[2] += 1
    elif q3 == "d":
        scores[3] += 1

    # Question 4
    print("\n4. What’s your ideal summer drink?")
    print("a) Lemonade")
    print("b) Smoothie")
    print("c) Iced Coffee")
    print("d) Milkshake")
    q4 = get_valid_input("Your choice (a/b/c/d): ").lower()
    if q4 == "a":
        scores[0] += 1
    elif q4 == "b":
        scores[1] += 1
    elif q4 == "c":
        scores[2] += 1
    elif q4 == "d":
        scores[3] += 1

    # Question 5
    print("\n5. Pick a vacation destination:")
    print("a) Beach")
    print("b) Tropical Island")
    print("c) Mountain Cabin")
    print("d) Amusement Park")
    q5 = get_valid_input("Your choice (a/b/c/d): ").lower()
    if q5 == "a":
        scores[0] += 1
    elif q5 == "b":
        scores[1] += 1
    elif q5 == "c":
        scores[2] += 1
    elif q5 == "d":
        scores[3] += 1

    # Question 6
    print("\n6. What’s your preferred summer outfit?")
    print("a) Swimsuit")
    print("b) Flowy Dress/Top")
    print("c) Hoodie")
    print("d) T-shirt and shorts")
    q6 = get_valid_input("Your choice (a/b/c/d): ").lower()
    if q6 == "a":
        scores[0] += 1
    elif q6 == "b":
        scores[1] += 1
    elif q6 == "c":
        scores[2] += 1
    elif q6 == "d":
        scores[3] += 1

    # Question 7
    print("\n7. What’s your summer hobby?")
    print("a) Hiking or playing sports")
    print("b) Photography or art")
    print("c) Binge-watching movies/shows")
    print("d) Baking or gardening")
    q7 = get_valid_input("Your choice (a/b/c/d): ").lower()
    if q7 == "a":
        scores[0] += 1
    elif q7 == "b":
        scores[1] += 1
    elif q7 == "c":
        scores[2] += 1
    elif q7 == "d":
        scores[3] += 1

def find_top_flavor():
    highest = 0
    index = 0
    for i in range(len(scores)):
        if scores[i] > highest:
            highest = scores[i]
            index = i
    return flavors[index]

ask_questions()
result = find_top_flavor()
print("\nBased on your answers, your summer ice cream flavor is:", result + "! 🍨")

