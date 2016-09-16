import Rx
import sys


def validate(argv):
    rx = Rx.Factory(register_core_types=True)
    schemafile = "schema.yaml"
    schema = None
    data = None
    with open(schemafile, "r") as f:
        data = f.read()
    schema = rx.make_schema(data)
    # get all yml files from protocols
    # validate with
    schema.validate(data)


if __name__ == '__main__':
    validate(sys.argv)
