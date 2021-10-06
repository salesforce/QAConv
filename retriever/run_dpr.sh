#!/bin/sh

data=$1

cd DPR

## Download saved model checkpoints
# python data/download_data.py --resource checkpoint.retriever.single-adv-hn.nq.bert-base-encoder

## Modify config path
# > modify `DPR/conf/ctx_sources/default_sources.yaml` qaconv file path
# > modify `DPR/conf/datasets/retriever_default.yaml` qaconv_test path and qaconv_val path

python generaste_dense_embeddings.py model_file=~/QAConv/retriever/DPR/dpr/downloads/checkpoint/retriever/single-adv-hn/nq/bert-base-encoder.cp ctx_src=qaconv shard_id=0 num_shards=1 out_file=../../../article_segment

if [ ${data} = "tst" ] 
then
    echo "1"${data}
    python dense_retriever.py model_file=$(pwd)/dpr/downloads/checkpoint/retriever/single-adv-hn/nq/bert-base-encoder.cp qa_dataset=qaconv_test ctx_datatsets=[qaconv] encoded_ctx_files=[\"$(pwd)/article_segment_0\"] out_file=../../../qaconv_test_dpr_results.json

elif [ ${data} = "val" ] 
then
    echo "2"${data}
    python dense_retriever.py model_file=$(pwd)/dpr/downloads/checkpoint/retriever/single-adv-hn/nq/bert-base-encoder.cp qa_dataset=qaconv_val ctx_datatsets=[qaconv] encoded_ctx_files=[\"$(pwd)/article_segment_0\"] out_file=../../../qaconv_val_dpr_results.json

else
    echo "Please indicate val or tst..."
fi

cd ..