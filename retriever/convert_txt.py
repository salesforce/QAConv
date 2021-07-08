import json
import os
import argparse
parser = argparse.ArgumentParser(description='')
parser.add_argument('-d', '--data_name', default='tst')
args = parser.parse_args()
data_name = args.data_name

mapping = {
    "trn": "train",
    "val": "val",
    "tst": "test"
}

for method in ["bm25"]:

    output_folder = "../data/nmt-{}-{}".format(method, data_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    article_json = json.load(open("../data/article_segment.json"))

    if method == "bm25":
        retriever_json = json.load(open("output_retriever_rank_bm25_{}.json".format(data_name)))
    
    retriever_json = {s["id"]:s["retrieved_article_segment_id"] for s in retriever_json}

    src_all, tgt_all = [], []
    ques_json = json.load(open("../data/{}.json".format(data_name)))
    for qa_pair in ques_json:
        context = article_json[retriever_json[qa_pair["id"]]]["seg_dialog"]
        context = " ".join(['{}: {}'.format(c["speaker"], c["text"].replace("\n", " ")) for c in context])
        src = "{} </s> {}".format(qa_pair["question"].strip(), context.strip())
        if len(qa_pair["answers"]):
            tgt = qa_pair["answers"][0].strip() # here we only use the first potential answers
        else: # unanswerable
            tgt = "unanswerable"
        src_all.append(src)
        tgt_all.append(tgt)

    with open("{}/test.source".format(output_folder), "w") as fout:
        fout.write("\n".join(src_all))
    with open("{}/test.target".format(output_folder), "w") as fout:
        fout.write("\n".join(tgt_all))
