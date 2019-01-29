#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import json
import os

CSV_DIR = "extracted_csvs"

HEADER = [
    "Title",
    "product_id",
    "ISSN print",
    "ISSN electronic",
    "Imprint",
    "Primary Language",
    "Open Access",
    "Comment",
    "License",
    "standard workflow July 18",
    "Production Editor",
    "Netherlands",
    "MPG",
    "UK",
    "Austria",
    "Finland",
    "Sweden",
    "Hungary",
    "Poland"
]

def main():
    
    participants = {}
    for file_name in os.listdir(CSV_DIR):
        path = os.path.join(CSV_DIR, file_name)
        if os.path.isfile(path):
            root, ext = os.path.splitext(file_name)
            if ext == ".csv":
                participants[root] = path
    
    csv_content = {}
    for sca_member, path in participants.items():
        csv_content[sca_member] = {}
        with open(path, encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for line in reader:
                product_id = line["product_id"]
                if not product_id:
                    msg = 'ERROR: Could not process journal "{}" in {} file: No product_id!'
                    msg = msg.format(line["Title"], sca_member)
                    print(msg)
                csv_content[sca_member][product_id] = line
                
    all_journals = []
    
    for sca_member in csv_content.keys():
        other_members = list(csv_content.keys())
        other_members.remove(sca_member)
        for product_id in list(csv_content[sca_member].keys()):
            journal_data = csv_content[sca_member][product_id]
            journal_data[sca_member] = "TRUE"
            title = csv_content[sca_member][product_id]["Title"]
            del csv_content[sca_member][product_id]
            for other_member in other_members:
                if product_id in csv_content[other_member]:
                    other_title = csv_content[other_member][product_id]["Title"]
                    if title != other_title:
                        msg = ('WARNING: Title mismatch for journal {} between {} and {} list: ' +
                               '"{}" vs "{}"')
                        msg = msg.format(product_id, sca_member, other_member, title, other_title)
                        print(msg)
                    del csv_content[other_member][product_id]
                    journal_data[other_member] = "TRUE"
                else:
                    journal_data[other_member] = "FALSE"
            all_journals.append(journal_data)

    with open("out.csv", "w") as out_file:
        writer = csv.DictWriter(out_file, fieldnames=HEADER, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_journals)
    
    
if __name__ == '__main__':
    main()
