# The World in One Day — Friday 20 November 2026

Entry for the make.fun bounty **news-image-20261120** ("Sum up 20 November's
world news in one image").

`entry.png` is a one-page, newspaper-style visual atlas of the world's news on
**Friday 20 November 2026**: a large dated masthead, one hero story, and
fourteen further panels — fifteen stories in total, each with a section label,
a bold headline, a one- or two-line summary and a simple flat icon. Every name,
number and date on the page was verified against live reporting on
20–21 November 2026 before it was put into the design brief (see the item list
below).

## How the image was made

The image was designed in **Canva** (`create-design`) from a brief containing
the exact verified wording for every panel, then exported as PNG and resized
to 1024 × 1024 px (587,037 bytes, within the 1024 × 1024 px / 1 MiB limits).

- Canva design: https://canva.link/64sxse6f3d8q5et
- Canva design id: `DAHbiCsvSbQ`
- Edit URL: https://www.canva.com/d/w6M73QM0JA6ia0W
- View URL: https://www.canva.com/d/Y8HEjXFE9FiyDKE

All icons are generic silhouettes (a bridge, a tanker, a skyscraper, scales of
justice, a ballot box); no specific real landmark is depicted.

## Running the entry

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # local run
```

`main.py` (Python 3, standard library only) simply copies the bundled
`entry.png` to the output directory. It uses no network and no timestamps, so
repeated runs produce byte-identical output.

## The fifteen stories, with sources

1. **Ukraine — Russia's huge barrage: 400+ drones, 110 missiles.** Kyiv's
   Dnipro bridges hit; 8 killed and nearly 30 hurt (figures given by President
   Zelensky); two Russian Kh-101 missiles fell inside Poland; the Dutch
   embassy in Kyiv was damaged.
   Sources: Meanwhile in Ukraine, "TOP NEWS TODAY — November 20, 2026"
   (patreon.com); BBC News and France 24 headlines (via feed.ayhart.com);
   informedclearly.com daily summary 2026-11-20.
2. **Shenzhen — Trump, Xi & Putin declare peace.** The trilateral summit ended
   with a joint peace declaration but no deal on Ukraine; the US and China
   agreed humans must keep control of military AI.
   Sources: Open Chronicle, "Global News Brief, November 20, 2026"
   (openchronicle.org); Daily Brief 2026-11-20 (briefing.3xnl.ai);
   standardtopic.com.
3. **Markets — record $81 billion IPO can't stop the AI rout.** Anthropic
   raised $81 billion in history's biggest IPO (+17% on debut); on Fri 20 Nov
   the Dow fell 1,101 points, the S&P 500 fell a sixth straight day and
   Taiwan's market sank 6.2%.
   Sources: WSJ, "Anthropic Raises $81 Billion in Biggest IPO Ever" and "U.S.
   Stocks Slide as AI Bust Continues Despite Anthropic IPO" (wsj.com);
   GlobalData; briefing.3xnl.ai.
4. **The Hague — World Court: Myanmar committed genocide.** The ICJ found
   Myanmar responsible for genocide against the Rohingya — a first in the
   court's history — and ordered reparations; the junta rejected the verdict.
   Sources: Le Monde (20 Nov 2026); WSJ; CNN (19–20 Nov 2026); UN News
   (20 Nov 2026); ReliefWeb/IIMM.
5. **Hormuz — 'largest energy shock on record'.** The US blockade tightened on
   Iranian shipping as the IEA warned of a record supply shock; Brent crude
   climbed to $92.77.
   Sources: standardtopic.com (20 Nov 2026); IANS (ianslive.in, 20 Nov 2026);
   houseofsaud.com (Reuters-linked).
6. **Tech / USA — Microsoft outage fells offices worldwide.** Outlook and
   Teams were down for over nine hours globally; amid the outage wave the
   White House replaced US cyber chief Sean Cairncross.
   Sources: informedclearly.com (20 Nov summary); briefing.3xnl.ai;
   feed.ayhart.com.
7. **Brussels — UK–EU 'reset': food checks scrapped.** A decade after Brexit,
   the summit deals linked carbon markets and opened 100,000 youth-mobility
   places each way; von der Leyen hailed a "turning point".
   Sources: Reuters, "What EU and UK have agreed to at summit" (reuters.com,
   2026-11-20); CNN (2026/11/20); AP via europesays.com.
8. **Climate / Antalya — COP31 runs into overtime, fossil fuels deleted.** No
   deal by Friday's deadline; the revised draft dropped every mention of
   fossil fuels and the $120 billion adaptation fund.
   Sources: Magna Bureau (20 Nov 2026); TFNOS (tfnos.org, citing The Guardian
   and Folha de S.Paulo); news.watannews.dk.
9. **Haiti — police storm gang stronghold, 34 killed.** The offensive retook
   the Martissant corridor in Port-au-Prince after five years of gang control;
   police reported no other casualties.
   Sources: Reuters via DevDiscourse (20 Nov 2026); CMC via cananews.com;
   BusinessMirror (20 Nov 2026).
10. **Saudi Arabia — missile damages Riyadh's tallest tower.** A Houthi strike
    hit the PIF Tower, the sovereign wealth fund's HQ; windows were blown out
    over seven to eight floors, with no injuries.
    Sources: WSJ; Reuters via DevDiscourse (20 Nov 2026); Fox News.
11. **USA / chips — California subpoenas Nvidia over China chips.** Attorney
    General Rob Bonta is probing whether advanced chips reached China and
    whether investors were misled.
    Sources: IANS (ianslive.in, 20 Nov 2026); briefing.3xnl.ai.
12. **Crimea — Ukraine hits the Kerch Bridge again.** Neptune missiles damaged
    the road and rail spans of Russia's bridge to Crimea; Moscow vowed
    retaliation.
    Sources: Meanwhile in Ukraine Nov 20 roundup (patreon.com);
    standardtopic.com.
13. **Taiwan — Russian bombers enter Taiwan's air zone.** Two Tu-95 bombers
    crossed the island's air defence zone during APEC; Taipei scrambled
    fighter jets. (Single source; wording kept plain.)
    Source: informedclearly.com daily summary 2026-11-20.
14. **Germany — Merz: no 'new Yalta' over Europe.** Berlin rejects any
    big-power settlement on Europe's future made without Europeans at the
    table. (Single source; wording kept plain.)
    Source: Open Chronicle, Global News Brief, November 20, 2026.
15. **El Salvador — Bukele registers for a third term.** The president filed
    for February's election after a constitutional rewrite scrapped term
    limits.
    Sources: Al Jazeera via feed.ayhart.com; Breitbart (2026/11/20);
    news.watannews.dk.

One widely-circulated item was deliberately excluded: the "Kramatorsk bus
strike" reported in some AI summaries actually happened on 8 October 2026, not
20 November (Wikipedia, "2026 Kramatorsk bus massacre"; BBC archive).

## License

MIT — see `LICENSE`.

## Production notes

The image was designed in Canva (design DAHbiCsvSbQ, linked above) and
exported at 2380x2380, then downscaled to 1024x1024. Three small text
rendering defects in the Canva export were corrected locally without
changing the design: the sources footer was re-typeset, "dratt" in
panel 8 was corrected to "draft", and "Europets" in panel 14 was
corrected to "Europe's" (the latter two by transplanting the design's
own glyphs). A pixel diff against the raw export confirms no other
changes.
