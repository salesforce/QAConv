# QAConv

## Overview
This repository maintains the QAConv dataset, a question answering dataset on informative conversations.

Paper: 
Authors: Chien-Sheng (Jason) Wu, Andrea Madotto, Wenhao Liu, and Caiming Xiong

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

## Code

### Running baselines in QAConv paper

#### Retriever
```console
❱❱❱ cd retriever
❱❱❱ ./run_retriver.sh
```

#### Free-form

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
❱❱❱ ./run_eval.sh 0 ../../../data/nmt/ ../../../data/ output/qaconv-allenai/unifiedqa-t5-base/ output/qaconv-allenai/unifiedqa-t5-base/ output/qaconv-allenai/unifiedqa-t5-base/prediction/
```

* Evaluation
```console
❱❱❱ python evaluate.py data/tst.json prediction/unifiedqa-t5-base-zeroshot.json
❱❱❱ python evaluate.py data/tst.json prediction/unifiedqa-t5-base.json
```

#### Span-base


## Report
Please create an issue or send email to wu.jason@salesforce.com to report any questions/bugs/etc.
