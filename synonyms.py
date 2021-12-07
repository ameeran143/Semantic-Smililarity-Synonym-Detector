import math
import re
# import txt as txt

# Part 1

# subpart a

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    sum_a = 0
    sum_b = 0
    total_dot_product = 0
    shared_keys = []

    for item in vec1.items():
        sum_a += item[1] ** 2
        if item[0] in vec2.keys():
            shared_keys.append(item[0])

    # calculating the sum of vec 2 squares
    for item in vec2.values():
        sum_b += item ** 2

    for i in shared_keys:
        total_dot_product += vec1.get(i) * vec2.get(i)

    return float(total_dot_product / (math.sqrt(sum_a * sum_b)))


def build_semantic_descriptors(sentences):
    semantic_descriptor = {}

    # doing this sentence bty sentence, loop through each sentence, checks if each word is in the dictionary already,
    # if yes, it then adds +1 to all the count of the other words into the respective dictionary
    for x in sentences:
        no_duplicates = []

        # removing all the duplicates from the sentences so that semantic descriptors is not double counted.
        for word in x:
            if word not in no_duplicates:
                no_duplicates.append(word)

        # doing this sentence bty sentence, loop through each sentence, checks if each word is in the dictionary already,
        # if yes, it then adds +1 to all the count of the other words into the respective dictionary
        for word in no_duplicates:
            word = word.lower()
            refined_word = word

            if refined_word in semantic_descriptor:
                for x in no_duplicates:
                    x = x.lower()
                    if x != refined_word:
                        if x in semantic_descriptor[refined_word]:
                            semantic_descriptor[refined_word][x] += 1
                        else:
                            semantic_descriptor[refined_word][x] = 1

            else:
                temp_dic = {}
                for x in no_duplicates:
                    x = x.lower()
                    if x != refined_word:
                        if x in temp_dic:
                            temp_dic[x] += 1
                        else:
                            temp_dic[x] = 1
                        semantic_descriptor[refined_word] = temp_dic

        return semantic_descriptor

        # for a in no_duplicates:
        #     for b in no_duplicates:
        #         if a not in semantic_descriptor.keys():
        #             semantic_descriptor[a] = {}
        #         if a != b:
        #             if b in semantic_descriptor[a].keys():
        #                 semantic_descriptor[a][b] += 1
        #             else:
        #                 semantic_descriptor[a][b] = 1

    return semantic_descriptor


def build_semantic_descriptors_from_files(filenames):
    # [",", "-", "--", ":", ";"]

    total_text = []
    punctuation = [",", "-", "--", ":", ";", '"']
    separations = ["!", "?"]

    for i in range(len(filenames)):
        f = open(filenames[i], "r", encoding="utf-8").read()
        f = f.lower()
        list1 = []

        for x in punctuation:
            f = f.replace(x, " ")
        for y in separations:
            f = f.replace(y, ".")

        f = f.replace("\ufeff", " ")

        f_split = f.split(".")

        for x in f_split:
            list1.append(x.split())
        total_text += list1

    return build_semantic_descriptors(total_text)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    # word - (string), choices - list of strings, similarity_fn - function
    # compute semantic similairty using the cosine_similarity function
    # check if the word is in the semantic_descriptor or else return -1

    word1_vec = semantic_descriptors.get(word.lower())
    similarity = 0
    choice = choices[0]
    temp = 0

    if word not in semantic_descriptors.keys():
        return choice

    for i in range(len(choices)):

        if choices[i].lower() not in semantic_descriptors:
            temp = -1
        else:
            word2_vec = semantic_descriptors.get(choices[i].lower())
            temp = similarity_fn(word1_vec, word2_vec)

        if i == 0:
            similarity = temp

        if temp > similarity:
            similarity = temp
            choice = choices[i]

    return choice


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    # takes in a file name that contains the testing in the format: word answer option1 op2 op3 (all lower case.)
    f = open(filename, "r", encoding="utf-8").read()
    split = f.split("\n")
    del split[-1]
    question_list = []

    for i in range(len(split)):
        question_list.append(split[i].split())

    max_similarity = 0
    calculated_answer = ""
    correct = 0
    total = len(question_list)
    options = []

    for i in range(len(question_list)):
        options = []

        word = question_list[i][0]
        real_answer = question_list[i][1]
        for x in range(len(question_list[i])):
            if x >= 2:
                options.append(question_list[i][x])

        if most_similar_word(word, options, semantic_descriptors, similarity_fn).lower() == real_answer:
            correct += 1

    return float((correct / total) * 100)

# sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt", "frankenstein.txt", "sholmes.txt", "oz.txt", "huckleberry.txt", "percy_jackson.txt"])
# res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
# print(res, "% of the guesses were correct")
