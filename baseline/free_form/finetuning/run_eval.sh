gpu=$1 # 0
DATA_TXT_DIR=$2 # ../../../data/nmt/
DATA_RAW_DIR=$3 # ../../../data/tst.json
CHECKPOINT=$4 # output/qaconv-allenai/unifiedqa-t5-base/
OUTPUT_NAME=$5 # unifiedqa-t5-base
OUT_DIR=$6 # output/qaconv-allenai/unifiedqa-t5-base/prediction/

mkdir ${OUT_DIR}

CUDA_VISIBLE_DEVICES=${gpu} python run_eval.py ${CHECKPOINT} ${DATA_TXT_DIR}/test.source ${OUT_DIR}/test-pred.txt \
    --reference_path ${DATA_TXT_DIR}/test.target \
    --score_path ${OUT_DIR}/test-rouge.json \
    --task qa \
    --device cuda \
    --bs 2

python convert_pred_txt2json.py -q ${DATA_RAW_DIR} \
    -p ${OUT_DIR}/test-pred.txt \
    -o ${OUTPUT_NAME}
