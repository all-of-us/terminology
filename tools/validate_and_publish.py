"""Validates input codebooks and questionnaires, and publishes valid results.

Inputs:
  Downloads current codebooks from Google sheets (where they are authored).
  Reads temporary questionnaire JSON files (exported from their authoring tool).
Output:
  If the combination of codebook and questionnaires is valid, this script
publishes the result by commiting it to the repository. Only this script should
ever commit terminology data. Published results may then be deployed to the Raw
Data Repository (RDR) using deploy.py.
"""

import logging
import sys

from main_util import configure_logging, get_parser


class _ValidationResult(object):
  def __init__(self):
    # Human-readable string validation results, categorized by severity.
    self.errors = []
    self.warnings = []

  def merge(self, other):
    self.error_messages += other.error_messages

  def log_all(self):
    for warning in self.warnings:
      logging.warning(warning)
    for error in self.errors:
      logging.error(error)


def main(commit_if_valid):
  codebook_paths = _download_codebooks()
  questionnaire_paths = _list_questionnaires()
  result = _validate_codebook(codebook_paths)
  result.Merge(_validate_questionnaires(questionnaire_paths))
  result.log_all()
  if result.errors:
    return False
  if commit_if_valid:
    _commit(codebook_paths, questionnaire_paths)
  return True


if __name__ == '__main__':
  configure_logging()
  parser = get_parser()
  parser.add_argument(
      '--commit', action='store_true',
      help='If the inputs are valid, commit (publish) the results.')
  args = parser.parse_arguments()
  if not main(args.commit):
    sys.exit(1)
