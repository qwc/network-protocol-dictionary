import sys
from jsonschema import validate
import yaml
import argparse
import glob


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", help="Validate all protocols.", action="store_true")
    parser.add_argument("-f", help="Validate file.", default=None)
    parser.add_argument("-s", help="Use schema file.", default="schema.yml")
    parser.add_argument("-v", help="Verbosity...", action="store_true")
    args = parser.parse_args()
    schemafile = args.s
    schemadata = None
    with open(schemafile, "r") as f:
        schemadata = yaml.load(f)
    if args.all:
        # search for files and validate them.
        print("Validating all files in protocols/osi*")
        list = glob.glob("protocols/osi*/*.yml", recursive=True)
        for file in list:
            print("Validating file: " + file)
            validateFile(file, schemadata, True if args.v else False)
        pass
    elif args.f is not None:
        validateFile(args.f, schemadata, True if args.v else False)
        pass


def validateFile(file, schema, verbose=False):
    data = None
    with open(file, "r") as f:
        data = yaml.load(f)
    try:
        validate(data, schema)
        print(file + " is valid.")
    except:
        print("Failed to validate: " + file)
        if verbose:
            raise


if __name__ == '__main__':
    main(sys.argv)
