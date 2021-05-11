# CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10001  run_qa.py \
#   --model_name_or_path twmkn9/distilbert-base-uncased-squad2 \
#   --output_dir save_v2/distilbert \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_2.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_2.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_2.json \
#   --do_train \
#   --do_eval \
#   --version_2_with_negative \
#   --per_device_train_batch_size 8 \
#   --per_device_eval_batch_size 8 \
#   --learning_rate 3e-5 \
#   --logging_steps 50 \
#   --num_train_epochs 5 \
#   --max_seq_length 512 \
#   --warmup_steps 1000 \
#   --weight_decay 0.01 \
#   --cache_dir cache/ \
#   --evaluation_strategy epoch \
#   --sharded_ddp simple \
#   --save_total_limit 1 &

# CUDA_VISIBLE_DEVICES=2 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10002  run_qa.py \
#   --model_name_or_path deepset/roberta-base-squad2 \
#   --output_dir save_v2/roberta-base \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_2.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_2.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_2.json \
#   --do_train \
#   --do_eval \
#   --version_2_with_negative \
#   --per_device_train_batch_size 8 \
#   --per_device_eval_batch_size 8 \
#   --learning_rate 3e-5 \
#   --logging_steps 50 \
#   --num_train_epochs 5 \
#   --max_seq_length 512 \
#   --warmup_steps 1000 \
#   --weight_decay 0.01 \
#   --cache_dir cache/ \
#   --evaluation_strategy epoch \
#   --sharded_ddp simple \
#   --save_total_limit 1 &

# CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch --nproc_per_node=1 --master_port=100111  run_qa.py \
#   --model_name_or_path deepset/roberta-large-squad2 \
#   --output_dir save_v2/roberta-large-largebsz \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_2.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_2.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_2.json \
#   --do_train \
#   --do_eval \
#   --version_2_with_negative \
#   --per_device_train_batch_size 1 \
#   --per_device_eval_batch_size 4 \
#   --gradient_accumulation_steps 32 \
#   --learning_rate 3e-5 \
#   --logging_steps 50 \
#   --num_train_epochs 5 \
#   --max_seq_length 512 \
#   --warmup_steps 1000 \
#   --weight_decay 0.01 \
#   --cache_dir cache/ \
#   --evaluation_strategy epoch \
#   --sharded_ddp simple \
#   --save_total_limit 1 


# CUDA_VISIBLE_DEVICES=8 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10004  run_qa.py \
#   --model_name_or_path deepset/bert-base-cased-squad2 \
#   --output_dir save_v2/bert-base \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_2.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_2.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_2.json \
#   --do_train \
#   --do_eval \
#   --version_2_with_negative \
#   --per_device_train_batch_size 8 \
#   --per_device_eval_batch_size 8 \
#   --learning_rate 3e-5 \
#   --logging_steps 50 \
#   --num_train_epochs 5 \
#   --max_seq_length 512 \
#   --warmup_steps 1000 \
#   --weight_decay 0.01 \
#   --cache_dir cache/ \
#   --evaluation_strategy epoch \
#   --sharded_ddp simple \
#   --save_total_limit 1 &

CUDA_VISIBLE_DEVICES=9 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10005  run_qa.py \
  --model_name_or_path deepset/bert-large-uncased-whole-word-masking-squad2 \
  --output_dir save_v2/bert-large-largebsz \
  --train_file data/QAConv_FINAL/QA4KRC_TRAIN_2.json \
  --validation_file data/QAConv_FINAL/QA4KRC_VALID_2.json \
  --test_file data/QAConv_FINAL/QA4KRC_TEST_2.json \
  --do_train \
  --do_eval \
  --version_2_with_negative \
  --per_device_train_batch_size 1 \
  --per_device_eval_batch_size 4 \
  --gradient_accumulation_steps 32 \
  --learning_rate 3e-5 \
  --logging_steps 50 \
  --num_train_epochs 5 \
  --max_seq_length 512 \
  --warmup_steps 1000 \
  --weight_decay 0.01 \
  --cache_dir cache/ \
  --evaluation_strategy epoch \
  --sharded_ddp simple \
  --save_total_limit 1 



CUDA_VISIBLE_DEVICES=1 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10015  run_qa.py \
  --model_name_or_path ahotrod/albert_xxlargev1_squad2_512 \
  --output_dir save_v2/albert_xxl \
  --train_file data/QAConv_FINAL/QA4KRC_TRAIN_2.json \
  --validation_file data/QAConv_FINAL/QA4KRC_VALID_2.json \
  --test_file data/QAConv_FINAL/QA4KRC_TEST_2.json \
  --do_train \
  --do_eval \
  --version_2_with_negative \
  --per_device_train_batch_size 1 \
  --per_device_eval_batch_size 4 \
  --gradient_accumulation_steps 32 \
  --learning_rate 3e-5 \
  --logging_steps 50 \
  --num_train_epochs 5 \
  --max_seq_length 512 \
  --warmup_steps 1000 \
  --weight_decay 0.01 \
  --cache_dir cache/ \
  --evaluation_strategy epoch \
  --sharded_ddp simple \
  --save_total_limit 1 

 