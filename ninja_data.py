import requests
from collections import defaultdict

from gen_items import gen_bases


# get price data from poe.ninja
def scrape_ninja():
	good_bases = [x['name'] for x in gen_bases]
	# List of items that cannot be gambled -- Uniques which have a base type that cannot spawn on gwennen are included as well but commented out.  EG flasks or runic bases
	bad_names = {
		# Vinktar's Square
		# "Vessel of Vinktar",
		# Quest Items
		"Survival Instincts", "Survival Secrets", "Survival Skills", "Conqueror's Longevity", "Conqueror's Potency", "Conqueror's Efficiency",
		"Assassin's Haste", "Poacher's Aim", "Warlord's Reach",
		# Corruption only
		"Ancient Waystones", "Atziri's Reign", "Blood Sacrifice", "Brittle Barrier", "Chill of Corruption", "Combustibles", "Corrupted Energy",
		"Fragility", "Hungry Abyss", "Mutated Growth", "Pacifism", "Powerlessness", "Sacrificial Harvest", "Self-Flagellation", "Vaal Sentencing",
		"Weight of Sin", "Fevered Mind", 'Blood of Corruption', "Malachai's Vision",
		# Divination card only item
		'Maw of Mischief',
		# Fated Uniques
		"Amplification Rod", "Asenath's Chant", "Atziri's Reflection", "Cameria's Avarice", "Chaber Cairn", "Cragfall", "Death's Opus", "Doedre's Malevolence", "Doomfletch's Prism",
		"Dreadbeak", "Duskblight", "Frostferno", "Geofri's Devotion", "Geofri's Legacy", "Hrimburn", "Hyrri's Demise", "Kaom's Way", "Malachai's Awakening", "Queen's Escape",
		"The Cauteriser", "The Dancing Duo", "The Iron Fortress", "The Nomad", "The Signal Fire", "The Stormwall", "The Tactician", "The Tempest", "Thirst for Horrors", "Timetwist",
		"Whakatutuki o Matua", "Wildwrap", "Windshriek", "Winterweave", "Ngamahu Tiki",
		# Vendor recipes
		'The Anima Stone', 'Arborix', 'Duskdawn', 'The Goddess Scorned', 'The Goddess Unleashed', 'Kingmaker', 'Magna Eclipsis', 'The Retch', 'Star of Wraeclast', 'The Taming',
		'The Vinktar Square', 'Loreweave',
		# incursion uniques from upgrades
		'Transcendent Flesh', 'Transcendent Mind', 'Transcendent Spirit', 'Slavedriver\'s Hand', 'Coward\'s Legacy', 'Omeyocan', 'Fate of the Vaal', 'Mask of the Stitched Demon', 'Apep\'s Supremacy', 'Zerphi\'s Heart',
		# "Soul Catcher",
		# incursion uniques
		'Sacrificial Heart', 'String of Servitude', 'Tempered Flesh', 'Tempered Mind', 'Tempered Spirit',
		'Shadowstitch', "Apep's Slumber", "Architect's Hand", "Coward's Chains", 'Dance of the Offered', 'Mask of the Spirit Drinker', 'Story of the Vaal',
		# 'Soul Ripper',
		# Breach Uniques
		'Xoph\'s Nurture', 'The Formless Inferno', 'Xoph\'s Blood', 'Tulfall', 'The Perfect Form', 'The Pandemonius', 'Hand of Wisdom and Action', 'Esh\'s Visage', 'Choir of the Storm',
		'Uul-Netol\'s Embrace', 'The Red Trail', 'The Surrender', 'United in Dream', 'Skin of the Lords', 'Presence of Chayula', 'The Red Nightmare', 'The Green Nightmare', 'The Blue Nightmare',
		# Harbinger Uniques -- Currently only drops as pieces
		"The Flow Untethered", "The Fracturing Spinner", "The Tempest's Binding", "The Rippling Thoughts", "The Enmity Divine", "The Unshattered Will",
		# Harbinger Pieces
		"First Piece of Focus", "Second Piece of Focus", "Third Piece of Focus", "Fourth Piece of Focus",
		"First Piece of Directions", "Second Piece of Directions", "Third Piece of Directions",
		"First Piece of Storms", "Second Piece of Storms", "Third Piece of Storms",
		"First Piece of Time", "Second Piece of Time",
		"First Piece of Brutality", "Second Piece of Brutality", "Third Piece of Brutality",
		"First Piece of the Arcane", "Second Piece of the Arcane", "Third Piece of the Arcane",
		# upgraded harbinger uniques
		"The Torrent's Reclamation", "The Shattered Divinity", "The Tempest's Liberation", "The Surging Thoughts", "The Yielding Mortality", "The Immortal Will",
		# Guardians, Shaper, and Elder
		"Voidwalker", "Shaper's Touch", "Starforge", 'Solstice Vigil',
		"Blasphemer's Grasp", "Shimmeron", "Nebuloch", "Hopeshredder", "Impresence", "Cyclopean Coil",
		"Indigon", "The Eternity Shroud", "Disintegrator", "Voidforge", "Mark of the Elder", "Mark of the Shaper", "Voidfletcher", "Watcher's Eye",
		"Soul Ascension",
		# "Dying Sun",
		# Atziri
		"Atziri's Step", "Doryani's Catalyst", "Doryani's Invitation", "Atziri's Reflection",
		"The Vertex", "Atziri's Splendour", "Atziri's Acuity", "Atziri's Disfavour", "Pledge of Hands",
		# "Atziri's Promise",
		# Maven
		"Arn's Anguish", "Graven's Secret", "Olesya's Delight", "Viridi's Veil", 'The Walls', 'The Claim', 'The Closest Peak', 'Atop the Atlas', 'The Vast Horizon', 'The Builder', 'Restless Cycles', 'The False Hope', 'Legacy of Fury',  'Doppelgänger Guise',
		# Bestiary League
		"Saqawal's Flock", "Saqawal's Nest", "Saqawal's Talons", "Saqawal's Winds",
		"Fenumus' Toxins", "Fenumus' Shroud", "Fenumus' Spinnerets", "Fenumus' Weave",
		"Craiceann's Chitin", "Craiceann's Carapace", "Craiceann's Tracks", "Craiceann's Pincers",
		"Farrul's Bite", "Farrul's Fur", "Farrul's Chase", "Farrul's Pounce",
		# Pillars of Arun
		"Gorgon's Gaze",
		# Doryani's Machinarium
		"Doryani's Delusion",
		# Synthesis League
		"Perepiteia", "Mask of the Tribunal", "Garb of the Ephemeral", "Offering to the Serpent", "Storm's Gift", "Nebulis", "Circle of Guilt", "Circle of Regret", "Circle of Fear", "Circle of Anguish", "Circle of Nostalgia",
		# "Bottled Faith",
		# Labyrinth
		"Glitterdisc", "Viper's Scales", "Death's Door", "Winds of Change", "Izaro's Dilemma", "Chitus' Needle", "Spine of the First Claimant", "Xirgil's Crank", "Izaro's Turmoil",
		"Emperor's Might", "Emperor's Cunning", "Emperor's Wit", "Emperor's Mastery",
		# Breach League
		"The Anticipation", "Esh's Mirror", "The Formless Flame", "Skin of the Loyal", "The Snowblind Grace", "The Infinite Pursuit", "Hand of Thought and Motion", "Severed in Sleep", "Xoph's Inception", "Uul-Netol's Kiss", "Xoph's Heart", "The Halcyon", "Voice of the Storm",
		"The Red Dream", "The Green Dream", "The Blue Dream",
		# Abyss League
		"Lightpoacher", "Shroud of the Lightless", "Bubonic Trail", "Tombfist", "Darkness Enthroned",
		# Delve League
		"Command of the Pit", "Crown of the Tyrant", "Cerberus Limb", "Aul's Uprising", "Doryani's Machinarium", 'Hale Negator',
		"Putembo's Valley", "Putembo's Mountain", "Putembo's Meadow",
		"Uzaza's Meadow", "Uzaza's Mountain", "Uzaza's Valley",
		"Ahkeli's Mountain", "Ahkeli's Meadow", "Ahkeli's Valley",
		"Precursor's Emblem",
		# Betrayal League
		"Bitterbind Point", "The Devouring Diadem", "The Queen's Hunger", "Paradoxica", "The Crimson Storm", "Hyperboreus", 'Vivinsect', "Cloak of Tawm'r Isley",
		# "Cinderswallow Urn",
		# Blight League
		"Breathstealer", "Cowl of the Ceraunophile", "Cowl of the Cryophile", "Cowl of the Thermophile", "Sporeguard", "The Stampede",
		# Conqueror & Sirus
		"Crown of the Inward Eye", 'Hands of the High Templar', 'The Saviour', 'Thread of Hope',
		# Delirium
		'One With Nothing', 'The Interrogation', "Kitava's Teachings", 'Voices', 'Split Personality',
		# Harvest
		'Abhorrent Interrogation', "Bear's Girdle", 'Forbidden Shako', 'Law of the Wilds', 'Plume of Pursuit', 'The Felbog Fang',
		"Witchhunter's Judgment",
		# Heist
		'Fated End', "Leadership's Price", "The Admiral", "Chains of Emancipation", "The Fledgling", "Nadir Mode", "Apex Mode", "Font of Thunder", "Actum", "The Iron Mass", "The Hidden Blade", "The Fulcrum", "Expedition's End", "Crest of Desire", "Shattershard",
		# Warbands League
		"Brinerot Flag", "Brinerot Mark", "Brinerot Whalers", "Broken Faith", "Mutewind Pennant", "Mutewind Seal", "Mutewind Whispersteps", "Redblade Band", "Redblade Banner", "Redblade Tramplers", "Steppan Eard", "The Pariah",
		# Ritual
		"Blackflame", "Qotra's Regulator", "Rotblood Promise", "Survivor's Guilt", "Hands of the Fervent",
		# Ultimatum
		"Atziri's Rule", "Cane of Kulemak", "Glimpse of Chaos", "Hateforge", "Mahuxotl's Machination", "Relic of the Pact", "Steelworm", "Temptation Step", "The Scales of Justice", "Triumvirate Authority", "Yaomac's Accord",
		# Scourge
		"Stranglegasp", "Uul-Netol's Vow", "Stasis Prison",
		# Archnemesis & Seige of the Atlas
		"Melding of the Flesh", "Crystallised Omniscience", "Sudden Dawn", "The Annihilating Light", "Ashes of the Stars", "Dissolution of the Flesh", "Polaric Devastation", "Forbidden Flame",
		"Forbidden Flesh", "Ceaseless Feast", "Inextricable Fate", "The Gluttonous Tide", "Black Zenith", "Dawnbreaker",
		# Sentinel uber boss drops
		"Call of the Void", "Echoes of Creation", "Impossible Escape", "Sublime Vision", "The Burden of Truth", "The Eternal Struggle",
		# Lake of Kalandra
		"Kalandra's Touch",
		# Abyss Jewels (Cannot generate bases on gwennen.. yet?)
		# "Amanamu's Gaze", "Tecrod's Gaze", "Ulaman's Gaze", "Kurgal's Gaze",
		# Expedition runic uniques (Cannot generate bases on gwennen.. yet?)
		# "Cadigan's Crown", "Faithguard", "Medved's Challenge", "Nightgrip", "Olroth's Charge", "Usurper's Penance", "Vorana's March",
		# "Elixir of the Unbroken Circle", "Olroth's Resolve", "Starlight Chalice", "Vorana's Preparation",
	}

	# for when people pull stuff out of remove only tabs in league
	legacy_base = {
		'Pillar of the Caged God': ['Long Staff'],
		'Dying Breath': ['Coiled Staff'],
		'Dusktoe': ['Leatherscale Boots'],
		'Duskblight': ['Leatherscale Boots'],
		'Blackgleam': ['Cured Quiver', "Fire Arrow Quiver"],
		'The Signal Fire': ['Cured Quiver', "Fire Arrow Quiver"],
		'The Searing Touch': ['Long Staff'],
		'Wings of Entropy': ['Sundering Axe'],
		'Infernal Mantle': ['Widowsilk Robe'],
		'Essentia Sanguis': ['Eye Gouger'],
		'Auxium': ['Chain Belt'],
		"Architect's Hand": ['Strapped Mitts'],
		'Dance of the Offered': ['Shackled Boots'],
		'Story of the Vaal': ['Variscite Blade'],
		'Mask of the Spirit Drinker': ['Crusader Helmet'],
		"Apep's Slumber": ['Ancient Spirit Shield'],
		"Asphyxia's Wrath": ["Two-Point Arrow Quiver"],
		"Saemus' Gift": ["Two-Point Arrow Quiver"],
		"Steelworm": ["Broadhead Arrow Quiver"],
		"Rearguard": ["Broadhead Arrow Quiver"],
		"Maloney's Nightfall": ["Blunt Arrow Quiver"],
		"Scorpion's Call": ["Broadhead Arrow Quiver"],
		"Voidfletcher": ["Penetrating Arrow Quiver"],
		# 0 index is a bugged royale base types that are dropping live
		"Abyssus": ["Cone Helmet"],
		"Actum": ["Boarding Axe"],
		"Aurseize": ["Fishscale Gauntlets"],
		"Bloodseeker": ["Sharktooth Claw"],
		"Cloak of Defiance": ["Padded Vest"],
		"Kaom's Heart": ["War Plate"],
		"Lioneye's Paws": ["Leatherscale Boots"],
		"Martyr of Innocence": ["Long Staff"],
		"Rat's Nest": ["Leather Cap"],
		"Windripper": ["Long Bow"],
		"Lightbane Raiment": ["Chainmail Vest"],
		"Relic of the Pact": ["Carved Wand"],
		"Divinarius": ["Carving Knife"],
		"Grelwood Shank": ["Broad Sword"],
		"The Gull": ["Scare Mask"],
		"Moonbender's Wing": ["Jade Hatchet"],
	}

	keys = [
		'UniqueJewel',
		'UniqueWeapon',
		'UniqueArmour',
		'UniqueAccessory',
	]

	requester = requests.session()
	header = {
		'User-Agent': 'xan.filter',
		'From': 'xanthic42+ninja@gmail.com'
	}

	atlas_bases = {
		'UniqueArmour': {"Apothecary's Gloves", "Fingerless Silk Gloves", "Fugitive Boots", "Gripped Gloves", "Spiked Gloves", "Two-Toned Boots", "Bone Helmet", "Artillery Quiver"},
		'UniqueWeapon': {"Convoking Wand"},
		'UniqueAccessory': {"Marble Amulet", "Seaglass Amulet", "Blue Pearl Amulet", "Iolite Ring", "Vanguard Belt", "Crystal Belt", "Cerulean Ring", "Opal Ring", "Steel Ring", "Vermillion Ring"}
	}

	show_10 = {}
	unique_data = {}
	seen_all = set()
	authority_set = set()  # basetype, name, icon, key
	missing_data = {}
	for l_str, league in [
		('sct', 'Kalandra'),
		('hct', 'Hardcore Kalandra'),
		('sc', 'Standard'),
		('hc', 'Hardcore')
	]:
		show_10[l_str] = 0
		unique_data[l_str] = defaultdict(list)
		missing_data[l_str] = defaultdict(list)
		vals = defaultdict(int)
		# keep track of uniques we have seen so variants can be noticed
		seen = set()
		# check if item that is in temp standard is missing
		missing_unhandled = authority_set.copy()
		# add atlas bases as possible purchase targets for influence
		for val in atlas_bases:
			for base in atlas_bases[val]:
				unique_data[l_str][base].append(('Influenced Base', 0, 'img/influenced_base.png', val))

		for key in keys:
			request = f'https://poe.ninja/api/data/itemoverview?league={league}&type={key}'
			req = requester.get(request, headers=header)
			print(f"{league} {key} Status code: {req.status_code}")
			if req.status_code == 204:
				print("No {} data for {}".format(key, league))
				continue
			data = req.json()

			if key in {'UniqueJewel', 'UniqueWeapon', 'UniqueArmour', 'UniqueAccessory'}:
				for i in data['lines']:
					if ((('links' in i and i['links']) or 'relic' in i['icon']) and i['name'] != 'Tabula Rasa') or 'Replica' in i['name'] or i['name'] in bad_names or (i['name'] in legacy_base and i['baseType'] in legacy_base[i['name']]):
						continue
					elif i['baseType'] not in good_bases:
						print(f"Skipping due to basetype: {i}")
						continue
					elif l_str != 'sct' and (i['baseType'], i['name'], i['icon'], key) not in authority_set:
						print(f"Skipping, not in temp softcore: {i}")
						continue
					if l_str != 'sct':
						missing_unhandled.discard((i['baseType'], i['name'], i['icon'], key))
					# keep track of the 10 most expensive bases
					if vals[i['baseType']] < i['chaosValue']:
						vals[i['baseType']] = i['chaosValue']
					unique_data[l_str][i['baseType']].append((i['name'], int(i['chaosValue']), i['icon'], key))
					if l_str == 'sct':
						authority_set.add((i['baseType'], i['name'], i['icon'], key))
					if i['name'] in seen:
						seen_all.add(i['name'])
					seen.add(i['name'])

			else:
				print('Unhandled key: "{}"'.format(key))

		for item in missing_unhandled:
			unique_data[l_str][item[0]].append((item[1], 0, item[2], item[3]))
			missing_data[l_str][item[0]].append((item[1], item[2], item[3]))

		# set default value to show the 10 most valuable bases
		show_10[l_str] = int(sorted(vals.values(), reverse=True)[9])

	if seen_all:
		print(f"Variants found for the following uniques: {seen_all}")

	return show_10, unique_data,  missing_data
