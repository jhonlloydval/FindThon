import re
from fileHandler import FileHandler

class RegexProcessor(FileHandler):
    def __init__(self, filename):
        super().__init__(filename)
        content = self.load_file()
        self._content = content.split('\n') if content else []
        
    def search_word_sentence(self, pattern):
        for i, line in enumerate(self._content, 1):
            if re.search(f"{pattern}", line):
                return f"First occurrence found in Line {i}:\n{line}"
        return "No occurrence found."
    

    def find_all_matches(self, pattern):
        matches = []

        for line_no, line in enumerate(self._content, 1):
            line = line.rstrip()
            if re.search(f"{pattern}", line):
                matches.append(f"Line {line_no}: {line}")

        return "\n".join(matches) if matches else "No occurrence found."


    def count_matches(self, pattern):
        count_list = []
        for line in self._content:
            line = line.rstrip()
            count = re.findall(f"{pattern}", line)

            for x in count:
                count_list.append(x)

        return len(count_list)
    
    def compute_totals_matches(self, pattern = None):
        num_list = []
        for line in self._content:
            line = line.rstrip()
            numbers = re.findall(r'-?\b\d+\b', line)
            for x in numbers:
                num_list.append(int(x))

        return sum(num_list)
    
    def find_min_max(self):
        num_list = []
        for line in self._content:
            line = line.rstrip()
            numbers = re.findall(r'-?\b\d+\b', line)
            num_list.extend(int(x) for x in numbers)
        if not num_list:
            return [0, 0] 
        return [min(num_list), max(num_list)]
    

    def calculate_average(self):
        num_list = []
        regex_pattern = input("Enter a pattern (press enter if none): ").strip()

        for line in self._content:
            line = line.rstrip()
            
            try:
                if regex_pattern:
                    numbers = re.findall(regex_pattern, line)
                else:
                    numbers = re.findall(r"\d+", line)
            except re.error:
                print("Invalid regex pattern. Please try again.")
                return 0

            num_list.extend(int(x) for x in numbers if x.isdigit())

        if not num_list:
            print("No numerical data found. Returning 0.")
            return 0  

        return sum(num_list) / len(num_list)
    
    def extensive_searching(self, regex_pattern):

        matches = []
        
        for line_no, line in enumerate(self._content, 1):
            line = line.rstrip()
            if re.search(f"{regex_pattern}", line):
                matches.append(f"Line {line_no}: {line}")

        return "\n".join(matches) if matches else "No occurrence found."