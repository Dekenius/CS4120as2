import spacy
from datetime import datetime


# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def log(txt):
    print(datetime.utcnow(), txt)

def create_doc(filename):
    log("Started create doc")
    # load text
    file = open(filename, 'rt', encoding="UTF8") # rt = read text
    text = file.read()
    doc = nlp(text)
    log("Finished create doc")
    return doc

def get_num_sentences(doc):
    log("Started num_sentences.")

    # Print all sentences, line by line
    i = 0
    for sent in doc.sents:
        # print(sent.text)
        # print(i)
        i+=1

    file = open("Q1.txt", "a")
    file.write("The number of sentences in the dataset is " + str(i) + '\n')
    file.close()

    log("Finished.")
    return i

    # print(len(doc.sents))

def get_num_verbs(doc):
    log("Started num_verbs.")

    # total number of verbs
    i = 0

    for token in doc:
        if token.pos_ == 'VERB':
            i += 1

    file = open("Q1.txt", "a")
    file.write("The number of verbs in the dataset is " + str(i) + '\n')
    file.close()

    log("Finished num_verbs.")
    return i

def verbs_per_sentence(doc, num_sent):
    log("Starting verbs_per_sentence.")

    # num_sent = num_sentences(doc)
    num_verb = get_num_verbs(doc)
    avg = num_verb / num_sent

    file = open("Q1.txt", "a")
    file.write("The average number of verbs per sentence in the dataset is " + str(avg) + '\n')
    file.close()
    log("Finished verbs_per_sentence.")
    return avg

def get_prepositions(doc):
    '''
    returns the total number of prepositions,
    also finds 3 most common prepositions
    '''
    log("Started get_preps")
    prep_dict = dict() # prep -> it's count
    count = 0 # total number of prepositions

    for token in doc:
        if token.dep_ == "prep":
            if token.text in prep_dict:
               prep_dict[token.text] += 1
            else:
                prep_dict[token.text] = 1
            count += 1

    # get most common preposition, then remove it to get 2nd most common, and again
    first_most = max(prep_dict, key=prep_dict.get)
    print(prep_dict[first_most])
    prep_dict[first_most] = 0
    second_most = max(prep_dict, key=prep_dict.get)
    print(prep_dict[second_most])
    prep_dict[second_most] = 0
    third_most = max(prep_dict, key=prep_dict.get)
    print(prep_dict[third_most])

    file = open("Q1.txt", "a")
    file.write("The average number of prepositions in the dataset is " + str(count) + '\n')
    file.write("The three most common prepositions: " + first_most + ", " + second_most + ", " +  third_most + '\n')
    file.close()

    log("Finished get_preps.")
    return count, first_most, second_most, third_most

def number_of_entities(doc):
    log("Started number_of_entities")
    ents = []
    count = 0
    for entity in doc.ents:
        if entity.label_ not in ents:
            ents.append(entity.label_)
        count += 1


    file = open("Q1.txt", "a")
    file.write("Number of entities: " + str(count) + '\n')
    file.write("Unique entities: " + str(ents) + '\n')
    file.close()

    log("Finished.")

def analyze_doc(doc):
    # Analyze syntax
    # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
    print("xXxXxX")
    for token in doc:
        print(token.lemma_, token.pos_)

    # Find named entities, phrases and concepts
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)


def main():

    log("Started main")

    doc = create_doc("parsing_dataset.txt")
    # analyze_doc(doc)

    #Clear text file
    file = open("Q1.txt", "w")
    file.close()

    # 1.1
    num_sents = get_num_sentences(doc)

    # 1.2
    vps = verbs_per_sentence(doc, num_sents)

    # 1.3
    preps = get_prepositions(doc)
    # print("number of prepositions", str(preps[0]))

    # 1.4
    number_of_entities(doc)

    log("Finished main.")


main()
