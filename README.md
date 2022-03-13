# QAConv: Question Answering on Informative Conversations

[Chien-Sheng (Jason) Wu](https://jasonwu0731.github.io/), [Andrea Madotto](https://andreamad8.github.io/), [Wenhao Liu](https://www.linkedin.com/in/owenwenhao), [Pascale Fung](https://pascale.home.ece.ust.hk/about.html), [Caiming Xiong](http://cmxiong.com/).

[[paper]](https://arxiv.org/abs/2105.06912) [[blog]]()

## Citation
Please cite our work if you use the data or code in this repository
```
@article{wu2021qaconv,
  title={QAConv: Question Answering on Informative Conversations},
  author={Wu, Chien-Sheng and Madotto, Andrea and Liu, Wenhao and Fung, Pascale and Xiong, Caiming},
  journal={arXiv preprint arXiv:2105.06912},
  year={2021}
}
```

## Abstract
This paper introduces QAConv, a new question answering (QA) dataset that uses conversations as a knowledge source. We focus on informative conversations including business emails, panel discussions, and work channels. Unlike opendomain and task-oriented dialogues, these conversations are usually long, complex, asynchronous, and involve strong domain knowledge. In total, we collect 34,204 QA pairs, including span-based, free-form, and unanswerable questions, from 10,259 selected conversations with both human-written and machine-generated questions. We segment long conversations into chunks, and use a question generator and dialogue summarizer as auxiliary tools to collect multi-hop questions. The dataset has two testing scenarios, chunk mode and full mode, depending on whether the grounded chunk is provided or retrieved from a large conversational pool. Experimental results show that state-of-the-art QA systems trained on existing QA datasets have limited zero-shot ability and tend to predict our questions as unanswerable. Fine-tuning such systems on our corpus can achieve significant improvement up to 23.6% and 13.6% in both chunk mode and full mode, respectively.


## Dataset
Unzip the `data.zip` file and files below are shown under the data folder.

* Question-Answer files (`trn.json`, `val.json`, `tst.json`)
```
[
  {
    "id": "tst-0",
    "article_segment_id": "newsdial-1068",
    "article_full_id": [
      "newsidal-NPR-170"
    ],
    "QG": false,
    "question": "Which contact number is available for callers on the line said by NEAL CONAN?",
    "answers": [
      "800-989-8255"
    ]
  }
]
```
* Document files (`article_segment.json`, `article_full.json`)
```
{
"newsdial-1068": {
    "prev_ctx": [
      {
        "id": "newsidal-NPR-170-133",
        "speaker": "AUBREY JEWETT",
        "text": "Up till about a week ago, I was among the many who thought, OK, in the end, Romney's going to pull it out, but I'll tell you, He is in a world of trouble right now in Florida. He may hang on, but Gingrich is really surging in the polls."
      }
    ],
    "seg_dialog": [
      {
        "id": "newsidal-NPR-170-134",
        "speaker": "NEAL CONAN, HOST",
        "text": "Lucy Morgan, what do you think?"
      },
      {
        "id": "newsidal-NPR-170-135",
        "speaker": "LUCY MORGAN",
        "text": "I think Romney will pull it out. The newest poll, the better of the polls, Quinnipiac, came out this morning giving Romney a one-point advantage, within the margin of error. But I think the advantage he has is the early vote and the establishment Republicans who are behind him."
      },
      ...
    ],
    "word_count": 204
  },
}
``` 
```
{
"newsidal-NPR-170": [
    {
      "id": "newsidal-NPR-170-0",
      "speaker": "NEAL CONAN, HOST",
      "text": "This is TALK OF THE NATION. I'm Neal Conan in Orlando. Gabby Giffords bows out of Congress, Michele Bachmann vows to return, Newt reborn in South Carolina, while Santorum struggles to stay afloat. It's Wednesday and time for a..."
    },
    {
      "id": "newsidal-NPR-170-1",
      "speaker": "RICK SANTORUM",
      "text": "These are not cogent thoughts..."
    },
    {
    ...
  ]
}
```

## Trained Models

You can load our trained QA models using the huggingface library. 

### Free-form

* t5-base: Salesforce/qaconv-unifiedqa-t5-base
* t5-large: Salesforce/qaconv-unifiedqa-t5-large
* t5-3B: Salesforce/qaconv-unifiedqa-t5-3b

You can directly run the trained model on any conversations, 
```
from transformers import AutoTokenizer, T5ForConditionalGeneration

model_name = "Salesforce/qaconv-unifiedqa-t5-base" # you can specify the model size here
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def run_model(input_string, **generator_args):
    generator_args["max_length"] = 20
    generator_args["min_length"] = 1
    input_ids = tokenizer.encode(input_string, return_tensors="pt")
    res = model.generate(input_ids, **generator_args)
    return tokenizer.batch_decode(res, skip_special_tokens=True)
```
For instance, here is how you can use it to answer a question (question and conversation are separated by </s>):
```
answer = run_model("Why Salesforce accquire Slack? </s> Jason: Boom! Check the news of Salesforce. Andrea: Wowm don't know why they want to accquire Slack. Jason: This will give them a unified platform for connecting employees, customers and partners. Debbie: How much did they pay? Andrea: $27.7 billion I saw.")
```
which gives `['To have a unified platform for connecting employees, customers and partners.']`

### Span-base
* roberta-large: Salesforce/qaconv-roberta-large-squad2
* bert-large: Salesforce/qaconv-bert-large-uncased-whole-word-masking-squad2

You can directly run the trained model on any conversations, 
```
from transformers import pipeline
qa_pipeline = pipeline("question-answering",model="Salesforce/qaconv-roberta-large-squad2")
```
For instance, here is how you can use it to answer a question
```
answer = qa_pipeline(question="Why Salesforce accquire Slack?", context="Jason: Boom! Check the news of Salesforce. Andrea: Wowm don't know why they want to accquire Slack. Jason: This will give them a unified platform for connecting employees, customers and partners. Debbie: How much did they pay? Andrea: $27.7 billion I saw.", handle_impossible_answer=True)
```
which gives `{'score': 0.33785736560821533, 'start': 127, 'end': 194, 'answer': 'a unified platform for connecting employees, customers and partners'}`


## Running Baselines

### Dependency
First, install requirements by `pip install -r requirements.txt`. 

If you encounter error while installing fairscale with error message `AttributeError: type object 'Callable' has no attribute '_abc_registry'`, try `pip uninstall typing` then redo the installation. 

### Retriever
* Run BM25 (./retriever)
```console
❱❱❱ cd retriever
❱❱❱ ./run_retriver.sh tst
```

* DPR-wiki
We release the retrieved top-1 results at `./retriever/output_retriever_rank_dpr-wiki.json`. Please check the [DPR repository](https://github.com/facebookresearch/DPR) for details.

### Free-form

* Preprocess (./data)
```console
❱❱❱ python convert_txt.py
```

* Zero-shot (./baseline/free_form/)
```console
❱❱❱ ./run_zs.sh
```

* Training (./baseline/free_form/finetuning/)
```console
❱❱❱ ./run_finetune.sh 0,1 2 allenai/unifiedqa-t5-base 8
```

* Inference (./baseline/free_form/finetuning/)
```console
❱❱❱ ./run_eval.sh 0 ../../../data/nmt/ ../../../data/ output/qaconv-allenai/unifiedqa-t5-base/ unifiedqa-t5-base output/qaconv-allenai/unifiedqa-t5-base/prediction/
❱❱❱ ./run_eval.sh 0 ../../../data/nmt-bm25/ ../../../data/ output/qaconv-allenai/unifiedqa-t5-base/ unifiedqa-t5-base-bm25 output/qaconv-allenai/unifiedqa-t5-base/prediction-bm25/
❱❱❱ ./run_eval.sh 0 ../../../data/nmt-dpr/ ../../../data/ output/qaconv-allenai/unifiedqa-t5-base/ unifiedqa-t5-base-dprwiki output/qaconv-allenai/unifiedqa-t5-base/prediction-dprwiki/
```

### Span-base

* Preprocess (./baseline/span_based)
```console
❱❱❱ cd ./baseline/span_based
❱❱❱ python preproc.py
```

* Training (./baseline/span_based)
```console
❱❱❱ ./run_qa.sh
```

* Inference (./baseline/span_based)
```console
❱❱❱ python test_pipe.py --gpu 0
```

### Evaluation 

* Evaluate one single prediction file (./)
```console
❱❱❱ python evaluate.py data/tst.json prediction/unifiedqa-t5-base-zeroshot.json
```

* Evaluate the whole folder with all the prediction files (./)
```console
❱❱❱ python evaluate.py data/tst.json prediction/ --folder
```

## Ethics
We have used only the publicly available transcripts data and adhere to their guideline, for example, the Media data is for research-purpose only and cannot be used for commercial purpose. 
As conversations may have biased views, for example, specific political opinions from speakers, the transcripts and QA pairs will likely contain them. The content of the transcripts and summaries only reflect the views of the speakers, not the authors' point-of-views. We would like to remind our dataset users that there could have potential bias, toxicity, and subjective opinions in the selected conversations which may impact model training. Please view the content and data usage with discretion.

## Leaderboard

If you submit papers on QAConv, please consider sending a pull request to merge your results onto the leaderboard. By submitting, you acknowledge that your results are obtained without training on the val/test split and tuned on the val split not the test split. 

#### Chunk Mode Performance
* Zero-Shot

<!-- V1.1 -->
|                             |     EM    |   F1  |  FZ-R |
|-----------------------------|:---------:|:-----:|:-----:|
| Human Performance           |   79.99   | 89.87 | 92.33 |
| T5-3B (UnifiedQA)           |   59.93   | 73.07 | 78.89 |
| T5-Large (UnifiedQA)        |   58.81   | 71.67 | 77.72 |
| BERT-Large (SQuAD 2.0)      |   53.54   | 62.58 | 71.11 |
| T5-Base (UnifiedQA)         |   51.95   | 65.48 | 73.26  |
| RoBERTa-Large (SQuAD 2.0)   |   50.78   | 59.73 | 69.11 |
| RoBERTa-Base (SQuAD 2.0)    |   48.92   | 57.33 | 67.40 |
| T5-11B (UnifiedQA)          |   44.96   | 61.52 | 68.68 |
| DistilBERT-Base (SQuAD 2.0) |   40.04   | 46.90 | 59.62 |
| BERT-Base (SQuAD 2.0)       |   36.22   | 44.57 | 57.72 |

<!-- V1.0 -->
<!-- |                             |     EM    |   F1  |  FZ-R |
|-----------------------------|:---------:|:-----:|:-----:|
| Human Performance           |   79.99   | 89.87 | 92.33 |
| T5-3B (UnifiedQA)           |   66.77   | 76.98 | 81.77 |
| T5-Large (UnifiedQA)        |   64.83   | 75.73 | 80.59 |
| BERT-Large (SQuAD 2.0)      |   61.06   | 68.11 | 74.98 |
| RoBERTa-Large (SQuAD 2.0)   |   59.04   | 66.54 | 73.80 |
| T5-Base (UnifiedQA)         |   57.75   | 69.90 | 76.31 |
| RoBERTa-Base (SQuAD 2.0)    |   57.75   | 64.53 | 72.40 |
| GPT-3 (CoQA prompt)         |   53.72   | 67.45 | 72.94 |
| T5-11B (UnifiedQA)          |   51.13   | 66.19 | 71.68 |
| DistilBERT-Base (SQuAD 2.0) |   46.50   | 52.79 | 63.30 |
| BERT-Base (SQuAD 2.0)       |   42.73   | 49.67 | 60.99 | -->

* Fine-Tune

<!-- V1.1 -->
|                             |    EM    |   F1  |  FZ-R |
|-----------------------------|:--------:|:-----:|:-----:|
| RoBERTa-Large (SQuAD 2.0)   |   67.80  | 78.80 | 83.10 |
| T5-3B (UnifiedQA)           |   67.41  | 79.41 | 83.64 |
| T5-Large (UnifiedQA)        |   66.76  | 78.67 | 83.21 |
| T5-Base (UnifiedQA)         |   64.98  | 76.52 | 81.69 |
| BERT-Large (SQuAD 2.0)      |   64.93  | 76.65 | 81.27 |
| RoBERTa-Base (SQuAD 2.0)    |   63.64  | 75.53 | 80.38 |
| BERT-Base (SQuAD 2.0)       |   58.84  | 71.02 | 77.03 |
| DistilBERT-Base (SQuAD 2.0) |   57.28  | 68.88 | 75.39 | 

<!-- V1.0 -->
<!-- |                             |    EM    |   F1  |  FZ-R |
|-----------------------------|:--------:|:-----:|:-----:|
| T5-3B (UnifiedQA)           |   75.21  | 84.14 | 87.47 |
| T5-Large (UnifiedQA)        |   73.54  | 83.03 | 86.61 |
| RoBERTa-Large (SQuAD 2.0)   |   74.62  | 83.65 | 87.38 |
| BERT-Large (SQuAD 2.0)      |   72.85  | 81.65 | 85.59 |
| T5-Base (UnifiedQA)         |   71.20  | 80.92 | 84.74 |
| RoBERTa-Base (SQuAD 2.0)    |   71.14  | 80.36 | 84.52 |
| BERT-Base (SQuAD 2.0)       |   66.37  | 76.29 | 81.25 |
| DistilBERT-Base (SQuAD 2.0) |   63.69  | 73.94 | 79.30 | -->



#### Full Mode Performance
* Zero-Shot

<!-- v1.1 -->
|                                    |     EM    |   F1  |  FZ-R | 
|:----------------------------------:|:---------:|:-----:|:-----:|
| BM25 + T5-3B (UnifiedQA)           |   41.76   | 52.68 | 63.54 | 
| BM25 + T5-Large (UnifiedQA)        |   40.62   | 50.87 | 62.10 | 
| BM25 + BERT-Large (SQuAD 2.0)      |   37.09   | 43.44 | 57.21 | 
| BM25 + T5-Base (UnifiedQA)         |   36.47   | 47.11 | 59.22 |  
| BM25 + RoBERTa-Large (SQuAD 2.0)   |   35.54   | 41.50 | 55.79 | 
| BM25 + RoBERTa-Base (SQuAD 2.0)    |   34.61   | 40.74 | 55.37 |
| BM25 + DistilBERT-Base (SQuAD 2.0) |   29.36   | 34.09 | 50.35 | 
| BM25 + BERT-Base (SQuAD 2.0)       |   25.84   | 31.52 | 48.28 | 

<!-- v1.0 -->
<!-- |                                    |     EM    |   F1  |  FZ-R | 
|:----------------------------------:|:---------:|:-----:|:-----:|
| BM25 + T5-3B (UnifiedQA)           |   45.87   | 55.24 | 64.83 | 
| BM25 + T5-Large (UnifiedQA)        |   44.08   | 53.17 | 63.17 | 
| BM25 + BERT-Large (SQuAD 2.0)      |   42.19   | 47.59 | 59.41 | 
| BM25 + RoBERTa-Large (SQuAD 2.0)   |   41.39   | 46.75 | 58.67 | 
| BM25 + RoBERTa-Base (SQuAD 2.0)    |   41.11   | 46.15 | 58.35 |
| BM25 + T5-Base (UnifiedQA)         |   39.68   | 49.76 | 60.51 |  
| BM25 + DistilBERT-Base (SQuAD 2.0) |   33.66   | 38.19 | 52.28 | 
| BM25 + BERT-Base (SQuAD 2.0)       |   30.80   | 35.80 | 50.50 | 
 -->
 
 
* Fine-Tune
<!-- v1.1 -->
|                                    |    EM    |   F1  |  FZ-R | 
|:----------------------------------:|:--------:|:-----:|:-----:|
| BM25 + T5-3B (UnifiedQA)           |   45.86  | 55.17 | 65.76 | 
| BM25 + RoBERTa-Large (SQuAD 2.0)   |   45.59  | 54.42 | 65.23 | 
| BM25 + T5-Large (UnifiedQA)        |   45.34  | 54.49 | 65.47 | 
| BM25 + BERT-Large (SQuAD 2.0)      |   44.50  | 53.48 | 64.21 | 
| BM25 + T5-Base (UnifiedQA)         |   43.95  | 52.96 | 64.22 |  
| BM25 + RoBERTa-Base (SQuAD 2.0)    |   43.18  | 52.64 | 63.62 |
| BM25 + BERT-Base (SQuAD 2.0)       |   40.02  | 49.39 | 61.13 | 
| BM25 + DistilBERT-Base (SQuAD 2.0) |   39.39  | 48.38 | 60.46 |

<!-- V1.0 -->
<!-- |                                    |    EM    |   F1  |  FZ-R | 
|:----------------------------------:|:--------:|:-----:|:-----:|
| BM25 + T5-3B (UnifiedQA)           |   51.44  | 58.80 | 68.10 | 
| BM25 + RoBERTa-Large (SQuAD 2.0)   |   50.24  | 57.80 | 67.57 | 
| BM25 + T5-Large (UnifiedQA)        |   49.64  | 57.58 | 67.36 | 
| BM25 + BERT-Large (SQuAD 2.0)      |   48.99  | 56.60 | 66.40 | 
| BM25 + RoBERTa-Base (SQuAD 2.0)    |   48.42  | 56.24 | 66.08 |
| BM25 + T5-Base (UnifiedQA)         |   48.56  | 56.38 | 66.01 |  
| BM25 + BERT-Base (SQuAD 2.0)       |   44.62  | 52.91 | 63.50 | 
| BM25 + DistilBERT-Base (SQuAD 2.0) |   43.51  | 52.12 | 62.63 |  -->

## Report
Please create an issue or send an email to wu.jason@salesforce.com for any questions/bugs/etc.
