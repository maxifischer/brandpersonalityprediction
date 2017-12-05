"""
# structural

- number of lines
    --> no newlines in data
- number of blank lines
    --> no newlines in data
- has a greeting
    --> very rare usages of 'hey' or 'dear', most of them not met as a general greeting
- has a farewell
    --> very few usages at the end
- indentation
    --> was very likely removed

- paragraph length
    --> no newlines again

if we assume one post as one paragraph the following features are already covered by word-based features
- number of sentences per paragraph
- number of words per paragraph


- separators per paragraph -> separators?
- quoted content
    --> quotation marks: ", ', `, >, <, _
- use of greeting statement
"""
import pandas as pd
import re

# configuration
quoteChars = ['"', "'", '`', '*', '_']
# build quoted content regexes
quotedMatchers = []
for quoteChar in quoteChars:
    if quoteChar == "'":
        matcher = r'([^\w]|^)\'\w[^\']*?\w\'([^\w]|$)'

    elif quoteChar == "*":
        matcher = r'([^\w]|^)\*(?!PROPNAME)[^*]+?\*([^\w]|$)'

    else:
        matcher = r'' + re.escape(quoteChar) + '[^' + quoteChar + ']+?' + re.escape(quoteChar)

    quotedMatchers.append(matcher)
    print(matcher)


def append_structural_features(df, column):
    # quoted content
    df['quoted_content'] = df[column].apply(lambda s: sum(1 for matcher in quotedMatchers for match in re.findall(matcher, s)))


if __name__ == "__main__":
    df = pd.read_csv("mypersonality_final.csv", encoding="ISO-8859-1")
    append_structural_features(df, 'STATUS')
    df = df[(df['quoted_content'] > 0)][['STATUS', 'quoted_content']]
    print(df)
    df.to_csv("new.csv", encoding="UTF-8")