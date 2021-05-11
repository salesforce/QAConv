import json
import pylcs
import random
# import stanza
# import benepar, spacy
from collections import defaultdict
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_theme(style="whitegrid")


# nlp = spacy.load('en_core_web_sm')
# if spacy.__version__.startswith('2'):
#     nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))
# else:
#     nlp.add_pipe("benepar", config={"model": "benepar_en3"})


def preproc(question,version):
    print(len(question))
    cnt_error = 0
    dataset = []
    for q_i, q in enumerate(question):
        if version == 1:
            dialogue_history = " ".join([f'{c["speaker"]}: {c["text"]}'.replace("\n"," ").replace("\t"," ") for c in article[q["article_segment_id"]]['seg_dialog']])
            idx_start = dialogue_history.lower().find(q["answers"][0].lower())
            lsc = pylcs.lcs2(q["answers"][0].lower(), dialogue_history.lower())
            if idx_start == -1 and lsc!=0:
                temp_anw  = q["answers"][0].lower()[:lsc-1]
                idx_start = dialogue_history.lower().find(temp_anw)
                if idx_start == -1 and lsc!=0:
                    temp_anw  = q["answers"][0].lower()[-lsc:]
                    idx_start = dialogue_history.lower().find(temp_anw)


            if idx_start != -1 and q["answers"][0].lower()!="":
                temp = {
                        # "title":q["article_segment_id"]+"___"+str(q_i),
                        "paragraphs": [
                            {
                            "context": dialogue_history.lower(),
                            "qas":[
                                    {
                                    "answers":[
                                        {
                                        "answer_start":idx_start,
                                        "text":q["answers"][0].lower()
                                        }
                                    ],
                                    "question":q["question"].lower(),
                                    "id":q["id"]
                                    }
                                ]
                            }
                            ]
                        }
                dataset.append(temp)
            else:
                cnt_error += 1
        else:
            dialogue_history = " ".join([f'{c["speaker"]}: {c["text"]}'.replace("\n"," ").replace("\t"," ") for c in article[q["article_segment_id"]]['seg_dialog']])
            if len(q["answers"])>0:
                idx_start = dialogue_history.lower().find(q["answers"][0].lower())
                lsc = pylcs.lcs2(q["answers"][0].lower(), dialogue_history.lower())
                if idx_start == -1 and lsc!=0:
                    temp_anw  = q["answers"][0].lower()[:lsc-1]
                    idx_start = dialogue_history.lower().find(temp_anw)
                    if idx_start == -1 and lsc!=0:
                        temp_anw  = q["answers"][0].lower()[-lsc:]
                        idx_start = dialogue_history.lower().find(temp_anw)

                if idx_start != -1 and q["answers"][0].lower()!="":
                    temp = {
                            # "title":q["article_segment_id"]+"___"+str(q_i),
                            "paragraphs": [
                                {
                                "context": dialogue_history.lower(),
                                "qas":[
                                        {
                                        "question":q["question"].lower(),
                                        "id":q["id"],
                                        "answers":[
                                            {
                                            "answer_start":idx_start,
                                            "text":q["answers"][0].lower()
                                            }
                                        ],
                                        "is_impossible": False
                                        }
                                    ]
                                }
                                ]
                            }
                    dataset.append(temp)
                else:
                    cnt_error += 1
            else:
                temp = {
                        # "title":q["article_segment_id"]+"___"+str(q_i),
                        "paragraphs": [
                            {
                            "context": dialogue_history.lower(),
                            "qas":[
                                    {
                                    "plausible_answers": [],
                                    "question":q["question"].lower(),
                                    "id":q["id"],
                                    "answers":[],
                                    "is_impossible": True
                                    }
                                ]
                            }
                            ]
                        }
                dataset.append(temp)

    print(f"NUMBER OF SKIPPED QA:{cnt_error}")
    print(len(dataset))
    return dataset

