Hosted at https://xanthics.github.io/poe_gen_gwennen/

Generate compact Search Strings for Gwennen. Prices are pulled from poe.ninja, with the last update time at the top. Simple filtering is possible by adjusting the chaos value, and the Select All Visible Only button will behave as described, selecting visible rows and unselecting hidden rows.

Every base that should be able to appear on Gwennen, including implicits and other words that can highlight an item, is broken down in to all non-common ngrams of length 1 to word length. Once you make a selection with the checkboxes and click Generate String a webworker will be started to bruteforce the shortest possible simple search string(s). It does this by removing all of the bad ngrams from the chosen bases, checking if any of the chosen bases share a short ngram, and then building as few search strings as possible.

This project runs about 4x faster on Chrome(~1.5s) vs Firefox(7-8s) for whatever reason. As an FYI.

Uniques that are assumed unobtainable, EG Blight encounter only or corrupted jewel outcomes, are listed in this [file](ninja_data.py).