data=$1

python bm25.py -d $data
python evaluate_recall.py -d $data
python convert_txt.py -d $data
