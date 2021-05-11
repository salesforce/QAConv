# QAConv

## Overview
This repository maintains the QAConv dataset, a question answering dataset on informative conversations including business emails, panel discussions, and work channels.

Paper: [QAConv: Question Answering on Informative Conversations]()

Authors: Chien-Sheng (Jason) Wu, Andrea Madotto, Wenhao Liu, and Caiming Xiong

## Leaderboard

If you submit papers on QAConv, please consider sending a pull request to merge your results onto the leaderboard. By submitting, you acknowledge that your results are obtained without training on the val/test split and tuned on the val split not the test split. 

### Chunk Mode Performance
##### Zero-Shot
|                             |     EM    |   F1  |  FZ-R |
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
| BERT-Base (SQuAD 2.0)       |   42.73   | 49.67 | 60.99 |

##### Fine-Tune
|                             |    EM    |   F1  |  FZ-R |
|-----------------------------|:--------:|:-----:|:-----:|
| T5-3B (UnifiedQA)           |   75.21  | 84.14 | 87.47 |
| T5-Large (UnifiedQA)        |   73.54  | 83.03 | 86.61 |
| RoBERTa-Large (SQuAD 2.0)   |   74.62  | 83.65 | 87.38 |
| BERT-Large (SQuAD 2.0)      |   72.85  | 81.65 | 85.59 |
| T5-Base (UnifiedQA)         |   71.20  | 80.92 | 84.74 |
| RoBERTa-Base (SQuAD 2.0)    |   71.14  | 80.36 | 84.52 |
| BERT-Base (SQuAD 2.0)       |   66.37  | 76.29 | 81.25 |
| DistilBERT-Base (SQuAD 2.0) |   63.69  | 73.94 | 79.30 |

### Full Mode Performance
##### Zero-Shot
|                                    |     EM    |   F1  |  FZ-R | 
|:----------------------------------:|:---------:|:-----:|:-----:|
| BM25 + T5-3B (UnifiedQA)           |   45.87   | 55.24 | 64.83 | 
| BM25 + T5-Large (UnifiedQA)        |   44.08   | 53.17 | 63.17 | 
| BM25 + BERT-Large (SQuAD 2.0)      |   42.19   | 47.59 | 59.41 | 
| BM25 + RoBERTa-Large (SQuAD 2.0)   |   41.39   | 46.75 | 58.67 | 
| BM25 + RoBERTa-Base (SQuAD 2.0)    |   41.11   | 46.15 | 58.35 |
| BM25 + T5-Base (UnifiedQA)         |   39.68   | 49.76 | 60.51 |  
| BM25 + DistilBERT-Base (SQuAD 2.0) |   33.66   | 38.19 | 52.28 | 
| BM25 + BERT-Base (SQuAD 2.0)       |   30.80   | 35.80 | 50.50 | 

##### Fine-Tune
|                                    |    EM    |   F1  |  FZ-R | 
|:----------------------------------:|:--------:|:-----:|:-----:|
| BM25 + T5-3B (UnifiedQA)           |   51.44  | 58.80 | 68.10 | 
| BM25 + RoBERTa-Large (SQuAD 2.0)   |   50.24  | 57.80 | 67.57 | 
| BM25 + T5-Large (UnifiedQA)        |   49.64  | 57.58 | 67.36 | 
| BM25 + BERT-Large (SQuAD 2.0)      |   48.99  | 56.60 | 66.40 | 
| BM25 + RoBERTa-Base (SQuAD 2.0)    |   48.42  | 56.24 | 66.08 |
| BM25 + T5-Base (UnifiedQA)         |   48.56  | 56.38 | 66.01 |  
| BM25 + BERT-Base (SQuAD 2.0)       |   44.62  | 52.91 | 63.50 | 
| BM25 + DistilBERT-Base (SQuAD 2.0) |   43.51  | 52.12 | 62.63 | 


## Dataset
The format of the data is as follow:
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
      {
        "id": "newsidal-NPR-170-136",
        "speaker": "NEAL CONAN, HOST",
        "text": "Let's see if we can get some callers on the line, 800-989-8255. Florida primary voters, have you made up your minds yet? We'll start with Marie(ph), and Marie's on with us from Fort Lauderdale."
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
      "id": "newsidal-NPR-170-2",
      "speaker": "NEAL CONAN, HOST",
      "text": "...edition of the Political Junkie."
    },
    ...
  ]
}
```

## Running Baselines

### Retriever
```console
❱❱❱ cd retriever
❱❱❱ ./run_retriver.sh
```

### Free-form

* Preprocess
```console
❱❱❱ cd data
❱❱❱ python convert_txt.py
```

* Zero-shot
```console
❱❱❱ cd baseline/free_form/
❱❱❱ ./run_zs.sh
```

* Training
```console
❱❱❱ cd baseline/free_form/finetuning/
❱❱❱ ./run_finetune.sh 0,1 2 allenai/unifiedqa-t5-base 8
```

* Inference
```console
❱❱❱ cd baseline/free_form/finetuning/
❱❱❱ ./run_eval.sh 0 ../../../data/nmt/ ../../../data/ output/qaconv-allenai/unifiedqa-t5-base/ unifiedqa-t5-base output/qaconv-allenai/unifiedqa-t5-base/prediction/
❱❱❱ ./run_eval.sh 0 ../../../data/nmt-bm25/ ../../../data/ output/qaconv-allenai/unifiedqa-t5-base/ unifiedqa-t5-base-bm25 output/qaconv-allenai/unifiedqa-t5-base/prediction-bm25/
```

* Evaluation
```console
❱❱❱ python evaluate.py data/tst.json prediction/unifiedqa-t5-base-zeroshot.json
❱❱❱ python evaluate.py data/tst.json prediction/unifiedqa-t5-base.json
❱❱❱ python evaluate.py data/tst.json prediction/unifiedqa-t5-base-bm25.json
```

### Span-base


## Report
Please create an issue or send email to wu.jason@salesforce.com to report any questions/bugs/etc.
