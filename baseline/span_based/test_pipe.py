from transformers import pipeline
import json
import os
from tqdm import tqdm

def run_zeroshot(fw_name, quesion_json, article_json, model,version, gpu, retriver="None"):
    if not os.path.exists(fw_name):
        if retriver == "bm25":
            retrieved = json.load(open("../retriever/output_retriever_rank_bm25.json"))
            retrieve_article = {}

            for r in retrieved:
                retrieve_article[r['id']] = r['retrieved_article_segment_id']
        elif retriver == "dpr":
            retrieved = json.load(open("../retriever/myEfficientQA/output_retriever_rank_dpr-wiki.json"))
            retrieve_article = {}
            for r in retrieved:
                retrieve_article[r['id']] = r['retrieved_article_segment_id']


        qa_pipeline_pred = {}
        qa_pipeline = pipeline("question-answering",model=mod,device=gpu)
        for qa_pair in tqdm(quesion_json):
            question = qa_pair["question"].lower()
            if retriver == "None":
                context = article_json[qa_pair["article_segment_id"]]["seg_dialog"]
            else:
                context = article_json[retrieve_article[qa_pair["id"]]]["seg_dialog"]

            context = " ".join([f'{c["speaker"]}: {c["text"]}' for c in context]).lower()
            if version == 1:
                answer = qa_pipeline(question=question, context=context)
            else:
                answer = qa_pipeline(question=question, context=context,handle_impossible_answer=True)
                if answer["answer"] == "": answer["answer"] = "unanswerable"
            qa_pipeline_pred[qa_pair["id"]] = answer["answer"].lower()
        with open(fw_name, "w") as fout:
            json.dump(qa_pipeline_pred, fout, indent=2)
    else:
        qa_pipeline_pred = json.load(open(fw_name))


if __name__ == "__main__":
    
    version = 2
    gpu = 6
    ques_json = json.load(open(f"data/QAConv_FINAL/QAConv-V{version}/tst.json"))
    article_json = json.load(open("data/QAConv_FINAL/article_segment.json"))

    if version ==1:
        for mod in ["distilbert-base-uncased-distilled-squad","csarron/bert-base-uncased-squad-v1","bert-large-uncased-whole-word-masking-finetuned-squad","csarron/roberta-base-squad-v1","csarron/roberta-large-squad-v1"]:
            name = mod.split('/')[1] if "/" in mod else mod
            pred_path = f"../prediction_v1/{name}-zero-shot_new_test.json"
            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu)

        for mod in ["save_v1/distilbert","save_v1/bert-base","save_v1/bert-large-largebsz","save_v1/roberta-base","save_v1/roberta-large"]:
            name = mod.split('/')[1] if "/" in mod else mod
            pred_path = f"../prediction_v1/{name}-finetuned_new_test.json"

            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu)

    if version == 2:

        for mod in ["ahotrod/albert_xxlargev1_squad2_512","twmkn9/distilbert-base-uncased-squad2","deepset/roberta-base-squad2","deepset/roberta-large-squad2","deepset/bert-base-cased-squad2","deepset/bert-large-uncased-whole-word-masking-squad2"]:
            name = mod.split('/')[1] if "/" in mod else mod
            pred_path = f"../prediction_v2/{name}-zero-shot_new_test.json"
            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu)

            pred_path = f"../prediction_v2_retrived/{name}-zero-shot_new_test_bm25.json"
            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu,retriver="bm25")
            
            pred_path = f"../prediction_v2_retrived/{name}-zero-shot_new_test_dpr.json"
            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu,retriver="dpr")


        for mod in ["save_v2/albert_xxl","save_v2/distilbert","save_v2/bert-base","save_v2/bert-large-largebsz","save_v2/roberta-base","save_v2/roberta-large"]:
            name = mod.split('/')[1] if "/" in mod else mod
            
            pred_path = f"../prediction_v2/{name}-finetuned_new_test.json"
            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu)
            
            pred_path = f"../prediction_v2_retrived/{name}-finetuned_new_test_bm25.json"
            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu,retriver="bm25")
            
            pred_path = f"../prediction_v2_retrived/{name}-finetuned_new_test_dpr.json"
            run_zeroshot(pred_path, ques_json, article_json, mod, version=version,gpu=gpu,retriver="dpr")