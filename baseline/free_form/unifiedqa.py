import json
import os
from tqdm import tqdm
from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch
import argparse

def allocate2gpu(x, name):
    if torch.cuda.is_available() and "11b" not in name:
        x = x.cuda()
    return x

def run_model(model_name, model, tokenizer, input_string, **generator_args):
    input_ids = tokenizer.encode(input_string, return_tensors="pt")
    input_ids = allocate2gpu(input_ids, model_name)
    res = model.generate(input_ids, **generator_args)
    return tokenizer.batch_decode(res, skip_special_tokens=True)


def run_zeroshot(model_name, model, tokenizer, fw_name, quesion_json, article_json):
    if not os.path.exists(fw_name):
        qa_pipeline_pred = {}
        for qa_pair in tqdm(quesion_json):
            question = qa_pair["question"]
            context = article_json[qa_pair["article_segment_id"]]["seg_dialog"]
            context = " ".join(['{}: {}'.format(c["speaker"], c["text"].replace("\n"," ")) for c in context])
            answer = run_model(model_name, model, tokenizer, f'{question} \n {context}')
            qa_pipeline_pred[qa_pair["id"]] = answer[0]
        with open(fw_name, "w") as fout:
            json.dump(qa_pipeline_pred, fout, indent=2)
    else:
        qa_pipeline_pred = json.load(open(fw_name))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run ...')
    parser.add_argument('-m',  '--model', type=str, required=True,
                    help='model name')
    parser.add_argument('-q',  '--ques_json_file', type=str, required=True,
                    help='QA data source')
    parser.add_argument('-p',  '--prediction', type=str, default="../../prediction",
                    help='output prediction path')
    args = parser.parse_args()

    if not os.path.exists(args.prediction):
        os.makedirs(args.prediction)

    model_name = args.model #"allenai/unifiedqa-t5-3b"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    model = allocate2gpu(model, args.model)

    ques_json = json.load(open(args.ques_json_file))
    article_json = json.load(open("../../data/article_segment.json"))

    pred_path = os.path.join(args.prediction, "{}-zeroshot.json".format(model_name.split("/")[1]))
    run_zeroshot(args.model, model, tokenizer, pred_path, ques_json, article_json)

