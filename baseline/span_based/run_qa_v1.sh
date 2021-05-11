# CUDA_VISIBLE_DEVICES=3 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10001  run_qa.py \
#   --model_name_or_path distilbert-base-uncased-distilled-squad \
#   --output_dir save_v1/distilbert \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_1.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_1.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_1.json \
#   --do_train \
#   --do_eval \
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
#   --save_total_limit 1 

CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10003  run_qa.py \
  --model_name_or_path bert-large-uncased-whole-word-masking-finetuned-squad \
  --output_dir save_v1/bert-large-largebsz \
  --train_file data/QAConv_FINAL/QA4KRC_TRAIN_1.json \
  --validation_file data/QAConv_FINAL/QA4KRC_VALID_1.json \
  --test_file data/QAConv_FINAL/QA4KRC_TEST_1.json \
  --do_train \
  --do_eval \
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


# CUDA_VISIBLE_DEVICES=5 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10002  run_qa.py \
#   --model_name_or_path csarron/bert-base-uncased-squad-v1 \
#   --output_dir save_v1/bert-base \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_1.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_1.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_1.json \
#   --do_train \
#   --do_eval \
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
#   --save_total_limit 1 


# CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10004  run_qa.py \
#   --model_name_or_path csarron/roberta-base-squad-v1 \
#   --output_dir save_v1/roberta-base \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_1.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_1.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_1.json \
#   --do_train \
#   --do_eval \
#   --per_device_train_batch_size 6 \
#   --per_device_eval_batch_size 6 \
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
  
# CUDA_VISIBLE_DEVICES=9 python -m torch.distributed.launch --nproc_per_node=1 --master_port=10005  run_qa.py \
#   --model_name_or_path csarron/roberta-large-squad-v1 \
#   --output_dir save_v1/roberta-large-largebsz \
#   --train_file data/QAConv_FINAL/QA4KRC_TRAIN_1.json \
#   --validation_file data/QAConv_FINAL/QA4KRC_VALID_1.json \
#   --test_file data/QAConv_FINAL/QA4KRC_TEST_1.json \
#   --do_train \
#   --do_eval \
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