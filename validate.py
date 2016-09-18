
import sys
from jsonschema import validate
import yaml



def main(argv):
    schemafile = "schema.yml"
    schema = None
    schemadata = None
    with open(schemafile, "r") as f:
        schemadata = yaml.load(f)
    data = None
    with open(argv[1], "r") as f:
        data = yaml.load(f)
    # get all yml files from protocols
    # validate with
    validate(data, schemadata)



if __name__ == '__main__':
    main(sys.argv)
