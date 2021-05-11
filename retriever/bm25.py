import json
import os
from rank_bm25 import BM25Okapi
from tqdm import tqdm
from utils import get_chunks_by_qa

ques_json = json.load(open("../data/tst.json"))
article_seg_json = json.load(open("../data/article_segment.json"))

output_name_all = "output_retriever_rank_bm25_all.json"
if not os.path.exists(output_name_all):
    output_retriever_rank = {}
    for qa_pair in tqdm(ques_json):
        # article_full_id_list = qa_pair["article_full_id"]
        chunks_dict = get_chunks_by_qa(qa_pair, article_seg_json)
        corpus = []
        for chunk_key, chunk_value in chunks_dict.items():
            utters = ["{}: {}".format(seg["speaker"], seg["text"]) for seg in chunk_value["seg_dialog"]]
            corpus.append(" ".join(utters))
        tokenized_corpus = [doc.split(" ") for doc in corpus]
        bm25 = BM25Okapi(tokenized_corpus)
        tokenized_query = qa_pair["question"].split(" ")
        doc_scores = bm25.get_scores(tokenized_query)

        output_retriever_rank[qa_pair["id"]] = {}
        for chunk_i, (chunk_key, chunk_value) in enumerate(chunks_dict.items()):
            output_retriever_rank[qa_pair["id"]][chunk_key] = doc_scores[chunk_i]

    with open(output_name_all, "w") as fout:
        json.dump(output_retriever_rank, fout, indent=2)
else:
    output_retriever_rank = json.load(open(output_name_all))

output_retriever = []
for key, value in output_retriever_rank.items():
    sort_dict = sorted(value.items(), key=lambda x: x[1])[::-1]
    output_retriever.append({
        "id": key,
        "retrieved_article_segment_id": sort_dict[0][0] 
    })
with open("output_retriever_rank_bm25.json", "w") as fout:
    json.dump(output_retriever, fout, indent=2)
