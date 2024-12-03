import time
import random as r

def calculate_mistakes(paratest, usertest):

    errors = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                errors += 1
        except IndexError:
            errors += 1
    return errors

def calculate_speed(time_start, time_end, user_input):
    
    time_delay = time_end - time_start
    time_delay_rounded = round(time_delay, 2)
    speed = len(user_input) / time_delay_rounded
    return round(speed)

def typing_speed_test():
    
    test_sentences = [
        "Hello, I am a Python developer as well as an AI developer",
        "I want to become an AI developer",
        "How much time will be required to finish my work?",
        "Thank you for your support"
    ]
    test_sentence = r.choice(test_sentences)
    
    print("***** Typing Speed Test *****")
    print(test_sentence)
    print()
    
    time_start = time.time()
    user_input = input("Enter: ")
    time_end = time.time()
    
    speed = calculate_speed(time_start, time_end, user_input)
    mistakes = calculate_mistakes(test_sentence, user_input)
    
    print(f"Speed: {speed} w/sec")
    print(f"Errors: {mistakes}")

while True:
    choice = input("Ready to test? (yes/no): ")
    if choice.lower() == "yes":
        typing_speed_test()
    elif choice.lower() == "no":
        print("Thank you")
        break
    else:
        print("Invalid input")


