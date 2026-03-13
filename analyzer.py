import argparse
import csv
import json
import os
import re
import sys
from collections import Counter

DEFAULT_LEVELS=["DEBUG","INFO","WARNING","ERROR","CRITICAL","NOTICE"]

def parse_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("logfile",nargs="+")
    parser.add_argument("--levels",nargs="+",default=DEFAULT_LEVELS)
    parser.add_argument("--json",dest="json_output")
    parser.add_argument("--csv",dest="csv_output")
    parser.add_argument("--sort",choices=["name","count"],default="name")
    parser.add_argument("--descending",action="store_true")
    return parser.parse_args()

def normalize_levels(levels):
    return [l.upper() for l in levels]

def extract_level(line,valid):
    line=line.strip()
    if not line:
        return None
    patterns=[
        r"^\[?(DEBUG|INFO|WARNING|ERROR|CRITICAL|NOTICE)\]?\b",
        r"^\S+\s+\S+\s+\[?(DEBUG|INFO|WARNING|ERROR|CRITICAL|NOTICE)\]?\b"
    ]
    for p in patterns:
        m=re.search(p,line,re.IGNORECASE)
        if m:
            level=m.group(1).upper()
            if level in valid:
                return level
    first=line.split(maxsplit=1)[0].strip("[]").upper()
    if first in valid:
        return first
    return None

def analyze_log(file_path,levels):
    valid=set(normalize_levels(levels))
    counts=Counter()
    total=0
    matched=0
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
            total+=1
            level=extract_level(line,valid)
            if level:
                counts[level]+=1
                matched+=1
    return {"file":file_path,"total_lines":total,"matched_lines":matched,"counts":dict(counts)}

def sort_counts(counts,sort_by,descending):
    items=list(counts.items())
    if sort_by=="count":
        items.sort(key=lambda x:(x[1],x[0]),reverse=descending)
    else:
        items.sort(key=lambda x:x[0],reverse=descending)
    return items

def print_result(result,sort_by,descending):
    print("\nFile:",result["file"])
    print("Log Analysis Results")
    print("--------------------")
    print("Total lines:",result["total_lines"])
    print("Matched log lines:",result["matched_lines"])
    for level,count in sort_counts(result["counts"],sort_by,descending):
        print(f"{level}: {count}")

def export_json(path,results):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(results,f,indent=4)

def export_csv(path,results):
    levels=set()
    for r in results:
        levels.update(r["counts"].keys())
    levels=sorted(levels)
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["file","total_lines","matched_lines"]+levels)
        for r in results:
            row=[r["file"],r["total_lines"],r["matched_lines"]]
            row.extend(r["counts"].get(l,0) for l in levels)
            w.writerow(row)

def main():
    args=parse_arguments()
    files=[f for f in args.logfile if os.path.isfile(f)]
    results=[]
    for f in files:
        results.append(analyze_log(f,args.levels))
    for r in results:
        print_result(r,args.sort,args.descending)
    if args.json_output:
        export_json(args.json_output,results)
    if args.csv_output:
        export_csv(args.csv_output,results)

if __name__=="__main__":
    main()
