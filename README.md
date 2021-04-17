# XKB keyboard layouts for Chrome OS

Chrome OS uses keyboard layouts based on [XKB](https://freedesktop.org/wiki/Software/XKeyboardConfig/). XKB defines [over 500 layouts](https://manpages.debian.org/buster/xkb-data/xkeyboard-config.7.en.html#LAYOUTS) but Chrome OS only exposes a [subset of around 150](https://chromium.googlesource.com/chromium/src/+/master/chrome/browser/resources/chromeos/input_method/google_xkb_manifest.json). This extension makes all XKB keyboard layouts visible in Chrome OS.

## Installation

Pending review in Chrome Web Store https://chrome.google.com/webstore/detail/eogbkpghmlfbjmcanfcfbcnjlmhflbej

## Charts

There are charts grouped by language at https://hickford.github.io/xkb_ldml/layouts/ . The XKB layouts are labelled 'linux'. The layouts labelled 'chromeos' are available without this extension.

## Developer instructions

    # Download XKB configuration as shipped in Chrome OS 
    http --download https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/raw/xkeyboard-config-2.27/rules/base.xml
    # Generate extension manifest
    python3 generate.py base.xml

## See also

https://github.com/google/extra-keyboards-for-chrome-os offers individual extensions for several layouts, including some of those found in this extension.
