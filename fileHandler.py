# FILE HANDLER
import os


class FileHandler:
    def __init__(self, filename):
        self._filename = filename
        self._content = None
        
    def get_filename(self):
        return self._filename
    
    def set_filename(self, newfile):
        """Change the file and reload its content."""
        if not os.path.exists(newfile):
            raise FileNotFoundError(f"Error: '{self.get_filename()}' not found.")
        
        self._filename = newfile
        self.load_file()

    def load_file(self):
        """Loads the file content into memory and returns it"""
        if not os.path.exists(self.get_filename()):
            raise FileNotFoundError(f"Error: '{self.get_filename()}' not found.")

        with open(self.get_filename(), "r", encoding="utf-8") as file:
            self._content = file.read()
        
        return self._content
        
    def get_content(self):
        return self._content

