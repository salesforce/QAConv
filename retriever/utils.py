
def get_chunks_by_qa(qa_pair, article_seg_json):
    chunks = {}
    for key, value in article_seg_json.items():
        if "slack" in qa_pair["article_segment_id"]:
            ids = set(["-".join(sent["id"].split("-")[:2]) for sent in value["seg_dialog"]])
            for article_full_id in qa_pair["article_full_id"]:
                if "-".join(article_full_id.split("-")[:2]) in ids:
                    chunks[key] = value
        else:
            # print(value)
            ids = set([sent["id"].rsplit("-", 1)[0] for sent in value["seg_dialog"]])
            for article_full_id in qa_pair["article_full_id"]:
                if article_full_id in ids:
                    chunks[key] = value
    return chunks