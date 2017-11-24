import pandas as pd
import nltk
import string


df = pd.read_csv("mypersonality_final.csv", encoding = "ISO-8859-1")

print(df.describe())
print(df.head())

### configurations

chosen_punctuation = ['.', ',', ';', ':', '!', '?', '"', "'"]
special_chars = set(string.punctuation) - set(chosen_punctuation)


### meta information

# time stamp
# language
# location
# number of urls in a message
# number of friends
# number of shares
# number of likes


### lexical

### char-based
# number of chars
# number of ascii chars
# number of ascii uppercase chars
# number of ascii lowercase chars
# number of digits
# number of whitespaces
# number of tabs
# number of special chars
# freq of special chars
# freq of letters

### word-based
# number of words
# number of short words
# number of unique words
# number of sentences
# short words / total ratio
# avg word length
# avg sentence length (chars)
# avg sentence length (words)
# avg line length
# word length distribution per word length
# word usage ratio (per 100 words) -> Hapax legomena (freq of once occuring words)


# vocabulary richness measures? -> Zheng / Tweedie and Baayen


### syntactic

# character freq of punctuation
# freq of function words -> which ones?


# part of speech (POS) -> might be immature
# occurence of prepositions


### structural

# number of lines
# number of blank lines
# has a greeting
# has a farewell


# paragraph length
# number of sentences per paragraph
# number of words per paragraph
# separators per paragraph
# quoted content -> special chars?
# indentation
# use of greeting statement


### content-specific

# freq of keywords
# emoticons
# abbreviations
# number of hashtags


# message similiarity score


### n-grams

# word n-grams
# character n-grams



def get_char_based_lexical_features():
	# number of chars
	df['total_chars'] = df['STATUS'].apply(len)


	# number of ascii chars
	df['total_alpha_chars'] = df['STATUS'].apply(lambda s: sum(1 for c in s if c.isalnum()))


	# number of ascii uppercase chars
	df['total_upper_chars'] = df['STATUS'].apply(lambda s: sum(1 for c in s if c.isupper()))


	# number of ascii lowercase chars
	df['total_lower_chars'] = df['STATUS'].apply(lambda s: sum(1 for c in s if c.islower()))


	# number of digits
	df['total_digits'] = df['STATUS'].apply(lambda s: sum(1 for c in s if c.isdigit()))


	# number of whitespaces
	df['total_whitespaces'] = df['STATUS'].apply(lambda s: sum(1 for c in s if c.isspace()))


	# number of tabs
	df['total_tabs'] = df['STATUS'].apply(lambda s: sum(1 for c in s if c=='\t'))


	# number of special chars
	df['total_whitespaces'] = df['STATUS'].apply(lambda s: sum(1 for c in s if c.isspace()))


	# freq of letters
	# freq of special chars

	print(df.head())

get_char_based_lexical_features()