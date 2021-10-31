from lxml import etree
import sys, json

evdev_path = sys.argv[1] if len(sys.argv) > 1 else "/usr/share/X11/xkb/rules/evdev.xml"

evdev = etree.parse(evdev_path)
manifest = dict() # https://developer.chrome.com/docs/extensions/mv3/manifest/
manifest['manifest_version'] = 3
manifest['name'] = 'XKB keyboard layouts for Chrome OS'
manifest['version'] = '0.0.7'
manifest['description'] = "500+ keyboard layouts for Chrome OS. This extension makes all XKB layouts visible in Chrome OS."
manifest['icons'] = {'128' : 'icon128.png'}
manifest['input_components'] = list()

from typing import List, NamedTuple, Optional
class ConfigItemDetails(NamedTuple):
    """Details from a single configItem element"""
    name: str
    brief: Optional[str]
    description: Optional[str]
    """Countries"""
    iso3166: Optional[List[str]]
    """Languages"""
    iso639: Optional[List[str]]

class LayoutDetails(NamedTuple):
    """Details combining layout and optional variant"""
    layout: str
    variant: Optional[str]
    brief: Optional[str]
    description: Optional[str]
    """Countries"""
    iso3166: Optional[List[str]]
    """Languages"""
    iso639: Optional[List[str]]

    def xkb_name(self) -> str:
        return f"{self.layout}({self.variant})" if self.variant else self.layout


def merge(parent : ConfigItemDetails, variant : Optional[ConfigItemDetails]) -> LayoutDetails:
    if not variant:
        return LayoutDetails(layout = parent.name, variant=None, brief = parent.brief, description = parent.description, iso3166 = parent.iso3166, iso639 = parent.iso639)
    return LayoutDetails(layout=parent.name, variant=variant.name, brief = variant.brief, description=variant.description, iso3166=variant.iso3166 if variant.iso3166 != None else parent.iso3166, iso639 = variant.iso639 if variant.iso639 != None else parent.iso639)

import langcodes

def append_input_component(details: LayoutDetails):
    obj = dict()
    obj['name']= f"XKB's {details.xkb_name()} -- {details.description}"
    obj['id']="all-xkb-layouts-" + details.xkb_name()
    if details.iso639:
        # languages = [f"{language}-{country}" for country in details.countries for language in details.languages] if details.countries else details.languages
        obj['language']=[langcodes.standardize_tag(language) for language in details.iso639] # multiple allowed
    else:
        # necessary otherwise switching to layoyut will crash Chrome OS
        obj['language']=['??']
    obj['layouts']=[details.xkb_name()] # list of one
    manifest['input_components'].append(obj)


def get_config_details(configItem) -> ConfigItemDetails:
    name = configItem.find('name').text
    shortDescription = configItem.find('shortDescription').text if configItem.find('shortDescription') is not None else None
    description = configItem.find('description').text if configItem.find('description') is not None else None
    iso3166 = [x.text for x in configItem.findall('countryList/iso3166Id')] if configItem.find('countryList') is not None else None
    iso639 = [x.text for x in configItem.findall('languageList/iso639Id')] if configItem.find('languageList') is not None else None
    return ConfigItemDetails(name=name, brief=shortDescription, description=description, iso3166=iso3166, iso639=iso639)


for layout in evdev.findall('layoutList/layout'):
    parent = get_config_details(layout.find('configItem'))
    append_input_component(merge(parent, None))
    for variant in layout.findall('variantList/variant/configItem'):
        append_input_component(merge(parent, get_config_details(variant)))

with open('manifest.json', 'w') as f:
    json.dump(manifest, f, indent=4)
