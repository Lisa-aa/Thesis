import sys
from io import open
from propbankLabelling import predictFunction
from ReplaceLabel2 import replaceSentenceLabel

if __name__ == "__main__":
    """Arguments: an amconll file should be given after -file
       Result: amconll file with frameset labels of verbs replaced
    """
    args = sys.argv[1:]
    if args[0] == "-file":
        file = args[1]
    data_file = open(file, "r", encoding="utf-8")
    lines = data_file.readlines()
    data_file.close()
    sentences = []
    counter = 0
    sentence = ""
    AMsentences = []
    AMsentence = ""
    for line in lines:
        try:
            AMsentence += line
            words = line.split("\t") 
            id = words[0]
            if str(counter + 1) == id:
                sentence += words[1] + " "
                counter += 1
            else:
                if sentence != "" :
                    sentences.append(sentence)
                sentence = ""
                counter = 0 
            if line == "\n":
                AMsentences.append(AMsentence)
                AMsentence = ""
        except:
            None
    if sentence != "" :
        sentences.append(sentence)
    AMsentences.append(AMsentence)
    verblist = []
    data_file = open("output2.txt", "w", encoding="utf-8")
    for (AMsentence,sentence) in zip(AMsentences,sentences):
        try:
            verblist = predictFunction(sentence)
            replaceSentenceLabel(verblist, AMsentence, data_file)
        except:
            None
    data_file.close()
