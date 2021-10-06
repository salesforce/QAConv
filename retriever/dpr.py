"""
 * Copyright (c) 2021, salesforce.com, inc.
 * All rights reserved.
 * SPDX-License-Identifier: BSD-3-Clause
 * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

"""

import json
import os
from tqdm import tqdm
from utils import get_chunks_by_qa
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-d', '--data_name', default='tst')
parser.add_argument('-o', '--output_name', default="output_retriever_rank_bm25")
parser.add_argument('-r', '--dpr_result', required=True)  # DPR/outputs/2021-08-11/16-40-38/qaconv_test_dpr_results.json
args = parser.parse_args()
data_name = args.data_name

ques_json = json.load(open("../data/{}.json".format(data_name)))
article_seg_json = json.load(open("../data/article_segment.json"))
dpr_result_json = json.load(open(args.dpr_result))

assert len(ques_json) == len(dpr_result_json)

output_name_all = "{}_all_{}.json".format(args.output_name, data_name)
if not os.path.exists(output_name_all):
    output_retriever_rank = {}
    for qa_idx, qa_pair in enumerate(tqdm(ques_json)):
        score_dict = {item["title"]: item["score"] for item in dpr_result_json[qa_idx]["ctxs"]}
        chunks_dict = get_chunks_by_qa(qa_pair, article_seg_json)
        output_retriever_rank[qa_pair["id"]] = {}
        for chunk_i, (chunk_key, chunk_value) in enumerate(chunks_dict.items()):
            output_retriever_rank[qa_pair["id"]][chunk_key] = score_dict[chunk_key]
    with open(output_name_all, "w") as fout:
        json.dump(output_retriever_rank, fout, indent=2)
else:
    output_retriever_rank = json.load(open(output_name_all))

output_retriever = []
for idx, item in enumerate(dpr_result_json):
    output_retriever.append({
        "id": ques_json[idx]["id"],
        "retrieved_article_segment_id": item["ctxs"][0]["title"]
    })
with open("{}_{}.json".format(args.output_name, data_name), "w") as fout:
    json.dump(output_retriever, fout, indent=2)
