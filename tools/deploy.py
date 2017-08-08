"""Deploys a validated version of All of Us terminology to the RDR."""

import logging

from client import Client
from main_util import configure_logging, get_parser


_HEAD_VERSION = 'HEAD'


def deploy_terminology(rdr_project, terminology_git_version):
  _check_out_version(terminology_git_version)
  client.request_json('POST', _build_payload())


if __name__ == '__main__':
  configure_logging()
  parser = get_parser()
  parser.add_argument(
      'project', default='all-of-us-rdr-sandbox',
      help='RDR environment/project name.')
  parser.add_argument(
      '--version', default=_HEAD_VERSION,
      help='Commit ID from this repository to deploy.')
  args = parser.parse_arguments()
  deploy_terminology(args.project, args.version)
