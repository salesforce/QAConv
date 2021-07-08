"""
 * Copyright (c) 2021, salesforce.com, inc.
 * All rights reserved.
 * SPDX-License-Identifier: BSD-3-Clause
 * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

"""

import json
import pylcs
import random
from collections import defaultdict

def preproc(question,article):
    cnt_error = 0
    dataset = []
    error_dataset = []
    for q_i, q in enumerate(question):
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
                temp = {
                        "paragraphs": [
                            {
                            "context": dialogue_history.lower(),
                            "qas":[
                                    {
                                    "question":q["question"].lower(),
                                    "id":q["id"],
                                    "answers":[
                                        {
                                        "text":q["answers"][0].lower()
                                        }
                                    ],
                                    }
                                ]
                            }
                            ]
                        }
                error_dataset.append(temp)
                cnt_error += 1
        else:
            temp = {
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

    print(f"NUMBER OF SKIPPED QA CANNOT FIND SPAN: {cnt_error}")
    print(f"NUMBER of QA FOUND: {len(dataset)}")
    return dataset, error_dataset

article = json.load(open("../../data/article_segment.json","r"))
question_trn = json.load(open(f"../../data/trn.json","r"))
question_val = json.load(open(f"../../data/val.json","r"))
question_tst = json.load(open(f"../../data/tst.json","r"))

print("Run train set...")
dataset, error_dataset = preproc(question_trn, article)
with open(f'../../data/QAConv-squad-filtered_TRAIN.json', 'w') as outfile:
    json.dump({"data":dataset, "version":2.0}, outfile, indent=4)
with open(f'../../data/QAConv-squad-error_TRAIN.json', 'w') as outfile:
    json.dump({"data":error_dataset, "version":2.0}, outfile, indent=4)

print("Run val set...")
dataset, error_dataset = preproc(question_val, article)
with open(f'../../data/QAConv-squad-filtered_VALID.json', 'w') as outfile:
    json.dump({"data":dataset, "version":2.0}, outfile, indent=4)
with open(f'../../data/QAConv-squad-error_VALID.json', 'w') as outfile:
    json.dump({"data":error_dataset, "version":2.0}, outfile, indent=4)

print("Run test set...")
dataset, error_dataset = preproc(question_tst, article)
with open(f'../../data/QAConv-squad-filtered_TEST.json', 'w') as outfile:
    json.dump({"data":dataset, "version":2.0}, outfile, indent=4)
with open(f'../../data/QAConv-squad-error_TEST.json', 'w') as outfile:
    json.dump({"data":error_dataset, "version":2.0}, outfile, indent=4)

