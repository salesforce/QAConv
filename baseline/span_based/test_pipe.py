from transformers import pipeline
import json
import os
from tqdm import tqdm
import argparse

def run_zeroshot(fw_name, quesion_json, article_json, model, gpu, retriver="None"):
    if not os.path.exists(fw_name):
        if retriver == "bm25":
            print("Use BM25 retrieved dialogue")
            retrieved = json.load(open("../../retriever/output_retriever_rank_bm25.json"))
            retrieve_article = {}

            for r in retrieved:
                retrieve_article[r['id']] = r['retrieved_article_segment_id']
        elif retriver == "dpr":
            print("Use DPR retrieved dialogue")

            retrieved = json.load(open("../../retriever/myEfficientQA/output_retriever_rank_dpr-wiki.json"))
            retrieve_article = {}
            for r in retrieved:
                retrieve_article[r['id']] = r['retrieved_article_segment_id']
        else:
            print("Use gold dialogue")

        qa_pipeline_pred = {}
        qa_pipeline = pipeline("question-answering",model=mod,device=gpu)
        for qa_pair in tqdm(quesion_json):
            question = qa_pair["question"].lower()
            if retriver == "None":
                context = article_json[qa_pair["article_segment_id"]]["seg_dialog"]
            else:
                context = article_json[retrieve_article[qa_pair["id"]]]["seg_dialog"]

            context = " ".join([f'{c["speaker"]}: {c["text"]}' for c in context]).lower()
            answer = qa_pipeline(question=question, context=context,handle_impossible_answer=True)
            if answer["answer"] == "": answer["answer"] = "unanswerable"
            qa_pipeline_pred[qa_pair["id"]] = answer["answer"].lower()
        with open(fw_name, "w") as fout:
            json.dump(qa_pipeline_pred, fout, indent=2)
    else:
        qa_pipeline_pred = json.load(open(fw_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Test zero-shot and finetuned models')
    parser.add_argument("--gpu", type=int, default=0, help="gpu to run")
    OPTS = parser.parse_args()
    gpu = OPTS.gpu
    ques_json = json.load(open("../../data/tst.json"))
    article_json = json.load(open("../../data/article_segment.json"))

    ## ZERO SHOT
    for mod in ["twmkn9/distilbert-base-uncased-squad2","deepset/roberta-base-squad2","deepset/roberta-large-squad2","deepset/bert-base-cased-squad2","deepset/bert-large-uncased-whole-word-masking-squad2"]:
        name = mod.split('/')[1] if "/" in mod else mod
        pred_path = f"../../prediction/{name}-zero-shot.json"
        run_zeroshot(pred_path, ques_json, article_json, mod,gpu=gpu)

        pred_path = f"../../prediction/{name}-zero-shot_bm25.json"
        run_zeroshot(pred_path, ques_json, article_json, mod,gpu=gpu,retriver="bm25")
        
        #pred_path = f"../../prediction/{name}-zero-shot_new_test_dpr.json"
        #run_zeroshot(pred_path, ques_json, article_json, mod,gpu=gpu,retriver="dpr")

    ## finetuned models
    for mod in ["save/distilbert","save/bert-base","save/bert-large-largebsz","save/roberta-base","save/roberta-large"]:
        name = mod.split('/')[1] if "/" in mod else mod
        
        pred_path = f"../../prediction/{name}-finetuned.json"
        run_zeroshot(pred_path, ques_json, article_json, mod,gpu=gpu)
        
        pred_path = f"../../prediction/{name}-finetuned_bm25.json"
        run_zeroshot(pred_path, ques_json, article_json, mod,gpu=gpu,retriver="bm25")
        
        #pred_path = f"../../prediction/{name}-finetuned_new_test_dpr.json"
        #run_zeroshot(pred_path, ques_json, article_json, mod,gpu=gpu,retriver="dpr")
