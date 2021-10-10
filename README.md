# XKB keyboard layouts for Chrome OS

Chrome OS uses keyboard layouts based on [XKB](https://freedesktop.org/wiki/Software/XKeyboardConfig/). XKB defines [over 500 layouts](https://manpages.debian.org/buster/xkb-data/xkeyboard-config.7.en.html#LAYOUTS) but Chrome OS only exposes a [subset of around 150](https://chromium.googlesource.com/chromium/src/+/master/chrome/browser/resources/chromeos/input_method/google_xkb_manifest.json). This extension makes all XKB keyboard layouts visible in Chrome OS.

## Installation

From Chrome Web Store https://chrome.google.com/webstore/detail/eogbkpghmlfbjmcanfcfbcnjlmhflbej

## Charts

There are charts grouped by language at https://hickford.github.io/xkb_ldml/layouts/ . The XKB layouts are labelled 'linux'. The layouts labelled 'chromeos' are available without this extension.

## Developer instructions

1. Check [xkeyboard-config version in Chrome OS](https://source.chromium.org/chromiumos/chromiumos/codesearch/+/main:src/third_party/chromiumos-overlay/x11-misc/xkeyboard-config/) remains 2.27.
2. Download [base.xml at version 2.27](https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/blob/xkeyboard-config-2.27/rules/base.xml):

       http --download https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config/-/raw/xkeyboard-config-2.27/rules/base.xml

3. Generate extension manifest:

       python3 generate.py base.xml

## See also

https://github.com/google/extra-keyboards-for-chrome-os offers individual extensions for several layouts, including some of those found in this extension.

## Layouts included 

| XKB layout | Description |
| -- | -- |
| af | Afghani |
| af(fa-olpc) | Persian (Afghanistan, Dari OLPC) |
| af(olpc-ps) | Pashto (Afghanistan, OLPC) |
| af(ps) | Pashto |
| af(uz-olpc) | Uzbek (Afghanistan, OLPC) |
| af(uz) | Uzbek (Afghanistan) |
| al | Albanian |
| al(plisi) | Albanian (Plisi) |
| am | Armenian |
| am(eastern-alt) | Armenian (alt. eastern) |
| am(eastern) | Armenian (eastern) |
| am(phonetic-alt) | Armenian (alt. phonetic) |
| am(phonetic) | Armenian (phonetic) |
| am(western) | Armenian (western) |
| ara | Arabic |
| ara(azerty_digits) | Arabic (AZERTY/digits) |
| ara(azerty) | Arabic (AZERTY) |
| ara(buckwalter) | Arabic (Buckwalter) |
| ara(digits) | Arabic (digits) |
| ara(mac) | Arabic (Macintosh) |
| ara(olpc) | Arabic (OLPC) |
| ara(qwerty_digits) | Arabic (qwerty/digits) |
| ara(qwerty) | Arabic (QWERTY) |
| at | German (Austria) |
| at(mac) | German (Austria, Macintosh) |
| at(nodeadkeys) | German (Austria, no dead keys) |
| at(sundeadkeys) | German (Austria, with Sun dead keys) |
| au | English (Australian) |
| az | Azerbaijani |
| az(cyrillic) | Azerbaijani (Cyrillic) |
| ba | Bosnian |
| ba(alternatequotes) | Bosnian (with guillemets) |
| ba(unicode) | Bosnian (with Bosnian digraphs) |
| ba(unicodeus) | Bosnian (US, with Bosnian digraphs) |
| ba(us) | Bosnian (US, with Bosnian letters) |
| bd | Bangla |
| bd(probhat) | Bangla (Probhat) |
| be | Belgian |
| be(iso-alternate) | Belgian (alt. ISO) |
| be(nodeadkeys) | Belgian (no dead keys) |
| be(oss_latin9) | Belgian (alt., Latin-9 only) |
| be(oss_sundeadkeys) | Belgian (alt., with Sun dead keys) |
| be(oss) | Belgian (alt.) |
| be(sundeadkeys) | Belgian (with Sun dead keys) |
| be(wang) | Belgian (Wang 724 AZERTY) |
| bg | Bulgarian |
| bg(bas_phonetic) | Bulgarian (new phonetic) |
| bg(phonetic) | Bulgarian (traditional phonetic) |
| br | Portuguese (Brazil) |
| br(dvorak) | Portuguese (Brazil, Dvorak) |
| br(nativo-epo) | Esperanto (Brazil, Nativo) |
| br(nativo-us) | Portuguese (Brazil, Nativo for US keyboards) |
| br(nativo) | Portuguese (Brazil, Nativo) |
| br(nodeadkeys) | Portuguese (Brazil, no dead keys) |
| br(thinkpad) | Portuguese (Brazil, IBM/Lenovo ThinkPad) |
| brai | Braille |
| brai(left_hand_invert) | Braille (left-handed inverted thumb) |
| brai(left_hand) | Braille (left-handed) |
| brai(right_hand_invert) | Braille (right-handed inverted thumb) |
| brai(right_hand) | Braille (right-handed) |
| bt | Dzongkha |
| bw | Tswana |
| by | Belarusian |
| by(latin) | Belarusian (Latin) |
| by(legacy) | Belarusian (legacy) |
| ca | French (Canada) |
| ca(eng) | English (Canada) |
| ca(fr-dvorak) | French (Canada, Dvorak) |
| ca(fr-legacy) | French (Canada, legacy) |
| ca(ike) | Inuktitut |
| ca(multi-2gr) | Canadian Multilingual (2nd part) |
| ca(multi) | Canadian Multilingual (1st part) |
| ca(multix) | Canadian Multilingual |
| cd | French (Democratic Republic of the Congo) |
| ch | German (Switzerland) |
| ch(de_mac) | German (Switzerland, Macintosh) |
| ch(de_nodeadkeys) | German (Switzerland, no dead keys) |
| ch(de_sundeadkeys) | German (Switzerland, with Sun dead keys) |
| ch(fr_mac) | French (Switzerland, Macintosh) |
| ch(fr_nodeadkeys) | French (Switzerland, no dead keys) |
| ch(fr_sundeadkeys) | French (Switzerland, with Sun dead keys) |
| ch(fr) | French (Switzerland) |
| ch(legacy) | German (Switzerland, legacy) |
| cm | English (Cameroon) |
| cm(azerty) | Cameroon Multilingual (AZERTY) |
| cm(dvorak) | Cameroon Multilingual (Dvorak) |
| cm(french) | French (Cameroon) |
| cm(mmuock) | Mmuock |
| cm(qwerty) | Cameroon Multilingual (QWERTY) |
| cn | Chinese |
| cn(altgr-pinyin) | Hanyu Pinyin (altgr) |
| cn(tib_asciinum) | Tibetan (with ASCII numerals) |
| cn(tib) | Tibetan |
| cn(ug) | Uyghur |
| cz | Czech |
| cz(bksl) | Czech (with <\\|> key) |
| cz(dvorak-ucw) | Czech (US, Dvorak, UCW support) |
| cz(qwerty_bksl) | Czech (QWERTY, extended backslash) |
| cz(qwerty) | Czech (QWERTY) |
| cz(rus) | Russian (Czech, phonetic) |
| cz(ucw) | Czech (UCW, only accented letters) |
| de | German |
| de(deadacute) | German (dead acute) |
| de(deadgraveacute) | German (dead grave acute) |
| de(deadtilde) | German (dead tilde) |
| de(dsb_qwertz) | Lower Sorbian (QWERTZ) |
| de(dsb) | Lower Sorbian |
| de(dvorak) | German (Dvorak) |
| de(mac_nodeadkeys) | German (Macintosh, no dead keys) |
| de(mac) | German (Macintosh) |
| de(neo) | German (Neo 2) |
| de(nodeadkeys) | German (no dead keys) |
| de(qwerty) | German (QWERTY) |
| de(ro_nodeadkeys) | Romanian (Germany, no dead keys) |
| de(ro) | Romanian (Germany) |
| de(ru) | Russian (Germany, phonetic) |
| de(sundeadkeys) | German (with Sun dead keys) |
| de(T3) | German (T3) |
| de(tr) | Turkish (Germany) |
| dk | Danish |
| dk(dvorak) | Danish (Dvorak) |
| dk(mac_nodeadkeys) | Danish (Macintosh, no dead keys) |
| dk(mac) | Danish (Macintosh) |
| dk(nodeadkeys) | Danish (no dead keys) |
| dk(winkeys) | Danish (Win keys) |
| dz | Berber (Algeria, Latin) |
| dz(ar) | Arabic (Algeria) |
| dz(ber) | Berber (Algeria, Tifinagh) |
| ee | Estonian |
| ee(dvorak) | Estonian (Dvorak) |
| ee(nodeadkeys) | Estonian (no dead keys) |
| ee(us) | Estonian (US, with Estonian letters) |
| epo | Esperanto |
| epo(legacy) | Esperanto (displaced semicolon and quote, obsolete) |
| es | Spanish |
| es(ast) | Asturian (Spain, with bottom-dot H and bottom-dot L) |
| es(cat) | Catalan (Spain, with middle-dot L) |
| es(deadtilde) | Spanish (dead tilde) |
| es(dvorak) | Spanish (Dvorak) |
| es(mac) | Spanish (Macintosh) |
| es(nodeadkeys) | Spanish (no dead keys) |
| es(sundeadkeys) | Spanish (with Sun dead keys) |
| es(winkeys) | Spanish (Win keys) |
| et | Amharic |
| fi | Finnish |
| fi(classic) | Finnish (classic) |
| fi(mac) | Finnish (Macintosh) |
| fi(nodeadkeys) | Finnish (classic, no dead keys) |
| fi(smi) | Northern Saami (Finland) |
| fi(winkeys) | Finnish (Winkeys) |
| fo | Faroese |
| fo(nodeadkeys) | Faroese (no dead keys) |
| fr | French |
| fr(azerty) | French (AZERTY) |
| fr(bepo_latin9) | French (Bepo, ergonomic, Dvorak way, Latin-9 only) |
| fr(bepo) | French (Bepo, ergonomic, Dvorak way) |
| fr(bre) | French (Breton) |
| fr(dvorak) | French (Dvorak) |
| fr(geo) | Georgian (France, AZERTY Tskapo) |
| fr(latin9_nodeadkeys) | French (legacy, alt., no dead keys) |
| fr(latin9_sundeadkeys) | French (legacy, alt., with Sun dead keys) |
| fr(latin9) | French (legacy, alt.) |
| fr(mac) | French (Macintosh) |
| fr(nodeadkeys) | French (no dead keys) |
| fr(oci) | Occitan |
| fr(oss_latin9) | French (alt., Latin-9 only) |
| fr(oss_nodeadkeys) | French (alt., no dead keys) |
| fr(oss_sundeadkeys) | French (alt., with Sun dead keys) |
| fr(oss) | French (alt.) |
| fr(sundeadkeys) | French (with Sun dead keys) |
| fr(us) | French (US, with French letters) |
| gb | English (UK) |
| gb(colemak) | English (UK, Colemak) |
| gb(dvorak) | English (UK, Dvorak) |
| gb(dvorakukp) | English (UK, Dvorak, with UK punctuation) |
| gb(extd) | English (UK, extended, with Win keys) |
| gb(intl) | English (UK, intl., with dead keys) |
| gb(mac_intl) | English (UK, intl., Macintosh) |
| gb(mac) | English (UK, Macintosh) |
| gb(pl) | Polish (British keyboard) |
| ge | Georgian |
| ge(ergonomic) | Georgian (ergonomic) |
| ge(mess) | Georgian (MESS) |
| ge(os) | Ossetian (Georgia) |
| ge(ru) | Russian (Georgia) |
| gh | English (Ghana) |
| gh(akan) | Akan |
| gh(avn) | Avatime |
| gh(ewe) | Ewe |
| gh(fula) | Fula |
| gh(ga) | Ga |
| gh(generic) | English (Ghana, multilingual) |
| gh(gillbt) | English (Ghana, GILLBT) |
| gh(hausa) | Hausa (Ghana) |
| gn | French (Guinea) |
| gr | Greek |
| gr(extended) | Greek (extended) |
| gr(nodeadkeys) | Greek (no dead keys) |
| gr(polytonic) | Greek (polytonic) |
| gr(simple) | Greek (simple) |
| hr | Croatian |
| hr(alternatequotes) | Croatian (with guillemets) |
| hr(unicode) | Croatian (with Croatian digraphs) |
| hr(unicodeus) | Croatian (US, with Croatian digraphs) |
| hr(us) | Croatian (US, with Croatian letters) |
| hu | Hungarian |
| hu(101_qwerty_comma_dead) | Hungarian (101/QWERTY/comma/dead keys) |
| hu(101_qwerty_comma_nodead) | Hungarian (101/QWERTY/comma/no dead keys) |
| hu(101_qwerty_dot_dead) | Hungarian (101/QWERTY/dot/dead keys) |
| hu(101_qwerty_dot_nodead) | Hungarian (101/QWERTY/dot/no dead keys) |
| hu(101_qwertz_comma_dead) | Hungarian (101/QWERTZ/comma/dead keys) |
| hu(101_qwertz_comma_nodead) | Hungarian (101/QWERTZ/comma/no dead keys) |
| hu(101_qwertz_dot_dead) | Hungarian (101/QWERTZ/dot/dead keys) |
| hu(101_qwertz_dot_nodead) | Hungarian (101/QWERTZ/dot/no dead keys) |
| hu(102_qwerty_comma_dead) | Hungarian (102/QWERTY/comma/dead keys) |
| hu(102_qwerty_comma_nodead) | Hungarian (102/QWERTY/comma/no dead keys) |
| hu(102_qwerty_dot_dead) | Hungarian (102/QWERTY/dot/dead keys) |
| hu(102_qwerty_dot_nodead) | Hungarian (102/QWERTY/dot/no dead keys) |
| hu(102_qwertz_comma_dead) | Hungarian (102/QWERTZ/comma/dead keys) |
| hu(102_qwertz_comma_nodead) | Hungarian (102/QWERTZ/comma/no dead keys) |
| hu(102_qwertz_dot_dead) | Hungarian (102/QWERTZ/dot/dead keys) |
| hu(102_qwertz_dot_nodead) | Hungarian (102/QWERTZ/dot/no dead keys) |
| hu(nodeadkeys) | Hungarian (no dead keys) |
| hu(qwerty) | Hungarian (QWERTY) |
| hu(standard) | Hungarian (standard) |
| id | Indonesian (Jawi) |
| ie | Irish |
| ie(CloGaelach) | CloGaelach |
| ie(ogam_is434) | Ogham (IS434) |
| ie(ogam) | Ogham |
| ie(UnicodeExpert) | Irish (UnicodeExpert) |
| il | Hebrew |
| il(biblical) | Hebrew (Biblical, Tiro) |
| il(lyx) | Hebrew (lyx) |
| il(phonetic) | Hebrew (phonetic) |
| in | Indian |
| in(ben_baishakhi) | Bangla (India, Baishakhi) |
| in(ben_bornona) | Bangla (India, Bornona) |
| in(ben_gitanjali) | Bangla (India, Uni Gitanjali) |
| in(ben_inscript) | Bangla (India, Baishakhi Inscript) |
| in(ben_probhat) | Bangla (India, Probhat) |
| in(ben) | Bangla (India) |
| in(bolnagri) | Hindi (Bolnagri) |
| in(eeyek) | Manipuri (Eeyek) |
| in(eng) | English (India, with rupee) |
| in(guj) | Gujarati |
| in(guru) | Punjabi (Gurmukhi) |
| in(hin-kagapa) | Hindi (KaGaPa phonetic) |
| in(hin-wx) | Hindi (Wx) |
| in(jhelum) | Punjabi (Gurmukhi Jhelum) |
| in(kan-kagapa) | Kannada (KaGaPa phonetic) |
| in(kan-kagapa) | Kannada (KaGaPa phonetic) |
| in(kan) | Kannada |
| in(mal_enhanced) | Malayalam (enhanced Inscript, with rupee) |
| in(mal_lalitha) | Malayalam (Lalitha) |
| in(mal) | Malayalam |
| in(mar-kagapa) | Marathi (KaGaPa phonetic) |
| in(olck) | Ol Chiki |
| in(ori) | Oriya |
| in(san-kagapa) | Sanskrit (KaGaPa phonetic) |
| in(tam_tamilnet_TAB) | Tamil (TamilNet '99, TAB encoding) |
| in(tam_tamilnet_TSCII) | Tamil (TamilNet '99, TSCII encoding) |
| in(tam_tamilnet_with_tam_nums) | Tamil (TamilNet '99 with Tamil numerals) |
| in(tam_tamilnet) | Tamil (TamilNet '99) |
| in(tam) | Tamil (Inscript) |
| in(tel-kagapa) | Telugu (KaGaPa phonetic) |
| in(tel-kagapa) | Telugu (KaGaPa phonetic) |
| in(tel-sarala) | Telugu (Sarala) |
| in(tel) | Telugu |
| in(urd-phonetic) | Urdu (phonetic) |
| in(urd-phonetic3) | Urdu (alt. phonetic) |
| in(urd-winkeys) | Urdu (Win keys) |
| iq | Iraqi |
| iq(ku_alt) | Kurdish (Iraq, Latin Alt-Q) |
| iq(ku_ara) | Kurdish (Iraq, Arabic-Latin) |
| iq(ku_f) | Kurdish (Iraq, F) |
| iq(ku) | Kurdish (Iraq, Latin Q) |
| ir | Persian |
| ir(ku_alt) | Kurdish (Iran, Latin Alt-Q) |
| ir(ku_ara) | Kurdish (Iran, Arabic-Latin) |
| ir(ku_f) | Kurdish (Iran, F) |
| ir(ku) | Kurdish (Iran, Latin Q) |
| ir(pes_keypad) | Persian (with Persian keypad) |
| is | Icelandic |
| is(dvorak) | Icelandic (Dvorak) |
| is(mac_legacy) | Icelandic (Macintosh, legacy) |
| is(mac) | Icelandic (Macintosh) |
| is(nodeadkeys) | Icelandic (no dead keys) |
| is(Sundeadkeys) | Icelandic (with Sun dead keys) |
| it | Italian |
| it(fur) | Friulian (Italy) |
| it(geo) | Georgian (Italy) |
| it(ibm) | Italian (IBM 142) |
| it(intl) | Italian (intl., with dead keys) |
| it(mac) | Italian (Macintosh) |
| it(nodeadkeys) | Italian (no dead keys) |
| it(scn) | Sicilian |
| it(us) | Italian (US, with Italian letters) |
| it(winkeys) | Italian (Winkeys) |
| jp | Japanese |
| jp(dvorak) | Japanese (Dvorak) |
| jp(kana) | Japanese (Kana) |
| jp(kana86) | Japanese (Kana 86) |
| jp(mac) | Japanese (Macintosh) |
| jp(OADG109A) | Japanese (OADG 109A) |
| ke | Swahili (Kenya) |
| ke(kik) | Kikuyu |
| kg | Kyrgyz |
| kg(phonetic) | Kyrgyz (phonetic) |
| kh | Khmer (Cambodia) |
| kr | Korean |
| kr(kr104) | Korean (101/104 key compatible) |
| kz | Kazakh |
| kz(ext) | Kazakh (extended) |
| kz(kazrus) | Kazakh (with Russian) |
| kz(latin) | Kazakh (Latin) |
| kz(ruskaz) | Russian (Kazakhstan, with Kazakh) |
| la | Lao |
| la(stea) | Lao (STEA proposed standard layout) |
| latam | Spanish (Latin American) |
| latam(colemak-gaming) | Spanish (Latin American, Colemak for gaming) |
| latam(colemak) | Spanish (Latin American, Colemak) |
| latam(deadtilde) | Spanish (Latin American, dead tilde) |
| latam(dvorak) | Spanish (Latin American, Dvorak) |
| latam(nodeadkeys) | Spanish (Latin American, no dead keys) |
| latam(sundeadkeys) | Spanish (Latin American, with Sun dead keys) |
| lk | Sinhala (phonetic) |
| lk(tam_TAB) | Tamil (Sri Lanka, TamilNet '99, TAB encoding) |
| lk(tam_unicode) | Tamil (Sri Lanka, TamilNet '99) |
| lk(us) | Sinhala (US, with Sinhala letters) |
| lt | Lithuanian |
| lt(ibm) | Lithuanian (IBM LST 1205-92) |
| lt(lekp) | Lithuanian (LEKP) |
| lt(lekpa) | Lithuanian (LEKPa) |
| lt(std) | Lithuanian (standard) |
| lt(us) | Lithuanian (US, with Lithuanian letters) |
| lv | Latvian |
| lv(adapted) | Latvian (adapted) |
| lv(apostrophe) | Latvian (apostrophe) |
| lv(ergonomic) | Latvian (ergonomic, \u016aGJRMV) |
| lv(fkey) | Latvian (F) |
| lv(modern) | Latvian (modern) |
| lv(tilde) | Latvian (tilde) |
| ma | Arabic (Morocco) |
| ma(french) | French (Morocco) |
| ma(tifinagh-alt-phonetic) | Berber (Morocco, Tifinagh alt. phonetic) |
| ma(tifinagh-alt) | Berber (Morocco, Tifinagh alt.) |
| ma(tifinagh-extended-phonetic) | Berber (Morocco, Tifinagh extended phonetic) |
| ma(tifinagh-extended) | Berber (Morocco, Tifinagh extended) |
| ma(tifinagh-phonetic) | Berber (Morocco, Tifinagh phonetic) |
| ma(tifinagh) | Berber (Morocco, Tifinagh) |
| mao | Maori |
| md | Moldavian |
| md(gag) | Moldavian (Gagauz) |
| me | Montenegrin |
| me(cyrillic) | Montenegrin (Cyrillic) |
| me(cyrillicalternatequotes) | Montenegrin (Cyrillic with guillemets) |
| me(cyrillicyz) | Montenegrin (Cyrillic, ZE and ZHE swapped) |
| me(latinalternatequotes) | Montenegrin (Latin with guillemets) |
| me(latinunicode) | Montenegrin (Latin, Unicode) |
| me(latinunicodeyz) | Montenegrin (Latin, Unicode, QWERTY) |
| me(latinyz) | Montenegrin (Latin, QWERTY) |
| mk | Macedonian |
| mk(nodeadkeys) | Macedonian (no dead keys) |
| ml | Bambara |
| ml(fr-oss) | French (Mali, alt.) |
| ml(us-intl) | English (Mali, US, intl.) |
| ml(us-mac) | English (Mali, US, Macintosh) |
| mm | Burmese |
| mm(zawgyi) | Burmese Zawgyi |
| mn | Mongolian |
| mt | Maltese |
| mt(alt-gb) | Maltese (UK layout with AltGr overrides) |
| mt(alt-us) | Maltese (US layout with AltGr overrides) |
| mt(us) | Maltese (with US layout) |
| mv | Dhivehi |
| my | Malay (Jawi, Arabic Keyboard) |
| my(phonetic) | Malay (Jawi, phonetic) |
| nec_vndr/jp | Japanese (PC-98) |
| ng | English (Nigeria) |
| ng(hausa) | Hausa (Nigeria) |
| ng(igbo) | Igbo |
| ng(yoruba) | Yoruba |
| nl | Dutch |
| nl(mac) | Dutch (Macintosh) |
| nl(std) | Dutch (standard) |
| nl(sundeadkeys) | Dutch (with Sun dead keys) |
| no | Norwegian |
| no(colemak) | Norwegian (Colemak) |
| no(dvorak) | Norwegian (Dvorak) |
| no(mac_nodeadkeys) | Norwegian (Macintosh, no dead keys) |
| no(mac) | Norwegian (Macintosh) |
| no(nodeadkeys) | Norwegian (no dead keys) |
| no(smi_nodeadkeys) | Northern Saami (Norway, no dead keys) |
| no(smi) | Northern Saami (Norway) |
| no(winkeys) | Norwegian (Win keys) |
| np | Nepali |
| ph | Filipino |
| ph(capewell-dvorak-bay) | Filipino (Capewell-Dvorak, Baybayin) |
| ph(capewell-dvorak) | Filipino (Capewell-Dvorak, Latin) |
| ph(capewell-qwerf2k6-bay) | Filipino (Capewell-QWERF 2006, Baybayin) |
| ph(capewell-qwerf2k6) | Filipino (Capewell-QWERF 2006, Latin) |
| ph(colemak-bay) | Filipino (Colemak, Baybayin) |
| ph(colemak) | Filipino (Colemak, Latin) |
| ph(dvorak-bay) | Filipino (Dvorak, Baybayin) |
| ph(dvorak) | Filipino (Dvorak, Latin) |
| ph(qwerty-bay) | Filipino (QWERTY, Baybayin) |
| pk | Urdu (Pakistan) |
| pk(ara) | Arabic (Pakistan) |
| pk(snd) | Sindhi |
| pk(urd-crulp) | Urdu (Pakistan, CRULP) |
| pk(urd-nla) | Urdu (Pakistan, NLA) |
| pl | Polish |
| pl(csb) | Kashubian |
| pl(dvorak_altquotes) | Polish (Dvorak, with Polish quotes on key 1) |
| pl(dvorak_quotes) | Polish (Dvorak, with Polish quotes on quotemark key) |
| pl(dvorak) | Polish (Dvorak) |
| pl(dvp) | Polish (programmer Dvorak) |
| pl(legacy) | Polish (legacy) |
| pl(qwertz) | Polish (QWERTZ) |
| pl(ru_phonetic_dvorak) | Russian (Poland, phonetic Dvorak) |
| pl(szl) | Silesian |
| pt | Portuguese |
| pt(mac_nodeadkeys) | Portuguese (Macintosh, no dead keys) |
| pt(mac_sundeadkeys) | Portuguese (Macintosh, with Sun dead keys) |
| pt(mac) | Portuguese (Macintosh) |
| pt(nativo-epo) | Esperanto (Portugal, Nativo) |
| pt(nativo-us) | Portuguese (Nativo for US keyboards) |
| pt(nativo) | Portuguese (Nativo) |
| pt(nodeadkeys) | Portuguese (no dead keys) |
| pt(sundeadkeys) | Portuguese (with Sun dead keys) |
| ro | Romanian |
| ro(cedilla) | Romanian (cedilla) |
| ro(std_cedilla) | Romanian (standard cedilla) |
| ro(std) | Romanian (standard) |
| ro(winkeys) | Romanian (Win keys) |
| rs | Serbian |
| rs(alternatequotes) | Serbian (Cyrillic with guillemets) |
| rs(latin) | Serbian (Latin) |
| rs(latinalternatequotes) | Serbian (Latin with guillemets) |
| rs(latinunicode) | Serbian (Latin, Unicode) |
| rs(latinunicodeyz) | Serbian (Latin, Unicode, QWERTY) |
| rs(latinyz) | Serbian (Latin, QWERTY) |
| rs(rue) | Pannonian Rusyn |
| rs(yz) | Serbian (Cyrillic, ZE and ZHE swapped) |
| ru | Russian |
| ru(bak) | Bashkirian |
| ru(chm) | Mari |
| ru(cv_latin) | Chuvash (Latin) |
| ru(cv) | Chuvash |
| ru(dos) | Russian (DOS) |
| ru(kom) | Komi |
| ru(legacy) | Russian (legacy) |
| ru(mac) | Russian (Macintosh) |
| ru(os_legacy) | Ossetian (legacy) |
| ru(os_winkeys) | Ossetian (Win keys) |
| ru(phonetic_azerty) | Russian (phonetic, AZERTY) |
| ru(phonetic_dvorak) | Russian (phonetic, Dvorak) |
| ru(phonetic_fr) | Russian (phonetic, French) |
| ru(phonetic_winkeys) | Russian (phonetic, with Win keys) |
| ru(phonetic_yazherty) | Russian (phonetic yazherty) |
| ru(phonetic) | Russian (phonetic) |
| ru(sah) | Yakut |
| ru(srp) | Serbian (Russia) |
| ru(tt) | Tatar |
| ru(typewriter-legacy) | Russian (typewriter, legacy) |
| ru(typewriter) | Russian (typewriter) |
| ru(udm) | Udmurt |
| ru(xal) | Kalmyk |
| se | Swedish |
| se(dvorak) | Swedish (Dvorak) |
| se(mac) | Swedish (Macintosh) |
| se(nodeadkeys) | Swedish (no dead keys) |
| se(rus_nodeadkeys) | Russian (Sweden, phonetic, no dead keys) |
| se(rus) | Russian (Sweden, phonetic) |
| se(smi) | Northern Saami (Sweden) |
| se(svdvorak) | Swedish (Svdvorak) |
| se(swl) | Swedish Sign Language |
| se(us_dvorak) | Swedish (based on US Intl. Dvorak) |
| se(us) | Swedish (US, with Swedish letters) |
| si | Slovenian |
| si(alternatequotes) | Slovenian (with guillemets) |
| si(us) | Slovenian (US, with Slovenian letters) |
| sk | Slovak |
| sk(bksl) | Slovak (extended backslash) |
| sk(qwerty_bksl) | Slovak (QWERTY, extended backslash) |
| sk(qwerty) | Slovak (QWERTY) |
| sn | Wolof |
| sy | Arabic (Syria) |
| sy(ku_alt) | Kurdish (Syria, Latin Alt-Q) |
| sy(ku_f) | Kurdish (Syria, F) |
| sy(ku) | Kurdish (Syria, Latin Q) |
| sy(syc_phonetic) | Syriac (phonetic) |
| sy(syc) | Syriac |
| tg | French (Togo) |
| th | Thai |
| th(pat) | Thai (Pattachote) |
| th(tis) | Thai (TIS-820.2538) |
| tj | Tajik |
| tj(legacy) | Tajik (legacy) |
| tm | Turkmen |
| tm(alt) | Turkmen (Alt-Q) |
| tr | Turkish |
| tr(alt) | Turkish (Alt-Q) |
| tr(crh_alt) | Crimean Tatar (Turkish Alt-Q) |
| tr(crh_f) | Crimean Tatar (Turkish F) |
| tr(crh) | Crimean Tatar (Turkish Q) |
| tr(f) | Turkish (F) |
| tr(intl) | Turkish (intl., with dead keys) |
| tr(ku_alt) | Kurdish (Turkey, Latin Alt-Q) |
| tr(ku_f) | Kurdish (Turkey, F) |
| tr(ku) | Kurdish (Turkey, Latin Q) |
| tr(sundeadkeys) | Turkish (with Sun dead keys) |
| tw | Taiwanese |
| tw(indigenous) | Taiwanese (indigenous) |
| tw(saisiyat) | Saisiyat (Taiwan) |
| tz | Swahili (Tanzania) |
| ua | Ukrainian |
| ua(homophonic) | Ukrainian (homophonic) |
| ua(legacy) | Ukrainian (legacy) |
| ua(phonetic) | Ukrainian (phonetic) |
| ua(rstu_ru) | Russian (Ukraine, standard RSTU) |
| ua(rstu) | Ukrainian (standard RSTU) |
| ua(typewriter) | Ukrainian (typewriter) |
| ua(winkeys) | Ukrainian (Win keys) |
| us | English (US) |
| us(alt-intl) | English (US, alt. intl.) |
| us(altgr-intl) | English (intl., with AltGr dead keys) |
| us(chr) | Cherokee |
| us(colemak) | English (Colemak) |
| us(dvorak-alt-intl) | English (Dvorak, alt. intl.) |
| us(dvorak-classic) | English (classic Dvorak) |
| us(dvorak-intl) | English (Dvorak, intl., with dead keys) |
| us(dvorak-l) | English (Dvorak, left-handed) |
| us(dvorak-r) | English (Dvorak, right-handed) |
| us(dvorak) | English (Dvorak) |
| us(dvp) | English (programmer Dvorak) |
| us(euro) | English (US, euro on 5) |
| us(hbs) | Serbo-Croatian (US) |
| us(intl) | English (US, intl., with dead keys) |
| us(mac) | English (Macintosh) |
| us(olpc2) | English (the divide/multiply keys toggle the layout) |
| us(rus) | Russian (US, phonetic) |
| us(workman-intl) | English (Workman, intl., with dead keys) |
| us(workman) | English (Workman) |
| uz | Uzbek |
| uz(latin) | Uzbek (Latin) |
| vn | Vietnamese |
| vn(fr) | Vietnamese (French, with Vietnamese letters) |
| vn(us) | Vietnamese (US, with Vietnamese letters) |
| za | English (South Africa) |
