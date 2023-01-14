import spacy
nlp = spacy.load('en_core_web_md')

# --- Cat,(apple), monkey,banana similarity ---

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens: 
        print(token1.text, token2.text, token1.similarity(token2))

# as nlp has become very advanced more links between more categories are added 
# such as in this example where not only does the nlp model
# detect similarities between two animals but also that of an animal and a food its associated with


# --- Desk, candle, Sweden, brother  similarity ---

tokens = nlp('desk candle Sweden brother ')
for token1 in tokens:
    for token2 in tokens: 
        print(token1.text, token2.text, token1.similarity(token2))

# my aim was to find unrelated words which reflects in the results
# i was expectign desk and candle to have the highest similarity 
# the siilarity between brother and Sweden was unexpected


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I'd like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# en_core_web_sm seems to see less simialrity in all sentences 
# but more similarity betwwen the words desk, candle, Sweden, brother