def charCount(text):

    chars = {}

    for char in text:
        char = char.lower()

        if char in chars:
            chars[char] +=1
        else:
            chars[char] = 1

    return chars

def bookReport(book):
    with open(book) as f:
        file_contents = f.read()

    #print(file_contents)

    words = file_contents.split()
    
    print(f"--- Begin report of {book} ---")
    print(f"{len(words)} words found in the document\n")

    chars = charCount(file_contents)
    ascii = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for k,v in chars.items():
        if k in ascii:
            print(f"The '{k}' character was found {v} times")

    print("--- End report ---")
    
    #print(chars)




def main():
    location = "books/frankenstein.txt"
    bookReport(location)
    

main()