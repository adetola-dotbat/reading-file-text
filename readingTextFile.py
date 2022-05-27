# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#function to read the required file
def read_file_content(filename):
    # [assignment] Add your code here 

    with open(filename, 'r') as storyfile:
        filename = storyfile.read()
        
    return filename

#function to count the occurence of word in the file
def count_words():
    # [assignment] Add your code here
    text = read_file_content("./story.txt")
    counts = dict()
    text = text.lower()
    text = text.split()
    
    for x in text:
        if x in counts:
            counts[x] +=1
        else:
            counts[x]=1
    return counts
    

print(count_words())
