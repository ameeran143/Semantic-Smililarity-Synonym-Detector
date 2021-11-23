import math


# Part 1

# subpart a
def cosine_similarity(vec1, vec2):
    sum_a = 0
    sum_b = 0
    total_dot_product = 0

    for item in vec1.items():
        sum_a += item[1] ** 2
        if item[0] in vec2.keys():
            total_dot_product += item[1] * vec2.get(item[0])
            print(total_dot_product)

    # calculating the sum of vec 2 squares
    for item in vec2.values():
        sum_b += item ** 2

    return float(total_dot_product / (math.sqrt(sum_a * sum_b)))


def build_semantic_descriptors(sentences):
    semantic_descriptor = {}

    # doing this sentence bty sentence, loop through each sentence, checks if each word is in the dictionary already,
    # if yes, it then adds +1 to all the count of the other words into the respective dictionary
    for n in range(len(sentences)):
        for word in sentences[n]:

            if word not in semantic_descriptor:
                semantic_descriptor[word] = {}

            for words in sentences[n]:
                if words != word:
                    if words in semantic_descriptor[word]:
                        semantic_descriptor[word][words] += 1
                    else:
                        semantic_descriptor[word][words] = 1

    return semantic_descriptor







a = {"a": 1, "b": 2, "c": 3}
b = {"b": 4, "c": 5, "d": 6}

if "a" in a:
    print("yes")

# a["e"] = "yes"
# print(a)


# print(cosine_similarity(a, b))
print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
 ["i", "am", "a", "spiteful", "man"],
 ["i", "am", "an", "unattractive", "man"],
 ["i", "believe", "my", "liver", "is", "diseased"],
 ["however", "i", "know", "nothing", "at", "all", "about", "my",
 "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))
