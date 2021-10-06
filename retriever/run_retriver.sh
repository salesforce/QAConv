data=$1 # val or tst

python chunk2tsv.py

## bm25
python bm25.py -d $data -o output_retriever_rank_bm25
python evaluate_recall.py -d $data -o output_retriever_rank_bm25
python convert_txt.py -d $data -o output_retriever_rank_bm25

## dpr-wiki

./run_dpr.sh $data

if [ ${data} = "tst" ] 
then
    python dpr.py -d $data -o output_retriever_rank_dpr-wiki -r DPR/qaconv_test_dpr_results.json
elif [ ${data} = "val" ] 
then
    python dpr.py -d $data -o output_retriever_rank_dpr-wiki -r DPR/qaconv_val_dpr_results.json
else
    echo "Please indicate val or tst..."
fi

python evaluate_recall.py -d $data -o output_retriever_rank_dpr-wiki
python convert_txt.py -d $data -o output_retriever_rank_dpr-wiki