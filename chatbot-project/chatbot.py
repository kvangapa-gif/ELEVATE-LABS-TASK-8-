# ---------------------------------------------
# Chatbot Project - Rule Based Using If-Else
# Built by Kundan Vangapandu
# ---------------------------------------------

def greet():
    print("Chatbot: Hello! How can I help you?")


def tell_joke():
    print("Chatbot: Why did the computer catch a cold? Because it had too many windows open! 😂")


def motivate():
    print("Chatbot: Keep going! Small progress each day leads to big success. 🚀")


def menu():
    print("\n--- MENU ---")
    print("1. Greet")
    print("2. Tell a Joke")
    print("3. Motivation")
    print("4. Chat Freely")
    print("5. Exit")


def free_chat(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        greet()
    elif "joke" in msg:
        tell_joke()
    elif "motivate" in msg or "motivation" in msg:
        motivate()
    elif "how are you" in msg:
        print("Chatbot: I'm doing great! Thanks for asking 😄")
    else:
        print("Chatbot: Sorry, I didn't understand that.")


# -------- MAIN PROGRAM --------

print("🤖 Chatbot Project Started!")
print("Choose options from the menu.\n")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        greet()

    elif choice == "2":
        tell_joke()

    elif choice == "3":
        motivate()

    elif choice == "4":
        user_msg = input("You: ")
        free_chat(user_msg)

    elif choice == "5":
        print("Chatbot: Goodbye! 👋")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
