#!/usr/bin/python
import sys
import os
from pymarkovchain import MarkovChain

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--repo", type=str, default="", help="Create an issue on the named repository (must already exist), instead of just printing it.")
parser.add_argument("--token", type=str, default="", help="Your github API token. If left blank look in token.txt")


def main():
    args = parser.parse_args()
    dirname=os.path.split(__file__)[0]
    filename=os.path.join(dirname,"phil.txt")
    title_filename=os.path.join(dirname,"phil_titles.txt")
    dbname1 = "database.pkl"
    dbname2 = "database_title.pkl"
    new_db = not os.path.exists(dbname1)
    body_maker = MarkovChain(dbname1)
    title_maker = MarkovChain(dbname2)
    if new_db:
        title_maker.generateDatabase(open(title_filename).read())
        title_maker.dumpdb()
        body_maker.generateDatabase(open(filename).read())
        body_maker.dumpdb()

    name = title_maker.generateString()
    body = '  '.join([body_maker.generateString()+'.' for i in xrange(3)])

    if args.repo:
        if args.token:
            token = args.token
        else:
            token_filename = os.path.join(dirname, "token.txt")
            if not os.path.exists(token_filename):
                sys.stderr.write("Please either specify --token=XXX on the command line or put a github API token in token.txt\n")
                sys.stderr.write("You can generate a token here: https://github.com/settings/tokens\n")
                sys.exit(1)
            token = open(token_filename).read().strip()

        import github
        gh=github.Github(token)
        user=gh.get_user()
        repo=user.get_repo(args.repo)
        issue = repo.create_issue(title=name, body=body)
        print issue.html_url
    else:
        print 
        print name
        print "-"*len(name)
        print body


if __name__ == "__main__":
    main()

