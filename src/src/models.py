from dataclasses import dataclass
from typing import Any


@dataclass
class ReplacementRule:

    excel_column: str

    json_key: str

    value: Any

    ignore_blank: bool = True

    case_sensitive: bool = False


@dataclass
class ReplaceResult:

    key: str

    old_value: Any

    new_value: Any

    path: str

    success: bool


@dataclass
class Statistics:

    total_nodes: int = 0

    total_replacements: int = 0

    skipped: int = 0

    failed: int = 0
