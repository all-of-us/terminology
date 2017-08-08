"""Shared paths for input/output files."""

import os


_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

QUESTIONNAIRE_SRC_DIR = os.path.join(_BASE, 'source')
_OUT = os.path.join(_BASE, 'generated')
QUESTIONNAIRE_OUT_DIR = os.path.join(_OUT, 'Questionnaire')
CODESYSTEM_OUT_DIR = os.path.join(_OUT, 'CodeSystem')
