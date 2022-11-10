import time
import json
import argparse


class Flicker:
    def __init__(self, file_name=None):
        self.file_name = file_name if file_name is not None else "context_{}.json".format(round(time.time()*1000))
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
            start_time = str(round(time.time()*1000))
            print("Enter STOP to terminate the recording of the current context.")
            while str(input())!= "STOP":
                print("Enter STOP to terminate the recording of the current context.")
            stop_time = str(round(time.time() * 1000))
            self.use_cases.append({"LABEL": label, "START": start_time, "STOP": stop_time})
        self.save()

    def save(self):
        with open(self.file_name, "w") as f:
            data = [{"offset": 0, "session": self.use_cases, "appserver": ""}]
            json.dump(data, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flicker Python port')
    parser.add_argument('-a', type=str,
                        help='json file name (example context.json)')
    args = parser.parse_args()
    if args.a is not None and not args.a.endswith(".json"):
        parser.error("-a requires a json filename")
    flicker = Flicker(args.a)
    flicker.main_loop()

