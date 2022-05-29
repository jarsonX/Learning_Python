# Topic: classes and objects
# Source: online course
# Comments and notes: my own
# Code: my own but amended and optimised based on the official solution
#
# Description:
    # (1) Constructor (__init__) should take the argument text, make it lower 
    # case, and remove all punctuation. 
    # (2) freqAll method should create and return dictionary of all unique words 
    # in the text, along with the number of times they occur in the text. 
    # Each key in the dictionary should be the unique word appearing in the 
    # text and the associated value should be the number of times it occurs in 
    # the text. Create this dictionary from the fmtText attribute.
    # (3) freqOf method should take a word as an argument and return the 
    # number of occurrences of that word in fmtText. 

class edited(object):
    
# (1) Constructor
    def __init__(self, text):
        
        # Defining the attribute
        formatted = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formatted = text.lower()
        
        # Assigning the attribute to a value
        self.formatted_text = formatted

# (2) Method to create a dictionary
    def dictionary(self):
        
        # Split the text (keys)
        list_of_words = self.formatted_text.split()
        
        # Count the words (values)
        dictionary = {}
        for word in set(list_of_words):
            dictionary[word] = list_of_words.count(word)
        
        return dictionary
    
# (3) Method to return the number of occurrences of a word
    def count_words(self, word):
        dictionary = self.dictionary()
        
        if word in dictionary:
            return dictionary[word]
        return 0            
         

sample = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

sample = edited((sample))

print(sample.dictionary())
print(sample.count_words("et"))

