"""
 * Copyright (c) 2021, salesforce.com, inc.
 * All rights reserved.
 * SPDX-License-Identifier: BSD-3-Clause
 * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

"""

import json
import os
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-d', '--data_name', default='tst')
parser.add_argument('-o', '--output_name', default="output_retriever_rank_bm25")
args = parser.parse_args()
data_name = args.data_name

ques_json = json.load(open("../data/{}.json".format(data_name)))

def recall_k(match_position, k):
    return np.mean([1 if pos <= k else 0 for pos in match_position])

# bm25
output_retriever_rank = json.load(open("{}_all_{}.json".format(args.output_name, data_name)))
output_retriever = {}
for key, value in output_retriever_rank.items():
    sort_dict = sorted(value.items(), key=lambda x: x[1])[::-1]
    output_retriever[key] = [s[0] for s in sort_dict]

match_position = []
for qa_pair in ques_json:
    retrieved_docs = output_retriever[qa_pair["id"]]
    for i in range(len(retrieved_docs)):
        if retrieved_docs[i] == qa_pair["article_segment_id"]:
            match_position.append(i+1)
            break

for k in [1,3,5,10]:
    print("BM25 Recall@{}".format(k), recall_k(match_position, k))