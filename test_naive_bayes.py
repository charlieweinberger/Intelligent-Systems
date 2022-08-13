import sys
from naive_bayes import *

data = {
    "scam": ["no", "yes", "yes", "no", "no", "yes", "no", "no", "yes", "no"],
    "errors": ["no", "yes", "yes", "no", "no", "yes", "yes", "no", "yes", "no"],
    "links": ["no", "yes", "yes", "no", "yes", "yes", "no", "yes", "no", "yes"]
}

nb = NaiveBayes(data)

test_data = {
    "errors": ["no", "yes", "yes", "no"],
    "links": ["no", "yes", "no", "yes"]
}

print(nb.predict(test_data))