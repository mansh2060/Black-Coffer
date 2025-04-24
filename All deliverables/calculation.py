"""
Here from filtered txt file i have imported the datas and calculate the variables value asked and saved the data in
output structure .csv
"""



import pandas as pd
import re
from stopwordslist import positive_words_list, negative_words_list

df=pd.read_excel('input.xlsx')

def count_syllables(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

def calculate_metrics(text):
    """
    Perform linguistic calculations on the cleaned text.
    """
    sentences = text.split('.')
    num_sentences = len(sentences)
    words = text.split()
    num_words = len(words)
    
    # Count positive and negative words
    positive_count = sum(1 for word in words if word.lower() in positive_words_list())
    negative_count = sum(-1 for word in words if word.lower() in negative_words_list())
    
    # Polarity Score
    polarity_score = (positive_count - -1*negative_count) / (positive_count + -1*negative_count + 1e-5)
    
    # Subjectivity Score
    subjectivity_score = (positive_count + -1*negative_count) / (num_words + 1e-5)
    
    # Avg Sentence Length
    avg_sentence_length = num_words / num_sentences if num_sentences > 0 else 0
    
    # Complex Word Count and Percentage
    complex_word_count = sum(1 for word in words if count_syllables(word) > 2)
    percentage_complex_words = (complex_word_count / num_words) * 100 if num_words > 0 else 0
    
    # Fog Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    # Syllables Per Word
    total_syllables = sum(count_syllables(word) for word in words)
    syllables_per_word = total_syllables / num_words if num_words > 0 else 0
    
    # Personal Pronouns Count
    personal_pronouns = re.findall(r'\b(I|we|my|ours|us)\b', text, re.IGNORECASE)
    personal_pronoun_count = len(personal_pronouns)
    
    # Avg Word Length
    total_characters = sum(len(word) for word in words)
    avg_word_length = total_characters / num_words if num_words > 0 else 0
    
    return {

        'positive_score': positive_count,
        'negative_score': negative_count,
        'polarity_score': polarity_score,
        'subjectivity_score': subjectivity_score,
        'avg_sentence_length': avg_sentence_length,
        'percentage_complex_words': percentage_complex_words,
        'fog_index': fog_index,
        'complex_word_count': complex_word_count,
        'word_count': num_words,
        'syllables_per_word': syllables_per_word,
        'personal_pronouns': personal_pronoun_count,
        'avg_word_length': avg_word_length,
    }

# Path to the folder containing the filtered .txt files


# Initialize results
results = []


for url_id,url in zip(df['URL_ID'],df['URL']):
    # Construct the file name directly
    file_name = f"filtered_{url_id}.txt"
    
    try:
        # Read the filtered text file
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Perform calculations
        metrics = calculate_metrics(text)
        metrics['url_id'] = url_id 
        results.append(url_id)
        results.append(url)
        results.append(metrics)
    
    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping...")
    except Exception as e:
        print(f"Error processing file {file_name}: {e}")

        
        

# Convert results to DataFrame and save
results_df = pd.DataFrame(results)
results_df.to_csv('Output Structure.csv', index=False)

print("Analysis complete. Results saved to 'Output Data Structure.csv'.")
