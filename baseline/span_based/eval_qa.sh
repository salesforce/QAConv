CUDA_VISIBLE_DEVICES=0 python run_qa.py \
  --model_name_or_path distilbert-base-uncased-distilled-squad \
  --train_file data/QA4KRC_TRAIN.json \
  --validation_file data/QA4KRC_VALID.json \
  --test_file data/QA4KRC_TEST.json \
  --max_seq_length 512 \
  --output_dir tmp/debug_squad/ \
  --cache_dir cache\
  --do_predict \
  # --do_eval \
  # --doc_stride 128 \