GPU=$1 # 0,1
GPU_NB=$2 # 2
MODEL=$3 # allenai/unifiedqa-t5-base
BSZ=$4 # 8

RUN=qaconv-${MODEL}
CUDA_VISIBLE_DEVICES=${GPU} python3 -m torch.distributed.launch --nproc_per_node=${GPU_NB} --master_port=3000 finetune_trainer.py \
    --learning_rate=3e-5 \
    --do_train --do_eval --do_predict \
    --evaluation_strategy "steps" \
    --predict_with_generate \
    --num_train_epochs 10 \
    --data_dir ../../../data/ \
    --model_name_or_path ${MODEL} \
    --output_dir ./output/${RUN} \
    --per_device_train_batch_size ${BSZ} \
    --per_device_eval_batch_size ${BSZ} \
    --overwrite_output_dir \
    --run_name $RUN \
    --save_steps 5000 --logging_steps 5000
