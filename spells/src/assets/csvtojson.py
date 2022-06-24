import argparse
from os import error
import json5 as json
import io


def main(args):
    with io.open(args.csvfile,mode="r",encoding="utf-8") as f:
        lines = f.readlines()
    entete = list(map(lambda x: x.strip().replace(" ","_"), lines[0].split(args.separator)))
    entete[0] = entete[0][1:]
    data = lines[1:]
    output_dict = []
    for d in data:
        values =  list(map(lambda x: x.strip(), d.split(args.separator)))
        if len(values) != len(entete):
            print(values)
            raise("Oupsi doupsi pb in the data file.")
        obj = {}
        for i in range(len(entete)):
            obj[entete[i]] = values[i]
        output_dict.append(obj)
    with open(args.outputname,"w", encoding="utf-8") as fp:
        json.dump(output_dict, fp, indent=4, quote_keys=True, trailing_commas=False,ensure_ascii=False)


parser = argparse.ArgumentParser(description="Convert csv to JSON.")
parser.add_argument("csvfile",help="csv file you want to convert")
parser.add_argument("outputname", help="Filename of the output")
parser.add_argument("--separator","-s",help="separator",default=";")

args = parser.parse_args()

main(args)