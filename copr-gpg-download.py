#!/usr/bin/python3

from os import path, remove
from argparse import RawTextHelpFormatter, ArgumentParser
from requests import get
from copr.v3 import Client
from copr.v3.pagination import next_page


def get_gpg(url):

    response = get(url)
    return response.text


def gpg_out(isolate_file, file_name, response):
    if isolate_file:
        with open(file_name, "w") as file:
            file.write(response)

        print("Saved {0}".format(file_name))
    elif output_file:
        output_file.write(response)
    else:
        print(response)


def main():
    projects = cli.project_proxy.get_list(ownername=None, pagination={"limit": 100})
    while projects:
        if not projects:
            break

        for project in projects:
            file_name = args.path + "copr-{0}-{1}.gpg".format(project.ownername, project.name)
            url = be_url_tmpl.format(**{'username': project.ownername,
                                        'project_name': project.name})
            response = get_gpg(url)
            if "404 Not Found" in response:
                not_found(file_name)
            else:
                gpg_out(args.isolate_files, file_name, response)

        projects = next_page(projects)


def not_found(file_name):
    if path.isfile(file_name):
        print("Deleting {0} - project key doesn't exist.".format(file_name))
        remove(file_name)
    else:
        print("Skipping {} - already deleted.".format(file_name))


parser = ArgumentParser(description='Download GPG keys for COPR projects.',
                        formatter_class=RawTextHelpFormatter)
parser.add_argument('-f', '--file', action='store',
                    help='store keys to a file instead of printing to stdout')
parser.add_argument('--feurl', action='store', default='http://copr.fedorainfracloud.org/',
                    help='use this url as baseurl to frontend instead of\nhttp://copr.fedorainfracloud.org/')
parser.add_argument('--beurl', action='store', default='https://copr-be.cloud.fedoraproject.org',
                    help='use this url as baseurl to backend instead of\nhttps://copr-be.cloud.fedoraproject.org')
parser.add_argument('--user', action='store',
                    help='only download gpg keys for projects of this user')
parser.add_argument('--project', action='store',
                    help='only download gpg keys for projects of this name')
parser.add_argument('--isolate-files', action='store_true',
                    help='Each GPG file is stored in separate file.')
parser.add_argument('--path', action='store', default='./',
                    help='path to folder where keys are stored')

args = parser.parse_args()

be_url_tmpl = args.beurl+'/results/{username}/{project_name}/pubkey.gpg'

cli = Client.create_from_config_file()
cli.config["copr_url"] = args.feurl

if args.file:
    output_file = open(args.file, 'w')
else:
    output_file = None

try:
    main()
except KeyboardInterrupt as error:
    pass
