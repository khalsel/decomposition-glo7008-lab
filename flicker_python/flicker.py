import time
import json
import argparse
import os


class Flicker:
    def __init__(self, file_name: str = None, verbose: bool = False):
        self.file_name = file_name if file_name is not None else "context_{}.json".format(round(time.time()*1000))
        self.verbose = verbose
        self.use_cases = list()

    def main_loop(self):
        while True:
            if len(self.use_cases)!=0:
                print("LABEL\t\t\tSTART\t\t\tSTOP\t\t\t")
                for use_case in self.use_cases:
                    print("{LABEL}\t\t\t{START}\t\t\t{STOP}\t\t\t".format(**use_case))
            print('Enter <Label> to start recording current context (type "Exit" to quit).')
            label = str(input())
            if label=="Exit":
                break
            start_time = round(time.time()*1000)
            print("Enter STOP to terminate the recording of the current context.")
            while str(input())!= "STOP":
                print("Enter STOP to terminate the recording of the current context.")
            stop_time = round(time.time() * 1000)
            self.use_cases.append({"START": start_time, "LABEL": label, "STOP": stop_time})
        self.save()

    def save(self):
        os.makedirs(os.path.join(os.path.curdir, "output"), exist_ok=True)
        with open(os.path.join(os.path.curdir, "output", self.file_name), "w") as f:
            data = [{"offset": 0, "session": self.use_cases, "appserver": ""}]
            json.dump(data, f)
            if self.verbose:
                print(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flicker Python port')
    parser.add_argument('-a', type=str,
                        help='json file name (example context.json)')
    parser.add_argument('-v', action="store_true",
                        help='print the final results')
    args = parser.parse_args()
    if args.a is not None and not args.a.endswith(".json"):
        parser.error("-a requires a json filename")
    flicker = Flicker(args.a, args.v)
    flicker.main_loop()

