"""
 * Copyright (c) 2021, salesforce.com, inc.
 * All rights reserved.
 * SPDX-License-Identifier: BSD-3-Clause
 * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

"""

import json
import argparse

def convert(pred_txt_file, ques_json_file, exp_name):
    pred = open(pred_txt_file, "r").readlines()
    ques = json.load(open(ques_json_file, "r"))

    assert len (ques) == len(pred)
    
    out = {}
    for qi, qa in enumerate(ques):
        out[qa["id"]] = pred[qi].strip()
    
    with open("../../../prediction/{}.json".format(exp_name), "w") as fout:
        json.dump(out, fout, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run evaluation...')
    parser.add_argument('-q',  '--ques_json_file', type=str, required=True,
                    help='QA data source')
    parser.add_argument('-p', '--pred_txt_file', type=str, required=True,
                    help='prediction file')
    parser.add_argument('-o', '--output_name', type=str, required=True,
                    help='output name for the json prediction file, e.g., t5-base-10epoch')
    args = parser.parse_args()

    convert(args.pred_txt_file, args.ques_json_file, args.output_name)
