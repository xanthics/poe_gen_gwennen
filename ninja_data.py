#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.7.x or higher
# Gets current price data from poe.ninja
import json
import requests
from collections import defaultdict
from gen_items import gen_bases
from datetime import datetime


# get price data from poe.ninja
def scrape_ninja():
	now = datetime.now().strftime("%Y/%m/%d, %H:%M")
	with open('last_update.py', 'w') as f:
		f.write(f'time = "{now}"')
	good_bases = [x['name'] for x in gen_bases]
	# List of items that cannot be gambled
	bad_names = {
		# Quest Items
		"Survival Instincts", "Survival Secrets", "Survival Skills", "Conqueror's Longevity", "Conqueror's Potency", "Conqueror's Efficiency",
		"Assassin's Haste", "Poacher's Aim", "Warlord's Reach",
		# Corruption only
		"Ancient Waystones", "Atziri's Reign", "Blood Sacrifice", "Brittle Barrier", "Chill of Corruption", "Combustibles", "Corrupted Energy",
		"Fragility", "Hungry Abyss", "Mutated Growth", "Pacifism", "Powerlessness", "Sacrificial Harvest", "Self-Flagellation", "Vaal Sentencing",
		"Weight of Sin", "Fevered Mind", 'Blood of Corruption', "Malachai's Vision",
		# Prophecy drop only
		'Kintsugi', "Hinekora's Sight", "Ascent From Flesh", 'The Ascetic',
		# Divination card only item
		'Maw of Mischief',
		# Fated Uniques
		'Kaltensoul', 'Thirst for Horrors', 'Atziri\'s Reflection', 'The Oak', 'Ezomyte Hold', 'Frostferno', 'Martyr\'s Crown', 'Asenath\'s Chant', 'Deidbellow',
		'Malachai\'s Awakening', 'Wall of Brambles', 'Wildwrap', 'Fox\'s Fortune', 'Crystal Vault', 'Windshriek', 'Greedtrap', 'Shavronne\'s Gambit', 'Duskblight',
		'Sunspite', 'Hrimburn', 'Doedre\'s Malevolence', 'Amplification Rod', 'Corona Solaris', 'Sanguine Gambol', 'The Gryphon', 'Dreadsurge', 'Dreadbeak', 'Cameria\'s Avarice',
		'Silverbough', 'The Tempest', 'Doomfletch\'s Prism', 'Death\'s Opus', 'Mirebough', 'Realm Ender', 'The Stormwall', 'The Cauteriser', 'Queen\'s Escape', 'The Dancing Duo',
		'Hrimnor\'s Dirge', 'Panquetzaliztli', 'Geofri\'s Devotion', 'Voidheart', 'Kaom\'s Way', 'Winterweave', 'Timetwist', 'Ngamahu Tiki', 'Karui Charge', 'The Effigon',
		'The Tactician', 'The Nomad', 'The Signal Fire', 'Cragfall', 'Hyrri\'s Demise', 'Chaber Cairn', 'Geofri\'s Legacy', 'The Iron Fortress', 'Whakatutuki o Matua',
		# Vendor recipes
		'The Anima Stone', 'Arborix', 'Duskdawn', 'The Goddess Scorned', 'The Goddess Unleashed', 'Kingmaker', 'Magna Eclipsis', 'The Retch', 'Star of Wraeclast', 'The Taming',
		'The Vinktar Square', 'Loreweave',
		#  incursion uniques from upgrades
		'Transcendent Flesh', 'Transcendent Mind', 'Transcendent Spirit', 'Soul Ripper', 'Slavedriver\'s Hand', 'Coward\'s Legacy', 'Omeyocan', 'Fate of the Vaal', 'Mask of the Stitched Demon',
		'Apep\'s Supremacy', 'Zerphi\'s Heart',
		# incursion uniques
		'Sacrificial Heart', 'String of Servitude', 'Tempered Flesh', 'Tempered Mind', 'Tempered Spirit',
		'Shadowstitch', "Apep's Slumber", "Architect's Hand", "Coward's Chains", 'Dance of the Offered', 'Mask of the Spirit Drinker', 'Story of the Vaal',
		# Upgraded Breach Uniques
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
		"Voidwalker", "Shaper's Touch", "Starforge", "Dying Sun", 'Solstice Vigil',
		"Blasphemer's Grasp", "Shimmeron", "Nebuloch", "Hopeshredder", "Impresence", "Cyclopean Coil",
		"Indigon", "The Eternity Shroud", "Disintegrator", "Voidforge", "Mark of the Elder", "Mark of the Shaper", "Voidfletcher", "Watcher's Eye",
		# Atziri
		"Atziri's Step", "Doryani's Catalyst", "Doryani's Invitation", "Atziri's Promise",
		"The Vertex", "Atziri's Splendour", "Atziri's Acuity", "Atziri's Disfavour",
		# Maven
		"Arn's Anguish", "Graven's Secret", "Olesya's Delight", "Viridi's Veil", 'The Walls', 'The Claim', 'The Closest Peak', 'Atop the Atlas', 'The Vast Horizon', 'The Builder', 'Restless Cycles', 'The False Hope', 'Legacy of Fury',
		# Bestiary League
		"Saqawal's Flock", "Saqawal's Nest", "Saqawal's Talons", "Saqawal's Winds",
		"Fenumus' Toxins", "Fenumus' Shroud", "Fenumus' Spinnerets", "Fenumus' Weave",
		"Craiceann's Chitin", "Craiceann's Carapace", "Craiceann's Tracks", "Craiceann's Pincers",
		"Farrul's Bite", "Farrul's Fur", "Farrul's Chase", "Farrul's Pounce",
		# Pale Court
		"Mind of the Council", "Grip of the Council", "Breath of the Council", "Reach of the Council",
		"Eber's Unification", "Yriel's Fostering", "Inya's Epiphany", "Volkuur's Guidance",
		# Pillars of Arun
		"Gorgon's Gaze",
		# Doryani's Machinarium
		"Doryani's Delusion",
		# Synthesis League
		"Bottled Faith", "Perepiteia", "Mask of the Tribunal", "Garb of the Ephemeral", "Offering to the Serpent", "Storm's Gift", "Nebulis", "Circle of Guilt", "Circle of Regret", "Circle of Fear", "Circle of Anguish", "Circle of Nostalgia",
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
		"Bitterbind Point", "The Devouring Diadem", "The Queen's Hunger", "Cinderswallow", "Paradoxica", "The Crimson Storm", "Hyperboreus", 'Vivinsect', "Cloak of Tawm'r Isley",
		# Perandus League
		"Seven-League Step", "Trypanon", "Umbilicus Immortalis", "Varunastra", "Zerphi's Last Breath",
		# Blight League
		"Breathstealer", "Cowl of the Ceraunophile", "Cowl of the Cryophile", "Cowl of the Thermophile", "Sporeguard", "The Stampede",
		# Conqueror
		'Booming Populace', 'Hands of the High Templar', 'Irresistable Temptation', 'Misinformation', 'Stalwart Defenders', 'Territories Unknown', 'Terror', 'The Saviour', 'Thread of Hope', 'War Among the Stars',
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
		'From': 'xanthics on discord'
	}

	for l_str, league in [('sc', 'Scourge'), ('hc', 'Hardcore Scourge')]:
		price_val = defaultdict(list)
		# add atlas bases as possible purchase targets for influence
		for base in [
			"Apothecary's Gloves", "Fingerless Silk Gloves", "Fugitive Boots", "Gripped Gloves", "Spiked Gloves", "Two-Toned Boots", "Convoking Wand", "Bone Helmet", "Artillery Quiver", "Marble Amulet",
			"Seaglass Amulet", "Blue Pearl Amulet", "Iolite Ring", "Vanguard Belt", "Crystal Belt", "Cerulean Ring", "Opal Ring", "Steel Ring", "Vermillion Ring"
		]:
			price_val[base].append(['Influenced Base', 0, 'img/influenced_base.png'])

		for key in keys:
			missing_unhandled = []
			request = f'https://poe.ninja/api/data/itemoverview?league={league}&type={key}'
			req = requester.get(request, headers=header)
			print(f"{league} {key} Status code: {req.status_code}")
			if req.status_code == 204:
				print("No {} data for {}".format(key, league))
				continue
			data = req.json()

			if key in ['UniqueJewel', 'UniqueWeapon', 'UniqueArmour', 'UniqueAccessory']:
				for i in data['lines']:
					if ((('links' in i and i['links']) or 'relic' in i['icon']) and i['name'] != 'Tabula Rasa') or 'Replica' in i['name'] or i['name'] in bad_names:
						continue
					elif i['baseType'] not in good_bases:
						print(f"Skipping due to basetype: {i}")
						continue
					price_val[i['baseType']].append([i['name'], int(i['chaosValue']), i['icon']])

			else:
				print('Unhandled key: "{}"'.format(key))

			if missing_unhandled:
				missing_str = '\n\t'.join(missing_unhandled)
				print(f"{key} is missing presets for the following items:\n\t{missing_str}")

		# sort by value decending
		for base in price_val:
			price_val[base] = sorted(price_val[base], key=lambda x: x[1], reverse=True)
		with open(f'{l_str}_unique.json', 'w') as f:
			json.dump(price_val, f, sort_keys=True, indent=2)


if __name__ == '__main__':
	scrape_ninja()
	import gen_index
	gen_index.main()
