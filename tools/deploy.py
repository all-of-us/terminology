#!/usr/bin/env python
"""Deploys a validated version of All of Us terminology to the RDR."""

import logging

from rdr_client.client import Client
from rdr_common.main_util import configure_logging, get_parser


_HEAD_VERSION = 'HEAD'


def deploy_terminology(client, terminology_git_version):
  _check_out_version(terminology_git_version)
  client.request_json('POST', _build_payload())


def _check_out_version(git_tag):
  """TODO"""


def _build_payload():
  """TODO"""
  return {}


if __name__ == '__main__':
  configure_logging()
  parser = get_parser()
  parser.add_argument(
      'project', default='all-of-us-rdr-sandbox',
      help='RDR environment/project name.')
  parser.add_argument(
      '--version', default=_HEAD_VERSION,
      help='Commit ID from this repository to deploy.')
  client = Client(parser=parser)
  deploy_terminology(client, args.version)
