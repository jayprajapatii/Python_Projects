'''A program that reads a text file and analyzes
 its content, providing word count, line count,
 and character count'''

def text_file_analyzer(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        print(f"Lines: {len(lines)}, Words: {len(words)}, Characters: {len(content)}")

text_file_analyzer('D:/python/Practical List July Dec 2025/sample.txt')