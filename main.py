# START MENU
import os
from fileHandler import FileHandler
from regexProcessor import RegexProcessor

# Main class
class FindThon:
    def __init__(self):
        self.file_handler = None
        self.regex_processor = None

    # Clear terminal function
    @staticmethod
    def clear_terminal():

        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix/Linux/Mac
            os.system('clear')

    # Start menu
    def start(self):
        while True:

            print("\n")
            print(
                """
-------------------------[ WELCOME TO ]--------------------------

███████╗██╗███╗   ██╗██████╗ ████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔════╝██║████╗  ██║██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
█████╗  ██║██╔██╗ ██║██║  ██║   ██║   ███████║██║   ██║██╔██╗ ██║
██╔══╝  ██║██║╚██╗██║██║  ██║   ██║   ██╔══██║██║   ██║██║╚██╗██║
██║     ██║██║ ╚████║██████╔╝   ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

--------[ PYTHON CONSOLE-BASED TEXT FINDER USING REGEX ]---------                               
                                                    """)
            
            # Processing of the text file
            filename = input("\nEnter the name of the file ('x' to exit): ")
            if filename.lower() == 'x':
                print("Console terminated.")
                exit()
            try:
                if not filename.endswith(".txt"):  
                    filename += ".txt"
                self.file_handler = FileHandler(filename)
                self.file_handler.load_file()
                self.regex_processor = RegexProcessor(self.file_handler.get_filename())
                
                self.clear_terminal()
                self.main_menu()
            except FileNotFoundError as e:
                print(e)
                input("Press Enter to try again...")
                self.clear_terminal()

    def main_menu(self):
        while True:
            print("\n")
            print(
                """
---------------[ WELCOME TO ]---------------
▗▖  ▗▖ ▗▄▖ ▗▄▄▄▖▗▖  ▗▖▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖
▐▛▚▞▜▌▐▌ ▐▌  █  ▐▛▚▖▐▌▐▛▚▞▜▌▐▌   ▐▛▚▖▐▌▐▌ ▐▌
▐▌  ▐▌▐▛▀▜▌  █  ▐▌ ▝▜▌▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌▐▌ ▐▌
▐▌  ▐▌▐▌ ▐▌▗▄█▄▖▐▌  ▐▌▐▌  ▐▌▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘

-------[ PRESS THE FUNCTION TO USE ]--------                               
                                                    """)
            
            print("""
[ 0 ] Extensive Searching
[ 1 ] View the Entire File Content
[ 2 ] Search for a Word or Sentence
[ 3 ] Find All Matches
[ 4 ] Count Matches
[ 5 ] Compute Total Sum of Numbers
[ 6 ] Find Minimum and Maximum Values
[ 7 ] Calculate Average
[ 8 ] Choose Another File
[ 9 ] Exit

Type 'help' for details.
""")
            choice = input("Enter the number of your choice: ").rstrip()


            if choice == "0":
                while True:
                    data_type = input("Would you like to search for: \n[ A ] Strings\n[ B ] Numbers\nEnter your choice: ").strip().upper()
                    if data_type in ["A", "B"]:
                        break
                    print("Invalid input. Please enter 'A' for Strings or 'B' for Numbers.")

                # Dictionary for easy access of the conditions
                if data_type == "A":
                    conditions = {
                        "A": ("Exact Match", r"\b{}\b"),
                        "B": ("Case-Insensitive Match", r"(?i){}"),
                        "C": ("Whole Word Match", r"\b{}\b"),
                        "D": ("Words Starting with a Specific Letter", r"\b{}[a-zA-Z]*"),
                        "E": ("Words Ending with a Specific Letter", r"[a-zA-Z]*{}\b"),
                        "F": ("Words Containing a Specific Substring", r".*{}.*"),
                        "G": ("Alphanumeric Words Only", r"\b[a-zA-Z0-9]+\b"),
                        "H": ("Words with a Specific Length", r"\b\w{{{}}}\b"),
                        "I": ("Words with Special Characters", r"[^a-zA-Z0-9\s]"),
                        "J": ("Words with numbers", r"\b(?=\w*\d)(?=\w*[a-zA-Z])\w+\b")
                    }

                else:
                    conditions = {
                        "A": ("0-100", r"\b(?:[1-9]?[0-9]|100)\b"),
                        "B": ("Even only", r"\b(?:[02468])\b|\b(?:[1-9]*[02468])\b"),
                        "C": ("Odd only", r"\b(?:[13579])\b|\b(?:[1-9]*[13579])\b"),
                        "D": ("Decimals only", r"\b\d+\.\d+\b"),
                        "E": ("Percentages only", r"\b\d+%"),
                        "F": ("Numbers with leading zeros", r"\b0+\d+\b"),
                        "G": ("Positive numbers only", r"\b\d+\b"),
                        "H": ("Negative numbers only", r"-\d+"),
                        "I": ("Consecutive numbers", r"\b(?:123|234|345|456|567|678|789|987|876|765|654|543|432|321)\b"),
                        "J": ("Numbers containing a specific digit", r"\b[0-9]*{}[0-9]*\b")
                    }


                while True:
                    print("\n-- Choose a condition --")
                    for key, value in conditions.items():
                        print(f"[ {key} ] {value[0]}")

                    condition = input("\nEnter the letter of your choice: ").strip().upper()
                    if condition in conditions:
                        break
                    print("Invalid choice. Please enter a valid letter.")

                search_term = input(f"Enter the {'Word/Phrase' if data_type == "A" else 'number/pattern'} to match if applicable: ").strip()
                regex_pattern = conditions[condition[0]][1].format(search_term)
                print(f"Using regex_pattern: {regex_pattern}\nSearching..\n")
                print(self.regex_processor.extensive_searching(regex_pattern))
                input("\nPress enter to exit.")
                self.clear_terminal()




            elif choice == "9":
                print("Console terminated.")
                exit()
            elif choice == "8":
                self.file_handler = None
                self.regex_processor = None
                self.clear_terminal()
                return self.start()
            elif choice.lower() == "help":
                print(
"""
FindThon: Python Console-based Text Finder using Regex

        Jhon Lloyd Valencia
        1st Year Computer Science major in Software Engineering
                      
-----------
FindThon is a simple console-based tool to search, analyze, and process text files using regular expressions.

1. Enter the name of the text file:
   - If the file is not found, a notice will be displayed, and the user will be prompted to enter the name again.
   - If the file is found, the program will proceed to the MAIN MENU.
   - If the user types 'X', the program will exit immediately.

MAIN MENU
-------------
Note: Searches are case-sensitive unless specified otherwise.
You may put regular expressions pattern for more specific matches.

0. Extensive Searching:
   - Select whether to search for **Strings** or **Numbers**.
   - Choose a condition from the available options.
   - Enter the input to match based on the selected condition.
   - Displays the search results, including matched lines and occurrences.

STRING SEARCH CONDITIONS:
  A. Exact Match  
     - Matches the exact word or phrase.  
     - **Example:** Searching for `"apple"` will match `"apple"` but not `"Apple"` or `"apples"`.  
     - **Regex:** `r"\bapple\b"`  

  B. Case-Insensitive Match  
     - Matches word/phrase regardless of case.  
     - **Example:** Searching for `"hello"` will match `"Hello"`, `"HELLO"`, and `"hElLo"`.  
     - **Regex:** `r"(?i)hello"`  

  C. Whole Word Match  
     - Finds full words only.  
     - **Example:** Searching for `"cat"` will match `"cat"` but not `"cats"` or `"cattle"`.  
     - **Regex:** `r"\bcat\b"`  

  D. Words Starting with a Letter  
     - Matches words that start with a specific letter.  
     - **Example:** Searching for `"A"` will match `"Apple"`, `"Air"`, `"Awesome"` but not `"banana"`.  
     - **Regex:** `r"\b[Aa]\w*"`  

  E. Words Ending with a Letter  
     - Matches words ending with a specific letter.  
     - **Example:** Searching for `"d"` will match `"word"`, `"speed"`, `"closed"` but not `"open"`.  
     - **Regex:** `r"\w*[dD]\b"`  

  F. Words Containing a Substring  
     - Finds words that contain a specific substring.  
     - **Example:** Searching for `"sun"` will match `"sunlight"`, `"sunny"`, `"sunrise"`, but not `"moon"`.  
     - **Regex:** `r"\b\w*sun\w*\b"`  

  G. Alphanumeric Words Only  
     - Matches words that contain only letters and numbers (no special characters).  
     - **Example:** Matches `"abc123"`, `"hello2000"`, but not `"hello@world"`.  
     - **Regex:** `r"\b[a-zA-Z0-9]+\b"`  

  H. Words of Specific Length  
     - Matches words of a given length (e.g., 5 letters).  
     - **Example:** Searching for `5` will match `"apple"`, `"grape"`, `"table"` but not `"banana"`.  
     - **Regex:** `r"\b\w{5}\b"`  

  I. Words with Special Characters  
     - Matches words that contain special characters.  
     - **Example:** Matches `"hello!"`, `"@mention"`, `"#hashtag"`, but not `"hello"`.  
     - **Regex:** `r"\b\w*[^a-zA-Z0-9\s]\w*\b"`  

  J. Words with Numbers  
	 - Matches words that contain at least one number.
	 - **Example:** Matches "h3llo", "password123", "4ever", but not "hello".
	 - **Regex:** r"\b\w*\d\w*\b"


NUMBER SEARCH CONDITIONS:
  A. 0-100  
     - Matches numbers from 0 to 100.  
     - **Example:** Matches `"0"`, `"25"`, `"100"`, but not `"101"` or `"150"`.  
     - **Regex:** `r"\b(?:[1-9]?[0-9]|100)\b"`  

  B. Even only  
     - Matches even numbers.  
     - **Example:** Matches `"2"`, `"14"`, `"100"`, but not `"3"` or `"57"`.  
     - **Regex:** `r"\b\d*[02468]\b"`  

  C. Odd only  
     - Matches odd numbers.  
     - **Example:** Matches `"1"`, `"33"`, `"99"`, but not `"4"` or `"80"`.  
     - **Regex:** `r"\b\d*[13579]\b"`  

  D. Decimals only  
     - Matches floating-point numbers.  
     - **Example:** Matches `"3.14"`, `"0.5"`, `"100.99"`, but not `"2"` or `"50"`.  
     - **Regex:** `r"\b\d+\.\d+\b"`  

  E. Percentages only  
     - Matches numbers ending with `%`.  
     - **Example:** Matches `"5%"`, `"100%"`, `"42.5%"`, but not `"50"` or `"3.5"`.  
     - **Regex:** `r"\b\d+%""`  

  F. Numbers with Leading Zeros
     - Finds numbers that start with one or more zeros.
     - **Example**: Matches "007", "000123", "0456", but not "1234".
     - **Regex**: r"\b0+\d+\b"

  G. Positive numbers only  
     - Matches numbers greater than zero.  
     - **Example:** Matches `"1"`, `"99"`, `"500"`, but not `"0"` or `"-10"`.  
     - **Regex:** `r"\b[1-9]\d*\b"`  

  H. Negative numbers only  
     - Matches numbers less than zero.  
     - **Example:** Matches `"-1"`, `"-100"`, `"-500"`, but not `"10"` or `"0"`.  
     - **Regex:** `r"-\b\d+\b"`  

  I. Consecutive Increasing or Decreasing Numbers
     - Matches numbers that are sequentially increasing or decreasing.
     - **Example**: Matches "123", "4567", "987", but not "145".
     - **Regex**: r"\b(?:123|234|345|456|567|678|789|987|876|765|654|543|432|321)\b""

  J. Numbers containing a specific digit  
     - Matches numbers that contain a particular digit.  
     - **Example:** If searching for numbers containing `"5"`, it will match `"5"`, `"15"`, `"50"`, `"500"`, but not `"42"`.  
     - **Regex:** `r"\b\d*[5]\d*\b"`  # (Digit `5` can be replaced dynamically)  

1. View the Entire File Content:
   - Displays the full text content of the loaded file.

2. Search for a Word or Sentence:
   - Displays the first occurrence found.
   - Prints the entire line where the match was found.
   - If none, prints “No occurrence found.”

3. Find all Matches:
   - Displays all occurrences found in the text file.
   - Prints the entire line for each match.
   - If none, prints “No occurrence found.”

4. Count Matches:
   - Displays the total count of occurrences in the file.

5. Compute Totals from Matches (Numerical Data):
   - Extracts all numbers from the file.
   - Computes and displays the sum of all numbers found.

6. Find Minimum or Maximum Values (Numerical Data):
   - Extracts all numbers from the file.
   - Finds and displays the Minimum and Maximum numbers.

7. Calculate Average (Numerical Data):
   - Extracts all numbers from the file.
   - Computes and displays the average value.

8. Choose Another File:
   - Returns to the start-up screen to enter a new file.

9. Exit:
   - Terminates the program.
""")
                input("\nPress enter to exit.")
                self.clear_terminal()
            else:
                self.process_choice(choice)

    def process_choice(self, choice):
        if not self.regex_processor:
            print("No file loaded.")
            return
        
        if choice == "1":
            print("\n--- File Content ---\n")
            print(self.file_handler.get_content())
            input("\nPress enter to exit.")
            self.clear_terminal()


        elif choice == "2":
            pattern = input("Enter a word or sentence to search (You may write in Regex Form for specific searches): ")
            print(self.regex_processor.search_word_sentence(pattern))
            input("\nPress enter to exit.")
            self.clear_terminal()


        elif choice == "3":
            pattern = input("Enter a search pattern (You may write in Regex Form for specific searches): ").strip()
            print(self.regex_processor.find_all_matches(pattern))
            input("\nPress enter to exit.")
            self.clear_terminal()

        elif choice == "4":
            pattern = input("Enter a pattern to count: ").strip()
            print(f"Total occurrences: {self.regex_processor.count_matches(pattern)}")
            input("\nPress enter to exit.")
            self.clear_terminal()

        elif choice == "5":
            print(f"Total sum: {self.regex_processor.compute_totals_matches()}")
            input("\nPress enter to exit.")
            self.clear_terminal()

        elif choice == "6":
            min_val, max_val = self.regex_processor.find_min_max()
            print(f"Minimum Value: {min_val}\nMaximum Value: {max_val}")
            input("\nPress enter to exit.")
            self.clear_terminal()

        elif choice == "7":
            print(f"Average: {self.regex_processor.calculate_average()}")
            input("\nPress enter to exit.")
            self.clear_terminal()

        else:
            print("Invalid choice. Please try again.")
            self.clear_terminal()

def main():
    app = FindThon()
    app.start()

main()