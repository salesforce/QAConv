import json
from tqdm import tqdm
from utils import get_chunks_by_qa

article_seg_json = json.load(open("../data/article_segment.json"))

output_tsv = []
for idx, (article_seg_key, article_seg) in enumerate(article_seg_json.items()):
    utters = ["{}: {}".format(seg["speaker"], seg["text"]).replace("\t", " ").replace("\n", " ") for seg in article_seg["seg_dialog"]]
    output_tsv.append("{}\t{}\t{}".format(idx, " ".join(utters), article_seg_key))

with open("../data/article_segment.tsv", "w") as fout:
    fout.write("\n".join(output_tsv))
