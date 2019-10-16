import argparse

#create our own parser function and then just call it when we need it
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--format',default='json', choices=['json','csv'],type=str.lower,  help='file export type')
    parser.add_argument('--path', help='path to export file')
    return parser


#wiring all together
def main():
    import sys
    from hr import export
    from hr import users as u
    args = create_parser().parse_args()
    users = u.fetch_users()

    #check the path if file exists to save it
    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout

    if args.format =='json':
        export.to_json_file(file, users)
    else:
        export.to_csv_file(file, users)



