from multiprocessing.sharedctypes import Value
from lxml import etree
import sys, json

from typing import Iterator, NamedTuple, Optional

class LayoutDetails(NamedTuple):
    """Details combining layout and optional variant"""
    layout: str
    variant: Optional[str]
    brief: Optional[str]
    description: Optional[str]
    """Countries"""
    iso3166: Optional[list[str]]
    """Languages"""
    iso639: Optional[list[str]]

    def xkb_name(self) -> str:
        return f"{self.layout}({self.variant})" if self.variant else self.layout


import langcodes
def language(layout: LayoutDetails) -> str:
    # https://tools.ietf.org/html/bcp47
    if not layout.iso639:
        raise ValueError(f"no language for {layout.xkb_name()}")
    tag = layout.iso639[0]
    if layout.iso3166 and len(layout.iso3166) == 1:
        tag += "-" + layout.iso3166[0]
    return langcodes.standardize_tag(tag)


def append_input_component(details: LayoutDetails, manifest):
    obj = dict[str, object]()
    obj['name']= f"XKB's {details.xkb_name()} -- {details.description}"
    obj['id']="all-xkb-layouts-" + details.xkb_name()
    try:
        obj['language'] = [language(details)]
    except ValueError:
        # necessary otherwise switching to layout will crash Chrome OS
        obj['language']=['??']
    obj['layouts']=[details.xkb_name()] # list of one
    manifest['input_components'].append(obj)


def layouts_from_yaml_path(path: str) -> list[LayoutDetails]:
    import ruamel.yaml
    return [LayoutDetails(**layout) for layout in ruamel.yaml.safe_load(open(path))['layouts']]


if __name__ == "__main__":
    yaml_path = sys.argv[1] if sys.argv[1:] else "xkbcli-list.yaml"
    manifest = dict[str, object]() # https://developer.chrome.com/docs/extensions/mv3/manifest/
    manifest['manifest_version'] = 3
    manifest['name'] = 'XKB keyboard layouts for Chrome OS'
    manifest['version'] = '0.0.9'
    manifest['description'] = "500+ keyboard layouts for Chrome OS. This extension makes all XKB layouts visible in Chrome OS."
    manifest['icons'] = {'128' : 'icon128.png'}
    manifest['input_components'] = list()

    for layout in layouts_from_yaml_path(yaml_path):
        append_input_component(layout, manifest)

    with open('manifest.json', 'w') as f:
        json.dump(manifest, f, indent=4)
