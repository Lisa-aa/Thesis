from transformer_srl import dataset_readers, models, predictors
def predictFunction(sent):
    predictor = predictors.SrlTransformersPredictor.from_path("srl_bert_base_conll2012.tar.gz", "transformer_srl")
    try:
        result = predictor.predict_instances(predictor._sentence_to_srl_instances({"sentence": sent}))
        return(verbLabels(result))
    except:
        return([])

def verbLabels(dict):
    verbs = []
    for verb_info in dict["verbs"]:
        verbs.append([verb_info["verb"],verb_info["frame"]])
    return verbs