def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        letter_count = get_letter_count(text)
        char_list = get_character_sorted_list(letter_count)
        
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        print()
        
        for item in char_list:
               if not item["char"].isalpha():
                      continue
               print(f"The {item["char"]} character was found {item["num"]} times")
        print(f"--- End report ---")

def get_book_text(path):
        with open(path) as f:
            file_contents = f.read()
            return file_contents
        
def get_num_words(text):
       words = text.split()
       return len(words)

def get_letter_count(text):
       chars = {}
       for char in text:
              lowered_text = char.lower()
              if lowered_text in chars:
                     chars[lowered_text]+=1
              else:
                     chars[lowered_text]=1
       return chars

def sort_on(dict):
       return dict["num"]

def get_character_sorted_list(letter):
       sorted_list = []
       for item in letter:
              sorted_list.append({"char":item,"num":letter[item]})
       sorted_list.sort(reverse = True,key=sort_on)
       return sorted_list       

main()    