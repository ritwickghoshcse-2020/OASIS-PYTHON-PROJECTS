
def greetings():
  print("Hi there! How can I help you today?")

def respond_to_question(question):
  if question.lower() == "what time is it?":
    from datetime import datetime
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"It's {current_time}.")
  elif question.lower() == "what's the date today?":
    from datetime import date
    today = date.today()
    print(f"Today's date is {today.strftime('%Y-%m-%d')}.")
  else:
    print(f"Let me know what you need about {question}.")
    # Simulate web search
    print(f"Searching the web for '{question}'...")
    print("Here's some simulated search result...")

def main():
  greetings()
  while True:
    user_input = input("> ")
    if user_input.lower() == "hello":
      greetings()
    else:
      respond_to_question(user_input)

if __name__ == "__main__":
  main()
