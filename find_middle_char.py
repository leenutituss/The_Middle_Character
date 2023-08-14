def find_middle_characters(word):
    length_of_word = len(word)
    
    if length_of_word % 2 == 1:  
        middle_index = length_of_word // 2
        middle_character = word[middle_index]
    else:  
        middle_index = length_of_word // 2
        middle_character = word[middle_index - 1:middle_index + 1]
    
    return middle_character
even_length_word= "python"
result_even =find_middle_characters(even_length_word)
print(result_even) 

odd_length_word = "cat"
result_odd =find_middle_characters(odd_length_word)
print(result_odd) 
