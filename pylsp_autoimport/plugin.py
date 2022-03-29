import logging
from pylsp import hookimpl
from autoimport import fix_code
from pylsp.config.config import Config
from pylsp.workspace import Document
from typing import List, TypedDict


class RangeLine(TypedDict):
    line: int
    character: int


class Range(TypedDict):
    start: RangeLine
    end: RangeLine


class Change(TypedDict):
    range: Range
    newText: str


logger = logging.getLogger(__name__)


@hookimpl(tryfirst=True)
def pylsp_format_document(config, document):
    return format_document(config, document)


# @hookimpl(tryfirst=True)
# def pylsp_format_range(config, document, range):
#     range["start"]["character"] = 0
#     range["end"]["line"] += 1
#     range["end"]["character"] = 0
#     return format_document(config, document, range)
# Not Implemented Yet


@hookimpl
def pylsp_settings():
    logger.info("Initializing pylsp_autoimport")

    # Disable default plugins that conflicts with our plugin
    return {
        "plugins": {
            "autoimport": {"enabled": True}
            # "autopep8_format": {"enabled": False},
            # "definition": {"enabled": False},
            # "flake8_lint": {"enabled": False},
            # "folding": {"enabled": False},
            # "highlight": {"enabled": False},
            # "hover": {"enabled": False},
            # "jedi_completion": {"enabled": False},
            # "jedi_rename": {"enabled": False},
            # "mccabe_lint": {"enabled": False},
            # "preload_imports": {"enabled": False},
            # "pycodestyle_lint": {"enabled": False},
            # "pydocstyle_lint": {"enabled": False},
            # "pyflakes_lint": {"enabled": False},
            # "pylint_lint": {"enabled": False},
            # "references": {"enabled": False},
            # "rope_completion": {"enabled": False},
            # "rope_rename": {"enabled": False},
            # "signature": {"enabled": False},
            # "symbols": {"enabled": False},
            # "yapf_format": {"enabled": False},
        },
    }


def format_document(
    config: Config, document: Document, range: Range = None
) -> List[Change]:
    """
    autoimport via format.
    Parameters
    ----------
    config : Config
        The pylsp config.
    document : Document
        The document to be linted.
    Returns
    -------
    List[Dict[str, Any]]
        List of the linting data.
    """
    # Heavily based on pylsp-mypy code
    range: Range = {
        "start": {"line": 0, "character": 0},
        "end": {"line": len(document.lines), "character": 0},
    }

    formatted_text: str = fix_code(document.source)
    return [{"range": range, "newText": formatted_text}]
