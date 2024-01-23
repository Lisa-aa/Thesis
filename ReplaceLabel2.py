import re
def replaceSentenceLabel(labels, data, data_file):
    data = data.split("\n")
    count = 0
    for sentences in data:
        if sentences == "":
            if count == 0:
                data_file.write("\n")
                count = 1
        else:
            words =sentences.split("\t")
            try: 
                word2 = ""
                if re.search("\w", labels[0][0]) == None:
                    labels = labels[1:]
                if re.search("-", words[1]) != None:
                    splitting = words[1].split("-")
                    word = splitting[0]
                    word2 = splitting[1]
                else:
                    word = words[1]
                if word == labels[0][0] or word2 == labels[0][0]:
                    if (words[7][:(len(words[7])-3)] == "$LEMMA$" and words[3] ==labels[0][0] ) or words[7][:(len(words[7])-3)] == labels[0][0] :
                        words[7] = labels[0][1][:(len(labels[0][1])-3)] + "-" + labels[0][1][(len(labels[0][1])-2):]
                    labels = labels[1:]
                data_file.write(("\t").join(words)+ "\n")
            except:
                data_file.write(("\t").join(words)+ "\n")
                