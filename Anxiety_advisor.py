# Setting up a function that returns advice depending upon the user's anxiety level
def anxiety_advice(level):
    if level <= 3:
        return "Your anxiety seems mild. Try taking 3 deep and slow breaths."
    elif level <= 7:
        return (
            "Your anxiety is moderate. Let's try the 5-4-3-2-1 grounding method:\n"
            "  > Name 5 things you can SEE\n"
            "  > Name 4 things you can FEEL\n"
            "  > Name 3 things you can HEAR\n"
            "  > Name 2 things you can SMELL\n"
            "  > Name 1 thing you can TASTE"
        )
    elif level <= 10:
        return "Your anxiety is very high. Focus entirely on a slow 4 count exhale."
    else:
        return "Please enter a valid number between 1 and 10."

# Execution of the main program
while True:
    # The program first tries to run this block
    try:
        anxiety_level = int(input("How anxious do you feel today on a scale of (1-10): "))

        # User will be asked to enter the number in range and program will not proceed until they do
        if anxiety_level < 1 or anxiety_level > 10:
            print("That number is not between 1 and 10. Please try again.\n")
            continue  # Skips the rest of the loop and restarts it

        # The function is called and the result is stored
        advice = anxiety_advice(anxiety_level)
        print(advice)
        break
    except ValueError:
        # If a letter is entered the following message will be displayed instead of the program crashing
        print("Invalid input. Please enter a whole number between 1 and 10.\n")