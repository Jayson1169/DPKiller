import json

import spacy
from spacy.matcher import Matcher

patterns = json.load(open('patterns.json'))
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

for dp_name, dp_patterns in patterns.items():
    matcher.add(dp_name, dp_patterns)


def match(filename: str) -> dict:
    file = open(filename)
    data = json.load(file)
    compos = {}
    for compo in data['compos']:
        if compo['class'] != 'Text':
            continue
        doc = nlp(compo['text_content'])
        matches = matcher(doc)
        compo_id = compo['id']
        for match_id, start, end in matches:
            pattern = nlp.vocab.strings[match_id]
            span = doc[start:end]

            if compo_id not in compos.keys():
                compos[compo_id] = {}
                compos[compo_id]["compo_info"] = compo
                compos[compo_id]["text_analysis"] = {}
                compos[compo_id]["text_analysis"][pattern] = {"doc": doc.text, "span": span.text}
            elif pattern not in compos[compo_id]["text_analysis"].keys():
                compos[compo_id]["text_analysis"][pattern] = {"doc": doc.text, "span": span.text}
            else:
                current_span_length = len(compos[compo_id]["text_analysis"][pattern]["span"])
                if len(span.text) > current_span_length:
                    compos[compo_id]["text_analysis"][pattern] = {"doc": doc.text, "span": span.text}

    file.close()
    return compos
