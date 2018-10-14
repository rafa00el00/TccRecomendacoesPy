import fastText
import re

def strip_formatting(string):
    string = string.lower()
    string = re.sub(r"([.!?,'/()])", r" \1 ", string)
    return string

# Reviews to check
reviews = [
    "Esse restaurante literalmente mudou minha vida. Esse é o melhor lugar para se comer!",
    "Eu odeio muito esse lugar. ",
    "I não sei.É bom, eu acho. Não tenho muita certeza"
]

# Pre-process the text of each review so it matches the training format
preprocessed_reviews = list(map(strip_formatting, reviews))

# Load the model
classifier = fastText.load_model('comentarios.txt')

# Get fastText to classify each review with the model
labels, probabilities = classifier.predict(preprocessed_reviews, 1)

# Print the results
for review, label, probability in zip(reviews, labels, probabilities):
    stars = int(label[0][-1])

    print("{} ({}% confidence)".format("☆" * stars, int(probability[0] * 100)))
    print(review)
    print()