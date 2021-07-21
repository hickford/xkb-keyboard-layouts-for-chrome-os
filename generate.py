from lxml import etree
import sys, json

# Chrome OS uses base.xml from xkeyboard-config 2.27
# https://source.chromium.org/chromiumos/chromiumos/codesearch/+/main:src/third_party/chromiumos-overlay/x11-misc/xkeyboard-config/
# https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/blob/xkeyboard-config-2.27/rules/base.xml
evdev_path = sys.argv[1] if len(sys.argv) > 1 else "/usr/share/X11/xkb/rules/evdev.xml"

evdev = etree.parse(evdev_path)
manifest = dict() # https://developer.chrome.com/docs/extensions/mv3/manifest/
manifest['manifest_version'] = 3
manifest['name'] = 'XKB keyboard layouts for Chrome OS'
manifest['version'] = '0.0.5'
manifest['description'] = "500+ keyboard layouts for Chrome OS. This extension makes all XKB layouts visible in Chrome OS."
manifest['icons'] = {'128' : 'icon128.png'}
manifest['input_components'] = list()

from typing import List, NamedTuple, Optional
class ConfigItemDetails(NamedTuple):
    """Details from a single configItem element"""
    name: str
    shortDescription: Optional[str]
    description: Optional[str]
    countries: Optional[List[str]]
    languages: Optional[List[str]]

class LayoutDetails(NamedTuple):
    """Details combining layout and optional variant"""
    layout: str
    variant: Optional[str]
    shortDescription: Optional[str]
    description: Optional[str]
    countries: Optional[List[str]]
    languages: Optional[List[str]]

    def xkb_name(self) -> str:
        return f"{self.layout}({self.variant})" if self.variant else self.layout


def merge(parent : ConfigItemDetails, variant : Optional[ConfigItemDetails]) -> LayoutDetails:
    if not variant:
        return LayoutDetails(layout = parent.name, variant=None, shortDescription = parent.shortDescription, description = parent.description, countries = parent.countries, languages = parent.languages)
    return LayoutDetails(layout=parent.name, variant=variant.name, shortDescription = variant.shortDescription, description=variant.description, countries=variant.countries if variant.countries != None else parent.countries, languages = variant.languages if variant.languages != None else parent.languages)

import langcodes

def append_input_component(details: LayoutDetails):
    obj = dict()
    obj['name']= f"XKB's {details.xkb_name()} -- {details.description}"
    obj['type']='ime'
    obj['id']="all-xkb-layouts-" + details.xkb_name()
    obj['description']=details.description
    if details.languages:
        # languages = [f"{language}-{country}" for country in details.countries for language in details.languages] if details.countries else details.languages
        obj['language']=[langcodes.standardize_tag(language) for language in details.languages] # multiple allowed
    obj['layouts']=[details.xkb_name()] # list of one
    manifest['input_components'].append(obj)


def get_config_details(configItem) -> ConfigItemDetails:
    name = configItem.find('name').text
    shortDescription = configItem.find('shortDescription').text if configItem.find('shortDescription') is not None else None
    description = configItem.find('description').text if configItem.find('description') is not None else None
    countries = [x.text for x in configItem.findall('countryList/iso3166Id')] if configItem.find('countryList') is not None else None
    languages = [x.text for x in configItem.findall('languageList/iso639Id')] if configItem.find('languageList') is not None else None
    return ConfigItemDetails(name, shortDescription, description, countries, languages)


for layout in evdev.findall('layoutList/layout'):
    parent = get_config_details(layout.find('configItem'))
    append_input_component(merge(parent, None))
    for variant in layout.findall('variantList/variant/configItem'):
        append_input_component(merge(parent, get_config_details(variant)))

# TODO: exclude layouts shipped in Chrome OS's google_xkb_manifest.json

with open('manifest.json', 'w') as f:
    json.dump(manifest, f, indent=4)
