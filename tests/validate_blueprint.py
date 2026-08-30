"""Perform a small, dependency-light validation of the published blueprint."""

from pathlib import Path
from typing import Any

import yaml


class BlueprintLoader(yaml.SafeLoader):
    """Safe YAML loader that preserves Home Assistant's !input references."""


def _input(loader: BlueprintLoader, node: yaml.Node) -> dict[str, str]:
    return {"input": loader.construct_scalar(node)}


BlueprintLoader.add_constructor("!input", _input)

path = Path("blueprints/automation/kennethaasan/alpstuga_ventilation_boost.yaml")
document: dict[str, Any] = yaml.load(path.read_text(), Loader=BlueprintLoader)

assert document["blueprint"]["domain"] == "automation"
assert document["blueprint"]["input"]
assert "additional_safety_entities" in document["blueprint"]["input"]
assert document["triggers"]
assert document["actions"]
assert document["mode"] == "single"
