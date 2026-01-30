import nltk
from nltk.chat.util import reflections

# Download NLTK tokenizer models (only needed once)
nltk.download('punkt')

# Define patterns and responses
# Each pattern is matched with possible replies
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm an AI chatbot created using NLP!", "You can call me ChatNLP."]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?", "Feeling intelligent today!"]
    ],
    [
        r"(.*) your creator?",
        ["I was created by a Python programmer using NLTK."]
    ],
    [
        r"what is NLP ?",
        ["NLP stands for Natural Language Processing. It's a field of AI that deals with interaction between computers and humans using natural language."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help. Tell me your query.", "Of course, ask me anything!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Could you rephrase it?", "I'm still learning. Please ask something else."]
    ]
]

# Words that will end the chat
exit_words = ["bye", "exit", "quit"]

# Custom function to handle chatbot conversation
def start_chat():
    print("Hi! I'm an AI Chatbot. Type 'bye' to exit.")

    # Create chatbot with the defined patterns and reflections (handles 'I' to 'you' and vice versa)
    chat = nltk.chat.util.Chat(pairs, reflections)

    # Start an infinite loop to continue chatting
    while True:
        # Get user input and convert to lowercase for matching
        user_input = input("> ").lower()

        if user_input in exit_words:
            print("Goodbye!")
            break

        # Get a response based on the pattern matching
        response = chat.respond(user_input)
        print(response)

# Run the chatbot only when the script is executed directly
if __name__ == "__main__":
    start_chat()
