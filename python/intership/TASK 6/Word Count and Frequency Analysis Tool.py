from collections import Counter

def analyze_text_file(filename):
    try:
        
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        
        line_count = len(lines)
        word_count = 0
        char_count = 0
        words = []

        for line in lines:
            char_count += len(line)
            line_words = line.split()
            word_count += len(line_words)
            words.extend(line_words)

        
        cleaned_words = [word.strip('.,!?;:"()[]').lower() for word in words if word.isalpha() or word.isalnum()]

        
        word_freq = Counter(cleaned_words)

        
        print(" === Text File Analysis === ")
        print(f"Total Lines     : {line_count}")
        print(f"Total Words     : {word_count}")
        print(f"Total Characters: {char_count}\n")

        print(" Most Common Words:")
        for word, freq in word_freq.most_common(10):  
            print(f"{word:<15} → {freq} times")

    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("=== Word Count & Frequency Tool ===")
    file_name = input("Enter the name of the text file (e.g., sample.txt): ")
    analyze_text_file(file_name)
