# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    with open("./story.txt", "r") as openfile:
        story_file = openfile.read() 
    return story_file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    count = {} #empty dictionary
    for i in split_text:
        if i in count:
            count[i] += 1
        else: 
            count[i] =1
    return count

print(count_words())