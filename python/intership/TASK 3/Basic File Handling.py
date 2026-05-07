def file_handling(filename, old_word, new_word):
  try:
      with open(filename, 'r')as file:
          data = file.read()
          
      modified_data = data.replace(old_word, new_word) 
      
      if data == modified_data:
          print(f"No occurrences of '{old_word}' found in the file.")   
      else:
          print(f"All occurrences of '{old_word}' replaced with '{new_word}'.")
          
      with open(filename, 'w')as file:
            file.write(modified_data)
            
      print("file updated successfully")
      
  except FileNotFoundError:
      print(f"Error: the file '{filename}' was not found.")
      
  except PermissionError:
      print(f"Error: Permission denied to read/write the file '{filename}'.")
      
  except Exception as e:
      print(f"an unexpected error occurred: {e}")



file_name = "p1.txt"
old_word = input("Enter the word to find: ")
new_word = input("Enter the word to replace it with: ")

file_handling(file_name, old_word, new_word)