version = 1
article = json.load(open("../data/QAConv_FINAL/article_segment.json","r"))
question_trn = json.load(open(f"../data/QAConv_FINAL/QAConv-V{version}/trn.json","r"))
question_val = json.load(open(f"../data/QAConv_FINAL/QAConv-V{version}/val.json","r"))
question_tst = json.load(open(f"../data/QAConv_FINAL/QAConv-V{version}/tst.json","r"))

with open(f'../data/QAConv_FINAL/QA4KRC_TRAIN_{version}.json', 'w') as outfile:
    json.dump({"data":preproc(question_trn,version),"version":float(version)}, outfile, indent=4)

with open(f'../data/QAConv_FINAL/QA4KRC_VALID_{version}.json', 'w') as outfile:
    json.dump({"data":preproc(question_val,version),"version":float(version)}, outfile, indent=4)

with open(f'../data/QAConv_FINAL/QA4KRC_TEST_{version}.json', 'w') as outfile:
    json.dump({"data":preproc(question_tst,version),"version":float(version)}, outfile, indent=4)



# datafinal_TRAIN = {"data":dataset[:int(len(dataset)*0.80)],"version":1.0}
# datafinal_VALID = {"data":dataset[int(len(dataset)*0.80):],"version":1.0}
# datafinal_ALL = {"data":dataset,"version":1.0}
# print(len(dataset))
# with open(f'QA4KRC_TRAIN.json', 'w') as outfile:
#     json.dump(datafinal_TRAIN, outfile, indent=4)

# with open(f'QA4KRC_VALID.json', 'w') as outfile:
#     json.dump(datafinal_VALID, outfile, indent=4)

# with open(f'QA4KRC_ALL.json', 'w') as outfile:
#     json.dump(datafinal_ALL, outfile, indent=4)
# stats = defaultdict(list)
# stats_all = defaultdict(int)
# stats_ent = defaultdict(list)
# for i, d in enumerate(datafinal_VALID["data"]):
#     ans = d["paragraphs"][0]['qas'][0]['answers'][0]["text"]
#     # print(i, ans)
#     doc = nlp(ans)
#     entities = list()
#     for ent in doc.ents:
#         entities.append([ent.text,ent.label_])
#     sent = list(doc.sents)[0]
#     if len(entities):

#         stats_ent[entities[0][1]].append(ans)
#         stats_all[entities[0][1]]+=1

#     else:
#         label = sent._.labels[0]    
#         stats_all[label]+=1
#         stats[label].append(ans)


# for k, v in sorted(stats_all.items(), key=lambda item: item[1]):
#     if k in stats:
#         print(random.sample(stats[k], 2 if len(stats[k])>1 else 1))
#     elif(k in stats_ent):
#         print(random.sample(stats_ent[k], 10 if len(stats_ent[k])>10 else 1))
#     print(k,(v/len(datafinal_VALID["data"]))*100)   
#     print()
# print(len(stats.keys()))






    
# print(f"TRAIN LEN: {len(dataset[:int(len(dataset)*0.80)])}")
# print(f"VALID LEN: {len(dataset[int(len(dataset)*0.80):])}")









## OLD STUFF TO DELETE
# nlp = stanza.Pipeline('en', processors='tokenize,pos,ner')
# if q['answer'].isnumeric():   
#     stats["Other_Numeric"] += 1
# else:      
# print(f"ANSWER: {q['answer']}")


# print(f"ENT:{entities}")
# print(f"PARSER: {sent._.labels[0]}")


# print(sent._.parse_string)
# # (S (NP (NP (DT The) (NN time)) (PP (IN for) (NP (NN action)))) (VP (VBZ is) (ADVP (RB now))) (. .))
# print(sent._.labels)
# # ('S',)

# print(list(sent._.children))
# The time for action
# doc = nlp(q["answer"])
# for sent in doc.sentences:
#     tags = [word.upos for word in sent.words]
#     tags_x = [word.xpos for word in sent.words]
#     print({ent.text: ent.type for ent in doc.ents})
#     print(tags)
#     print(tags_x)
# print()
# print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')

# input()
# print(temp)