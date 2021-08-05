#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher

bases = {
	"Weapon": {
		"Bow|Dex|Ranged|Two|Weapon": [
			{'drop': 1, 'base': 'Bow', 'name': 'Hedron Bow', 'tier': -4},  # ?
			{'drop': 1, 'base': 'Bow', 'name': 'Foundry Bow', 'tier': -4},  # ?
			{'drop': 1, 'base': 'Bow', 'name': 'Solarine Bow', 'tier': -4},  # ?
			{'drop': 1, 'base': 'Bow', 'name': 'Crude Bow', 'tier': 4},
			{'drop': 5, 'base': 'Bow', 'name': 'Short Bow', 'tier': 4},
			{'drop': 9, 'base': 'Bow', 'name': 'Long Bow', 'tier': 4},
			{'drop': 14, 'base': 'Bow', 'name': 'Composite Bow', 'tier': 4},
			{'drop': 18, 'base': 'Bow', 'name': 'Recurve Bow', 'tier': 4},
			{'drop': 23, 'base': 'Bow', 'name': 'Bone Bow', 'tier': 4},
			{'drop': 28, 'base': 'Bow', 'name': 'Royal Bow', 'tier': 4},  # Elemental Damage With Attack Skills +(20 to 24)
			{'drop': 32, 'base': 'Bow', 'name': 'Death Bow', 'tier': 4},  # Local Critical Strike Chance +(30 to 50)
			{'drop': 35, 'base': 'Bow', 'name': 'Grove Bow', 'tier': 4},
			{'drop': 36, 'base': 'Bow', 'name': 'Reflex Bow', 'tier': 4},  # Base Movement Velocity +(4)
			{'drop': 38, 'base': 'Bow', 'name': 'Decurve Bow', 'tier': 4},
			{'drop': 41, 'base': 'Bow', 'name': 'Compound Bow', 'tier': 4},
			{'drop': 44, 'base': 'Bow', 'name': 'Sniper Bow', 'tier': 4},
			{'drop': 47, 'base': 'Bow', 'name': 'Ivory Bow', 'tier': 4},
			{'drop': 50, 'base': 'Bow', 'name': 'Highborn Bow', 'tier': 4},  # Elemental Damage With Attack Skills +(20 to 24)
			{'drop': 53, 'base': 'Bow', 'name': 'Decimation Bow', 'tier': 4},  # Local Critical Strike Chance +(30 to 50)
			{'drop': 56, 'base': 'Bow', 'name': 'Thicket Bow', 'tier': 4},
			{'drop': 57, 'base': 'Bow', 'name': 'Steelwood Bow', 'tier': 4},  # Base Movement Velocity +(4)
			{'drop': 58, 'base': 'Bow', 'name': 'Citadel Bow', 'tier': 4},
			{'drop': 60, 'base': 'Bow', 'name': 'Ranger Bow', 'tier': 4},
			{'drop': 62, 'base': 'Bow', 'name': 'Assassin Bow', 'tier': 3},
			{'drop': 64, 'base': 'Bow', 'name': 'Spine Bow', 'tier': 2},
			{'drop': 66, 'base': 'Bow', 'name': 'Imperial Bow', 'tier': 1},  # Elemental Damage With Attack Skills +(20 to 24)
			{'drop': 68, 'base': 'Bow', 'name': 'Harbinger Bow', 'tier': 1},  # Local Critical Strike Chance +(30 to 50)
			{'drop': 71, 'base': 'Bow', 'name': 'Maraketh Bow', 'tier': 2},  # Base Movement Velocity +(6)
		],
		"Claw|Dex|Int|Melee|One|Weapon": [
			{'drop': 3, 'base': 'Claw', 'name': 'Nailed Fist', 'tier': 4},  # Local Life Gain Per Target (3)
			{'drop': 7, 'base': 'Claw', 'name': 'Sharktooth Claw', 'tier': 4},  # Local Life Gain Per Target (6)
			{'drop': 12, 'base': 'Claw', 'name': 'Awl', 'tier': 4},  # Local Life Gain Per Target (7)
			{'drop': 17, 'base': 'Claw', 'name': "Cat's Paw", 'tier': 4},  # Local Life Gain Per Target (8)
			{'drop': 22, 'base': 'Claw', 'name': 'Blinder', 'tier': 4},  # Local Life Gain Per Target (12)
			{'drop': 26, 'base': 'Claw', 'name': 'Timeworn Claw', 'tier': 4},  # Local Life Gain Per Target (19)
			{'drop': 30, 'base': 'Claw', 'name': 'Sparkling Claw', 'tier': 4},  # Local Life Gain Per Target (15)
			{'drop': 34, 'base': 'Claw', 'name': 'Fright Claw', 'tier': 4},  # Local Life Gain Per Target (20)
			{'drop': 36, 'base': 'Claw', 'name': 'Double Claw', 'tier': 4},  # Local Mana Gain Per Target (6), Local Life Gain Per Target (15)
			{'drop': 37, 'base': 'Claw', 'name': 'Thresher Claw', 'tier': 4},  # Local Life Gain Per Target (25)
			{'drop': 40, 'base': 'Claw', 'name': 'Gouger', 'tier': 4},  # Local Life Gain Per Target (24)
			{'drop': 43, 'base': 'Claw', 'name': "Tiger's Paw", 'tier': 4},  # Local Life Leech From Physical Damage (1.6)
			{'drop': 46, 'base': 'Claw', 'name': 'Gut Ripper', 'tier': 3},  # Local Life Gain Per Target (44)
			{'drop': 49, 'base': 'Claw', 'name': 'Prehistoric Claw', 'tier': 4},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 52, 'base': 'Claw', 'name': 'Noble Claw', 'tier': 3},  # Local Life Gain Per Target (40)
			{'drop': 55, 'base': 'Claw', 'name': 'Eagle Claw', 'tier': 4},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 57, 'base': 'Claw', 'name': 'Twin Claw', 'tier': 3},  # Local Mana Gain Per Target (10), Local Life Gain Per Target (28)
			{'drop': 58, 'base': 'Claw', 'name': 'Great White Claw', 'tier': 2},  # Local Life Gain Per Target (46)
			{'drop': 60, 'base': 'Claw', 'name': 'Throat Stabber', 'tier': 2},  # Local Life Gain Per Target (40)
			{'drop': 62, 'base': 'Claw', 'name': "Hellion's Paw", 'tier': 4},  # Local Life Leech From Physical Damage (1.6)
			{'drop': 64, 'base': 'Claw', 'name': 'Eye Gouger', 'tier': 2},  # Local Life Gain Per Target (50)
			{'drop': 66, 'base': 'Claw', 'name': 'Vaal Claw', 'tier': 3},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 68, 'base': 'Claw', 'name': 'Imperial Claw', 'tier': 1},  # Local Life Gain Per Target (46)
			{'drop': 70, 'base': 'Claw', 'name': 'Terror Claw', 'tier': 3},  # Local Life Leech From Physical Damage (2.0)
			{'drop': 72, 'base': 'Claw', 'name': 'Gemini Claw', 'tier': 1},  # Local Mana Gain Per Target (14), Local Life Gain Per Target (38)
		],
		"Dagger|Dex|Int|Melee|One|Weapon": [
			{'drop': 1, 'base': 'Dagger', 'name': 'Glass Shank', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 5, 'base': 'Dagger', 'name': 'Skinning Knife', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 15, 'base': 'Dagger', 'name': 'Stiletto', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 35, 'base': 'Dagger', 'name': 'Flaying Knife', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 36, 'base': 'Dagger', 'name': 'Prong Dagger', 'tier': 4},  # Monster Base Block (4)
			{'drop': 41, 'base': 'Dagger', 'name': 'Poignard', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 55, 'base': 'Dagger', 'name': 'Trisula', 'tier': 4},  # Monster Base Block (4)
			{'drop': 56, 'base': 'Dagger', 'name': 'Gutting Knife', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 60, 'base': 'Dagger', 'name': 'Ambusher', 'tier': 3},  # Critical Strike Chance +(30)
			{'drop': 70, 'base': 'Dagger', 'name': 'Sai', 'tier': 2},  # Monster Base Block (6)
		],
		"Caster|Rune Daggers|Dex|Int|Melee|One|Weapon": [
			{'drop': 1, 'base': 'Rune Daggers', 'name': 'Flickerflame Blade', 'tier': -4},  # Critical Strike Chance +(30)
			{'drop': 1, 'base': 'Rune Daggers', 'name': 'Flashfire Blade', 'tier': -4},  # Critical Strike Chance +(30)
			{'drop': 1, 'base': 'Rune Daggers', 'name': 'Infernal Blade', 'tier': -4},  # Critical Strike Chance +(30)
			{'drop': 10, 'base': 'Rune Daggers', 'name': 'Carving Knife', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 20, 'base': 'Rune Daggers', 'name': 'Boot Knife', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 24, 'base': 'Rune Daggers', 'name': 'Copper Kris', 'tier': 3},  # Critical Strike Chance +(50)
			{'drop': 28, 'base': 'Rune Daggers', 'name': 'Skean', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 32, 'base': 'Rune Daggers', 'name': 'Imp Dagger', 'tier': 4},  # Critical Strike Chance +(40)
			{'drop': 38, 'base': 'Rune Daggers', 'name': 'Butcher Knife', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 44, 'base': 'Rune Daggers', 'name': 'Boot Blade', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 47, 'base': 'Rune Daggers', 'name': 'Golden Kris', 'tier': 3},  # Critical Strike Chance +(50)
			{'drop': 50, 'base': 'Rune Daggers', 'name': 'Royal Skean', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 53, 'base': 'Rune Daggers', 'name': 'Fiend Dagger', 'tier': 4},  # Critical Strike Chance +(40)
			{'drop': 58, 'base': 'Rune Daggers', 'name': 'Slaughter Knife', 'tier': 4},  # Critical Strike Chance +(30)
			{'drop': 62, 'base': 'Rune Daggers', 'name': 'Ezomyte Dagger', 'tier': 2},  # Critical Strike Chance +(30)
			{'drop': 64, 'base': 'Rune Daggers', 'name': 'Platinum Kris', 'tier': 1},  # Critical Strike Chance +(50)
			{'drop': 66, 'base': 'Rune Daggers', 'name': 'Imperial Skean', 'tier': 2},  # Critical Strike Chance +(30)
			{'drop': 68, 'base': 'Rune Daggers', 'name': 'Demon Dagger', 'tier': 1},  # Critical Strike Chance +(40)
		],
		"Dex|Melee|One|One Hand Axe|Str|Weapon": [
			{'drop': 2, 'base': 'One Hand Axe', 'name': 'Rusted Hatchet', 'tier': 4},
			{'drop': 6, 'base': 'One Hand Axe', 'name': 'Jade Hatchet', 'tier': 4},
			{'drop': 11, 'base': 'One Hand Axe', 'name': 'Boarding Axe', 'tier': 4},
			{'drop': 16, 'base': 'One Hand Axe', 'name': 'Cleaver', 'tier': 4},
			{'drop': 21, 'base': 'One Hand Axe', 'name': 'Broad Axe', 'tier': 4},
			{'drop': 25, 'base': 'One Hand Axe', 'name': 'Arming Axe', 'tier': 4},
			{'drop': 29, 'base': 'One Hand Axe', 'name': 'Decorative Axe', 'tier': 4},
			{'drop': 33, 'base': 'One Hand Axe', 'name': 'Spectral Axe', 'tier': 4},
			{'drop': 35, 'base': 'One Hand Axe', 'name': 'Etched Hatchet', 'tier': 4},  # Physical Damage +(8)
			{'drop': 36, 'base': 'One Hand Axe', 'name': 'Jasper Axe', 'tier': 4},
			{'drop': 39, 'base': 'One Hand Axe', 'name': 'Tomahawk', 'tier': 4},
			{'drop': 42, 'base': 'One Hand Axe', 'name': 'Wrist Chopper', 'tier': 4},
			{'drop': 45, 'base': 'One Hand Axe', 'name': 'War Axe', 'tier': 4},
			{'drop': 48, 'base': 'One Hand Axe', 'name': 'Chest Splitter', 'tier': 4},
			{'drop': 51, 'base': 'One Hand Axe', 'name': 'Ceremonial Axe', 'tier': 4},
			{'drop': 54, 'base': 'One Hand Axe', 'name': 'Wraith Axe', 'tier': 4},
			{'drop': 56, 'base': 'One Hand Axe', 'name': 'Engraved Hatchet', 'tier': 4},  # Physical Damage +(8)
			{'drop': 57, 'base': 'One Hand Axe', 'name': 'Karui Axe', 'tier': 4},
			{'drop': 59, 'base': 'One Hand Axe', 'name': 'Siege Axe', 'tier': 1},
			{'drop': 61, 'base': 'One Hand Axe', 'name': 'Reaver Axe', 'tier': 4},
			{'drop': 63, 'base': 'One Hand Axe', 'name': 'Butcher Axe', 'tier': 4},
			{'drop': 65, 'base': 'One Hand Axe', 'name': 'Vaal Hatchet', 'tier': 1},
			{'drop': 67, 'base': 'One Hand Axe', 'name': 'Royal Axe', 'tier': 3},
			{'drop': 69, 'base': 'One Hand Axe', 'name': 'Infernal Axe', 'tier': 3},
			{'drop': 71, 'base': 'One Hand Axe', 'name': 'Runic Hatchet', 'tier': 2},  # Physical Damage +(12)
		],
		"Melee|One|One Hand Mace|Str|Weapon": [
			{'drop': 1, 'base': 'One Hand Mace', 'name': 'Driftwood Club', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 5, 'base': 'One Hand Mace', 'name': 'Tribal Club', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 10, 'base': 'One Hand Mace', 'name': 'Spiked Club', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 15, 'base': 'One Hand Mace', 'name': 'Stone Hammer', 'tier': 4},  # Base Stun Threshold Reduction +(15)
			{'drop': 20, 'base': 'One Hand Mace', 'name': 'War Hammer', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 24, 'base': 'One Hand Mace', 'name': 'Bladed Mace', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 28, 'base': 'One Hand Mace', 'name': 'Ceremonial Mace', 'tier': 4},  # Base Stun Threshold Reduction +(15)
			{'drop': 32, 'base': 'One Hand Mace', 'name': 'Dream Mace', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 34, 'base': 'One Hand Mace', 'name': 'Wyrm Mace', 'tier': 4},  # Local Attack Speed +(4)
			{'drop': 35, 'base': 'One Hand Mace', 'name': 'Petrified Club', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 38, 'base': 'One Hand Mace', 'name': 'Barbed Club', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 41, 'base': 'One Hand Mace', 'name': 'Rock Breaker', 'tier': 4},  # Base Stun Threshold Reduction +(15)
			{'drop': 44, 'base': 'One Hand Mace', 'name': 'Battle Hammer', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 47, 'base': 'One Hand Mace', 'name': 'Flanged Mace', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 50, 'base': 'One Hand Mace', 'name': 'Ornate Mace', 'tier': 4},  # Base Stun Threshold Reduction +(15)
			{'drop': 53, 'base': 'One Hand Mace', 'name': 'Phantom Mace', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 55, 'base': 'One Hand Mace', 'name': 'Dragon Mace', 'tier': 4},  # Local Attack Speed +(4)
			{'drop': 56, 'base': 'One Hand Mace', 'name': 'Ancestral Club', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 58, 'base': 'One Hand Mace', 'name': 'Tenderizer', 'tier': 4},  # Base Stun Threshold Reduction +(10)
			{'drop': 60, 'base': 'One Hand Mace', 'name': 'Gavel', 'tier': 4},  # Base Stun Threshold Reduction +(15)
			{'drop': 62, 'base': 'One Hand Mace', 'name': 'Legion Hammer', 'tier': 2},  # Base Stun Threshold Reduction +(10)
			{'drop': 64, 'base': 'One Hand Mace', 'name': 'Pernach', 'tier': 3},  # Base Stun Threshold Reduction +(10)
			{'drop': 66, 'base': 'One Hand Mace', 'name': 'Auric Mace', 'tier': 4},  # Base Stun Threshold Reduction +(15)
			{'drop': 68, 'base': 'One Hand Mace', 'name': 'Nightmare Mace', 'tier': 2},  # Base Stun Threshold Reduction +(10)
			{'drop': 70, 'base': 'One Hand Mace', 'name': 'Behemoth Mace', 'tier': 1},  # Local Attack Speed +(6)
		],
		"Dex|Melee|One|One Hand Sword|Str|Weapon": [
			{'drop': 1, 'base': 'One Hand Sword', 'name': 'Rusted Sword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 5, 'base': 'One Hand Sword', 'name': 'Copper Sword', 'tier': 4},  # Local Accuracy Rating (45)
			{'drop': 10, 'base': 'One Hand Sword', 'name': 'Sabre', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 15, 'base': 'One Hand Sword', 'name': 'Broad Sword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 20, 'base': 'One Hand Sword', 'name': 'War Sword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 24, 'base': 'One Hand Sword', 'name': 'Ancient Sword', 'tier': 4},  # Local Accuracy Rating (165)
			{'drop': 28, 'base': 'One Hand Sword', 'name': 'Elegant Sword', 'tier': 4},  # Local Accuracy Rating (190)
			{'drop': 32, 'base': 'One Hand Sword', 'name': 'Dusk Blade', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 34, 'base': 'One Hand Sword', 'name': 'Hook Sword', 'tier': 4},  # Base Chance To Dodge (4)
			{'drop': 35, 'base': 'One Hand Sword', 'name': 'Variscite Blade', 'tier': 4},  # Local Accuracy Rating (240)
			{'drop': 38, 'base': 'One Hand Sword', 'name': 'Cutlass', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 41, 'base': 'One Hand Sword', 'name': 'Baselard', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 44, 'base': 'One Hand Sword', 'name': 'Battle Sword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 47, 'base': 'One Hand Sword', 'name': 'Elder Sword', 'tier': 4},  # Local Accuracy Rating (330)
			{'drop': 50, 'base': 'One Hand Sword', 'name': 'Graceful Sword', 'tier': 4},  # Local Accuracy Rating (350)
			{'drop': 53, 'base': 'One Hand Sword', 'name': 'Twilight Blade', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 55, 'base': 'One Hand Sword', 'name': 'Grappler', 'tier': 4},  # Base Chance To Dodge (4)
			{'drop': 56, 'base': 'One Hand Sword', 'name': 'Gemstone Sword', 'tier': 4},  # Local Accuracy Rating (400)
			{'drop': 58, 'base': 'One Hand Sword', 'name': 'Corsair Sword', 'tier': 1},  # Local Accuracy Rating +(40)
			{'drop': 60, 'base': 'One Hand Sword', 'name': 'Gladius', 'tier': 3},  # Local Accuracy Rating +(40)
			{'drop': 62, 'base': 'One Hand Sword', 'name': 'Legion Sword', 'tier': 3},  # Local Accuracy Rating +(40)
			{'drop': 64, 'base': 'One Hand Sword', 'name': 'Vaal Blade', 'tier': 2},  # Local Accuracy Rating (460)
			{'drop': 66, 'base': 'One Hand Sword', 'name': 'Eternal Sword', 'tier': 1},  # Local Accuracy Rating (475)
			{'drop': 68, 'base': 'One Hand Sword', 'name': 'Midnight Blade', 'tier': 2},  # Local Accuracy Rating +(40)
			{'drop': 70, 'base': 'One Hand Sword', 'name': 'Tiger Hook', 'tier': 3},  # Base Chance To Dodge (6)
		],
		"Caster|Int|Melee|One|Sceptre|Str|Weapon": [
			{'drop': 1, 'base': 'Sceptre', 'name': 'Driftwood Sceptre', 'tier': 4},  # Elemental Damage +(10)
			{'drop': 5, 'base': 'Sceptre', 'name': 'Darkwood Sceptre', 'tier': 4},  # Elemental Damage +(12)
			{'drop': 10, 'base': 'Sceptre', 'name': 'Bronze Sceptre', 'tier': 4},  # Elemental Damage +(12)
			{'drop': 15, 'base': 'Sceptre', 'name': 'Quartz Sceptre', 'tier': 4},  # Elemental Damage +(20)
			{'drop': 20, 'base': 'Sceptre', 'name': 'Iron Sceptre', 'tier': 4},  # Elemental Damage +(14)
			{'drop': 24, 'base': 'Sceptre', 'name': 'Ochre Sceptre', 'tier': 4},  # Elemental Damage +(16)
			{'drop': 28, 'base': 'Sceptre', 'name': 'Ritual Sceptre', 'tier': 4},  # Elemental Damage +(16)
			{'drop': 32, 'base': 'Sceptre', 'name': 'Shadow Sceptre', 'tier': 4},  # Elemental Damage +(22)
			{'drop': 35, 'base': 'Sceptre', 'name': 'Grinning Fetish', 'tier': 4},  # Elemental Damage +(18)
			{'drop': 36, 'base': 'Sceptre', 'name': 'Horned Sceptre', 'tier': 3},  # Reduce Enemy Elemental Resistance (4)
			{'drop': 38, 'base': 'Sceptre', 'name': 'Sekhem', 'tier': 4},  # Elemental Damage +(18)
			{'drop': 41, 'base': 'Sceptre', 'name': 'Crystal Sceptre', 'tier': 4},  # Elemental Damage +(30)
			{'drop': 44, 'base': 'Sceptre', 'name': 'Lead Sceptre', 'tier': 4},  # Elemental Damage +(22)
			{'drop': 47, 'base': 'Sceptre', 'name': 'Blood Sceptre', 'tier': 4},  # Elemental Damage +(24)
			{'drop': 50, 'base': 'Sceptre', 'name': 'Royal Sceptre', 'tier': 4},  # Elemental Damage +(24)
			{'drop': 53, 'base': 'Sceptre', 'name': 'Abyssal Sceptre', 'tier': 3},  # Elemental Damage +(30)
			{'drop': 55, 'base': 'Sceptre', 'name': 'Stag Sceptre', 'tier': 3},  # Reduce Enemy Elemental Resistance (4)
			{'drop': 56, 'base': 'Sceptre', 'name': 'Karui Sceptre', 'tier': 4},  # Elemental Damage +(26)
			{'drop': 58, 'base': 'Sceptre', 'name': "Tyrant's Sekhem", 'tier': 4},  # Elemental Damage +(26)
			{'drop': 60, 'base': 'Sceptre', 'name': 'Opal Sceptre', 'tier': 1},  # Elemental Damage +(40)
			{'drop': 62, 'base': 'Sceptre', 'name': 'Platinum Sceptre', 'tier': 3},  # Elemental Damage +(30)
			{'drop': 64, 'base': 'Sceptre', 'name': 'Vaal Sceptre', 'tier': 2},  # Elemental Damage +(32)
			{'drop': 66, 'base': 'Sceptre', 'name': 'Carnal Sceptre', 'tier': 2},  # Elemental Damage +(32)
			{'drop': 68, 'base': 'Sceptre', 'name': 'Void Sceptre', 'tier': 1},  # Elemental Damage +(40)
			{'drop': 70, 'base': 'Sceptre', 'name': 'Sambar Sceptre', 'tier': 1},  # Reduce Enemy Elemental Resistance (6)
		],
		"Int|Melee|Warstaves|Str|Two|Weapon": [
			{'drop': 18, 'base': 'Warstaves', 'name': 'Iron Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 23, 'base': 'Warstaves', 'name': 'Coiled Staff', 'tier': 4},  # Staff Block (20)
			{'drop': 33, 'base': 'Warstaves', 'name': 'Vile Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 45, 'base': 'Warstaves', 'name': 'Military Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 49, 'base': 'Warstaves', 'name': 'Serpentine Staff', 'tier': 4},  # Staff Block (20)
			{'drop': 55, 'base': 'Warstaves', 'name': 'Foul Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 62, 'base': 'Warstaves', 'name': 'Ezomyte Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 64, 'base': 'Warstaves', 'name': 'Maelström Staff', 'tier': 3},  # Staff Block (20)
			{'drop': 68, 'base': 'Warstaves', 'name': 'Judgement Staff', 'tier': 2},  # Staff Block (18)
		],
		"Caster|Int|Melee|Stave|Str|Two|Weapon": [
			{'drop': 4, 'base': 'Stave', 'name': 'Gnarled Branch', 'tier': 4},  # Staff Block (18)
			{'drop': 9, 'base': 'Stave', 'name': 'Primitive Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 13, 'base': 'Stave', 'name': 'Long Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 28, 'base': 'Stave', 'name': 'Royal Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 36, 'base': 'Stave', 'name': 'Crescent Staff', 'tier': 2},  # Critical Strike Chance +(80)
			{'drop': 37, 'base': 'Stave', 'name': 'Woodful Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 41, 'base': 'Stave', 'name': 'Quarterstaff', 'tier': 4},  # Staff Block (18)
			{'drop': 52, 'base': 'Stave', 'name': 'Highborn Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 57, 'base': 'Stave', 'name': 'Moon Staff', 'tier': 2},  # Critical Strike Chance +(80)
			{'drop': 58, 'base': 'Stave', 'name': 'Primordial Staff', 'tier': 4},  # Staff Block (18)
			{'drop': 60, 'base': 'Stave', 'name': 'Lathi', 'tier': 4},  # Staff Block (18)
			{'drop': 66, 'base': 'Stave', 'name': 'Imperial Staff', 'tier': 3},  # Staff Block (18)
			{'drop': 70, 'base': 'Stave', 'name': 'Eclipse Staff', 'tier': 1},  # Critical Strike Chance +(100)
		],
		"Dex|Melee|One|Thrusting One Hand Sword|Weapon": [
			{'drop': 3, 'base': 'Thrusting One Hand Sword', 'name': 'Rusted Spike', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 7, 'base': 'Thrusting One Hand Sword', 'name': 'Whalebone Rapier', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 12, 'base': 'Thrusting One Hand Sword', 'name': 'Battered Foil', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 17, 'base': 'Thrusting One Hand Sword', 'name': 'Basket Rapier', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 22, 'base': 'Thrusting One Hand Sword', 'name': 'Jagged Foil', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 26, 'base': 'Thrusting One Hand Sword', 'name': 'Antique Rapier', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 30, 'base': 'Thrusting One Hand Sword', 'name': 'Elegant Foil', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 34, 'base': 'Thrusting One Hand Sword', 'name': 'Thorn Rapier', 'tier': 3},  # Base Critical Strike Multiplier +(35)
			{'drop': 36, 'base': 'Thrusting One Hand Sword', 'name': 'Smallsword', 'tier': 4},  # Local Chance To Bleed On Hit (15)
			{'drop': 37, 'base': 'Thrusting One Hand Sword', 'name': 'Wyrmbone Rapier', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 40, 'base': 'Thrusting One Hand Sword', 'name': 'Burnished Foil', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 43, 'base': 'Thrusting One Hand Sword', 'name': 'Estoc', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 46, 'base': 'Thrusting One Hand Sword', 'name': 'Serrated Foil', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 49, 'base': 'Thrusting One Hand Sword', 'name': 'Primeval Rapier', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 52, 'base': 'Thrusting One Hand Sword', 'name': 'Fancy Foil', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 55, 'base': 'Thrusting One Hand Sword', 'name': 'Apex Rapier', 'tier': 3},  # Base Critical Strike Multiplier +(35)
			{'drop': 57, 'base': 'Thrusting One Hand Sword', 'name': 'Courtesan Sword', 'tier': 4},  # Local Chance To Bleed On Hit (15)
			{'drop': 58, 'base': 'Thrusting One Hand Sword', 'name': 'Dragonbone Rapier', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 60, 'base': 'Thrusting One Hand Sword', 'name': 'Tempered Foil', 'tier': 4},  # Base Critical Strike Multiplier +(25)
			{'drop': 62, 'base': 'Thrusting One Hand Sword', 'name': 'Pecoraro', 'tier': 3},  # Base Critical Strike Multiplier +(25)
			{'drop': 64, 'base': 'Thrusting One Hand Sword', 'name': 'Spiraled Foil', 'tier': 2},  # Base Critical Strike Multiplier +(25)
			{'drop': 66, 'base': 'Thrusting One Hand Sword', 'name': 'Vaal Rapier', 'tier': 3},  # Base Critical Strike Multiplier +(25)
			{'drop': 68, 'base': 'Thrusting One Hand Sword', 'name': 'Jewelled Foil', 'tier': 1},  # Base Critical Strike Multiplier +(25)
			{'drop': 70, 'base': 'Thrusting One Hand Sword', 'name': 'Harpy Rapier', 'tier': 1},  # Base Critical Strike Multiplier +(35)
			{'drop': 72, 'base': 'Thrusting One Hand Sword', 'name': 'Dragoon Sword', 'tier': 3},  # Local Chance To Bleed On Hit (20)
		],
		"Dex|Melee|Str|Two|Two Hand Axe|Weapon": [
			{'drop': 4, 'base': 'Two Hand Axe', 'name': 'Stone Axe', 'tier': 4},
			{'drop': 9, 'base': 'Two Hand Axe', 'name': 'Jade Chopper', 'tier': 4},
			{'drop': 13, 'base': 'Two Hand Axe', 'name': 'Woodsplitter', 'tier': 4},
			{'drop': 18, 'base': 'Two Hand Axe', 'name': 'Poleaxe', 'tier': 4},
			{'drop': 23, 'base': 'Two Hand Axe', 'name': 'Double Axe', 'tier': 4},
			{'drop': 28, 'base': 'Two Hand Axe', 'name': 'Gilded Axe', 'tier': 4},
			{'drop': 33, 'base': 'Two Hand Axe', 'name': 'Shadow Axe', 'tier': 4},
			{'drop': 36, 'base': 'Two Hand Axe', 'name': 'Dagger Axe', 'tier': 4},  # Local Critical Strike Chance +(50)
			{'drop': 37, 'base': 'Two Hand Axe', 'name': 'Jasper Chopper', 'tier': 4},
			{'drop': 41, 'base': 'Two Hand Axe', 'name': 'Timber Axe', 'tier': 4},
			{'drop': 45, 'base': 'Two Hand Axe', 'name': 'Headsman Axe', 'tier': 4},
			{'drop': 49, 'base': 'Two Hand Axe', 'name': 'Labrys', 'tier': 4},
			{'drop': 52, 'base': 'Two Hand Axe', 'name': 'Noble Axe', 'tier': 4},
			{'drop': 55, 'base': 'Two Hand Axe', 'name': 'Abyssal Axe', 'tier': 4},
			{'drop': 58, 'base': 'Two Hand Axe', 'name': 'Karui Chopper', 'tier': 4},
			{'drop': 59, 'base': 'Two Hand Axe', 'name': 'Talon Axe', 'tier': 3},  # Local Critical Strike Chance +(50)
			{'drop': 60, 'base': 'Two Hand Axe', 'name': 'Sundering Axe', 'tier': 3},
			{'drop': 62, 'base': 'Two Hand Axe', 'name': 'Ezomyte Axe', 'tier': 3},
			{'drop': 64, 'base': 'Two Hand Axe', 'name': 'Vaal Axe', 'tier': 1},
			{'drop': 66, 'base': 'Two Hand Axe', 'name': 'Despot Axe', 'tier': 2},
			{'drop': 68, 'base': 'Two Hand Axe', 'name': 'Void Axe', 'tier': 2},
			{'drop': 70, 'base': 'Two Hand Axe', 'name': 'Fleshripper', 'tier': 1},  # Local Critical Strike Chance +(50)
		],
		"Melee|Str|Two|Two Hand Mace|Weapon": [
			{'drop': 3, 'base': 'Two Hand Mace', 'name': 'Driftwood Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 8, 'base': 'Two Hand Mace', 'name': 'Tribal Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 12, 'base': 'Two Hand Mace', 'name': 'Mallet', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 17, 'base': 'Two Hand Mace', 'name': 'Sledgehammer', 'tier': 4},  # Base Stun Duration +(45)
			{'drop': 22, 'base': 'Two Hand Mace', 'name': 'Jagged Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 27, 'base': 'Two Hand Mace', 'name': 'Brass Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 32, 'base': 'Two Hand Mace', 'name': 'Fright Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 34, 'base': 'Two Hand Mace', 'name': 'Morning Star', 'tier': 4},  # Base Skill Area Of Effect +(4)
			{'drop': 36, 'base': 'Two Hand Mace', 'name': 'Totemic Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 40, 'base': 'Two Hand Mace', 'name': 'Great Mallet', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 44, 'base': 'Two Hand Mace', 'name': 'Steelhead', 'tier': 4},  # Base Stun Duration +(45)
			{'drop': 48, 'base': 'Two Hand Mace', 'name': 'Spiny Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 51, 'base': 'Two Hand Mace', 'name': 'Plated Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 54, 'base': 'Two Hand Mace', 'name': 'Dread Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 56, 'base': 'Two Hand Mace', 'name': 'Solar Maul', 'tier': 4},  # Base Skill Area Of Effect +(4)
			{'drop': 57, 'base': 'Two Hand Mace', 'name': 'Karui Maul', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 59, 'base': 'Two Hand Mace', 'name': 'Colossus Mallet', 'tier': 4},  # Base Stun Duration +(30)
			{'drop': 61, 'base': 'Two Hand Mace', 'name': 'Piledriver', 'tier': 3},  # Base Stun Duration +(45)
			{'drop': 63, 'base': 'Two Hand Mace', 'name': 'Meatgrinder', 'tier': 3},  # Base Stun Duration +(30)
			{'drop': 65, 'base': 'Two Hand Mace', 'name': 'Imperial Maul', 'tier': 2},  # Base Stun Duration +(30)
			{'drop': 67, 'base': 'Two Hand Mace', 'name': 'Terror Maul', 'tier': 2},  # Base Stun Duration +(30)
			{'drop': 69, 'base': 'Two Hand Mace', 'name': 'Coronal Maul', 'tier': 1},  # Base Skill Area Of Effect +(6)
		],
		"Dex|Melee|Str|Two|Two Hand Sword|Weapon": [
			{'drop': 3, 'base': 'Two Hand Sword', 'name': 'Corroded Blade', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 8, 'base': 'Two Hand Sword', 'name': 'Longsword', 'tier': 4},  # Local Accuracy Rating (60)
			{'drop': 12, 'base': 'Two Hand Sword', 'name': 'Bastard Sword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 17, 'base': 'Two Hand Sword', 'name': 'Two-Handed Sword', 'tier': 4},  # Local Accuracy Rating (120)
			{'drop': 22, 'base': 'Two Hand Sword', 'name': 'Etched Greatsword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 27, 'base': 'Two Hand Sword', 'name': 'Ornate Sword', 'tier': 4},  # Local Accuracy Rating (185)
			{'drop': 32, 'base': 'Two Hand Sword', 'name': 'Spectral Sword', 'tier': 4},  # Local Accuracy Rating +(30)
			{'drop': 35, 'base': 'Two Hand Sword', 'name': 'Curved Blade', 'tier': 4},  # Base Critical Strike Multiplier +(40)
			{'drop': 36, 'base': 'Two Hand Sword', 'name': 'Butcher Sword', 'tier': 4},  # Local Accuracy Rating (250)
			{'drop': 40, 'base': 'Two Hand Sword', 'name': 'Footman Sword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 44, 'base': 'Two Hand Sword', 'name': 'Highland Blade', 'tier': 4},  # Local Accuracy Rating (305)
			{'drop': 48, 'base': 'Two Hand Sword', 'name': 'Engraved Greatsword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 51, 'base': 'Two Hand Sword', 'name': 'Tiger Sword', 'tier': 4},  # Local Accuracy Rating (360)
			{'drop': 54, 'base': 'Two Hand Sword', 'name': 'Wraith Sword', 'tier': 4},  # Local Accuracy Rating +(30)
			{'drop': 56, 'base': 'Two Hand Sword', 'name': 'Lithe Blade', 'tier': 4},  # Base Critical Strike Multiplier +(40)
			{'drop': 57, 'base': 'Two Hand Sword', 'name': "Headman's Sword", 'tier': 4},  # Local Accuracy Rating (400)
			{'drop': 59, 'base': 'Two Hand Sword', 'name': 'Reaver Sword', 'tier': 3},  # Local Accuracy Rating +(40)
			{'drop': 61, 'base': 'Two Hand Sword', 'name': 'Ezomyte Blade', 'tier': 4},  # Local Accuracy Rating (435)
			{'drop': 63, 'base': 'Two Hand Sword', 'name': 'Vaal Greatsword', 'tier': 4},  # Local Accuracy Rating +(40)
			{'drop': 65, 'base': 'Two Hand Sword', 'name': 'Lion Sword', 'tier': 3},  # Local Accuracy Rating (470)
			{'drop': 67, 'base': 'Two Hand Sword', 'name': 'Infernal Sword', 'tier': 4},  # Local Accuracy Rating +(30)
			{'drop': 70, 'base': 'Two Hand Sword', 'name': 'Exquisite Blade', 'tier': 1},  # Base Critical Strike Multiplier +(60)
		],
		"Caster|Int|One|Ranged|Wand|Weapon": [
			{'drop': 6, 'base': 'Wand', 'name': "Goat's Horn", 'tier': 4},  # Spell Damage +(10 to 14)
			{'drop': 12, 'base': 'Wand', 'name': 'Carved Wand', 'tier': 4},  # Spell Damage +(11 to 15)
			{'drop': 18, 'base': 'Wand', 'name': 'Quartz Wand', 'tier': 4},  # Spell Damage +(18 to 22)
			{'drop': 24, 'base': 'Wand', 'name': 'Spiraled Wand', 'tier': 4},  # Spell Damage +(15 to 19)
			{'drop': 30, 'base': 'Wand', 'name': 'Sage Wand', 'tier': 4},  # Spell Damage +(17 to 21)
			{'drop': 34, 'base': 'Wand', 'name': 'Pagan Wand', 'tier': 3},  # Cast Speed +(10)
			{'drop': 35, 'base': 'Wand', 'name': "Faun's Horn", 'tier': 4},  # Spell Damage +(20 to 24)
			{'drop': 40, 'base': 'Wand', 'name': 'Engraved Wand', 'tier': 4},  # Spell Damage +(22 to 26)
			{'drop': 45, 'base': 'Wand', 'name': 'Crystal Wand', 'tier': 3},  # Spell Damage +(29 to 33)
			{'drop': 49, 'base': 'Wand', 'name': 'Serpent Wand', 'tier': 4},  # Spell Damage +(26 to 30)
			{'drop': 53, 'base': 'Wand', 'name': 'Omen Wand', 'tier': 4},  # Spell Damage +(27 to 31)
			{'drop': 55, 'base': 'Wand', 'name': 'Heathen Wand', 'tier': 3},  # Cast Speed +(10)
			{'drop': 56, 'base': 'Wand', 'name': "Demon's Horn", 'tier': 2},  # Spell Damage +(31 to 35)
			{'drop': 59, 'base': 'Wand', 'name': 'Imbued Wand', 'tier': 2},  # Spell Damage +(33 to 37)
			{'drop': 62, 'base': 'Wand', 'name': 'Opal Wand', 'tier': 1},  # Spell Damage +(38 to 42)
			{'drop': 65, 'base': 'Wand', 'name': 'Tornado Wand', 'tier': 2},  # Spell Damage +(35 to 39)
			{'drop': 68, 'base': 'Wand', 'name': 'Prophecy Wand', 'tier': 2},  # Spell Damage +(36 to 40)
			{'drop': 70, 'base': 'Wand', 'name': 'Profane Wand', 'tier': 1},  # Cast Speed +(14)
		],
	},
	"Armour": {
		"Armour|Body Armour|Str": [
			{'drop': 1, 'base': 'Body Armour', 'name': 'Plate Vest', 'tier': 4},
			{'drop': 6, 'base': 'Body Armour', 'name': 'Chestplate', 'tier': 4},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Copper Plate', 'tier': 4},
			{'drop': 21, 'base': 'Body Armour', 'name': 'War Plate', 'tier': 4},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Plate', 'tier': 4},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Arena Plate', 'tier': 4},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Lordly Plate', 'tier': 4},
			{'drop': 37, 'base': 'Body Armour', 'name': 'Bronze Plate', 'tier': 4},
			{'drop': 41, 'base': 'Body Armour', 'name': 'Battle Plate', 'tier': 4},
			{'drop': 45, 'base': 'Body Armour', 'name': 'Sun Plate', 'tier': 4},
			{'drop': 49, 'base': 'Body Armour', 'name': 'Colosseum Plate', 'tier': 4},
			{'drop': 53, 'base': 'Body Armour', 'name': 'Majestic Plate', 'tier': 4},
			{'drop': 56, 'base': 'Body Armour', 'name': 'Golden Plate', 'tier': 3},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Crusader Plate', 'tier': 3},
			{'drop': 62, 'base': 'Body Armour', 'name': 'Astral Plate', 'tier': 0},  # Resist all Elements (8 to 12)
			{'drop': 65, 'base': 'Body Armour', 'name': 'Gladiator Plate', 'tier': 2},
			{'drop': 68, 'base': 'Body Armour', 'name': 'Glorious Plate', 'tier': 1},
		],
		"Armour|Body Armour|Dex": [
			{'drop': 2, 'base': 'Body Armour', 'name': 'Shabby Jerkin', 'tier': 4},
			{'drop': 9, 'base': 'Body Armour', 'name': 'Strapped Leather', 'tier': 4},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Buckskin Tunic', 'tier': 4},
			{'drop': 25, 'base': 'Body Armour', 'name': 'Wild Leather', 'tier': 4},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Leather', 'tier': 4},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Sun Leather', 'tier': 4},
			{'drop': 35, 'base': 'Body Armour', 'name': "Thief's Garb", 'tier': 4},
			{'drop': 37, 'base': 'Body Armour', 'name': 'Eelskin Tunic', 'tier': 4},
			{'drop': 41, 'base': 'Body Armour', 'name': 'Frontier Leather', 'tier': 4},
			{'drop': 45, 'base': 'Body Armour', 'name': 'Glorious Leather', 'tier': 4},
			{'drop': 49, 'base': 'Body Armour', 'name': 'Coronal Leather', 'tier': 4},
			{'drop': 53, 'base': 'Body Armour', 'name': "Cutthroat's Garb", 'tier': 4},
			{'drop': 56, 'base': 'Body Armour', 'name': 'Sharkskin Tunic', 'tier': 4},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Destiny Leather', 'tier': 3},
			{'drop': 62, 'base': 'Body Armour', 'name': 'Exquisite Leather', 'tier': 2},
			{'drop': 65, 'base': 'Body Armour', 'name': 'Zodiac Leather', 'tier': 1},
			{'drop': 68, 'base': 'Body Armour', 'name': "Assassin's Garb", 'tier': 1},  # Base Movement Velocity +(3)
		],
		"Armour|Body Armour|Int": [
			{'drop': 3, 'base': 'Body Armour', 'name': 'Simple Robe', 'tier': 4},
			{'drop': 11, 'base': 'Body Armour', 'name': 'Silken Vest', 'tier': 4},
			{'drop': 18, 'base': 'Body Armour', 'name': "Scholar's Robe", 'tier': 4},
			{'drop': 25, 'base': 'Body Armour', 'name': 'Silken Garb', 'tier': 4},
			{'drop': 28, 'base': 'Body Armour', 'name': "Mage's Vestment", 'tier': 4},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Silk Robe', 'tier': 4},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Cabalist Regalia', 'tier': 4},
			{'drop': 37, 'base': 'Body Armour', 'name': "Sage's Robe", 'tier': 4},
			{'drop': 41, 'base': 'Body Armour', 'name': 'Silken Wrap', 'tier': 4},
			{'drop': 45, 'base': 'Body Armour', 'name': "Conjurer's Vestment", 'tier': 4},
			{'drop': 49, 'base': 'Body Armour', 'name': 'Spidersilk Robe', 'tier': 4},
			{'drop': 53, 'base': 'Body Armour', 'name': 'Destroyer Regalia', 'tier': 4},
			{'drop': 56, 'base': 'Body Armour', 'name': "Savant's Robe", 'tier': 4},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Necromancer Silks', 'tier': 4},
			{'drop': 62, 'base': 'Body Armour', 'name': "Occultist's Vestment", 'tier': 3},  # Spell Damage +(3 to 10)
			{'drop': 65, 'base': 'Body Armour', 'name': 'Widowsilk Robe', 'tier': 2},
			{'drop': 68, 'base': 'Body Armour', 'name': 'Vaal Regalia', 'tier': 1},
		],
		"Armour|Body Armour|Dex|Int": [
			{'drop': 4, 'base': 'Body Armour', 'name': 'Padded Vest', 'tier': 4},
			{'drop': 9, 'base': 'Body Armour', 'name': 'Oiled Vest', 'tier': 4},
			{'drop': 18, 'base': 'Body Armour', 'name': 'Padded Jacket', 'tier': 4},
			{'drop': 22, 'base': 'Body Armour', 'name': 'Oiled Coat', 'tier': 4},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Scarlet Raiment', 'tier': 4},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Waxed Garb', 'tier': 4},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Bone Armour', 'tier': 4},
			{'drop': 40, 'base': 'Body Armour', 'name': 'Quilted Jacket', 'tier': 4},
			{'drop': 44, 'base': 'Body Armour', 'name': 'Sleek Coat', 'tier': 4},
			{'drop': 48, 'base': 'Body Armour', 'name': 'Crimson Raiment', 'tier': 4},
			{'drop': 52, 'base': 'Body Armour', 'name': 'Lacquered Garb', 'tier': 4},
			{'drop': 56, 'base': 'Body Armour', 'name': 'Crypt Armour', 'tier': 4},
			{'drop': 59, 'base': 'Body Armour', 'name': 'Sentinel Jacket', 'tier': 4},
			{'drop': 62, 'base': 'Body Armour', 'name': 'Varnished Coat', 'tier': 3},
			{'drop': 65, 'base': 'Body Armour', 'name': 'Blood Raiment', 'tier': 3},
			{'drop': 68, 'base': 'Body Armour', 'name': 'Sadist Garb', 'tier': 2},
			{'drop': 71, 'base': 'Body Armour', 'name': 'Carnal Armour', 'tier': 1},  # Base Maximum Mana (20 to 25)
		],
		"Armour|Body Armour|Int|Str": [
			{'drop': 4, 'base': 'Body Armour', 'name': 'Chainmail Vest', 'tier': 4},
			{'drop': 8, 'base': 'Body Armour', 'name': 'Chainmail Tunic', 'tier': 4},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Ringmail Coat', 'tier': 4},
			{'drop': 21, 'base': 'Body Armour', 'name': 'Chainmail Doublet', 'tier': 4},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Ringmail', 'tier': 4},
			{'drop': 32, 'base': 'Body Armour', 'name': 'Full Chainmail', 'tier': 4},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Holy Chainmail', 'tier': 4},
			{'drop': 39, 'base': 'Body Armour', 'name': 'Latticed Ringmail', 'tier': 4},
			{'drop': 43, 'base': 'Body Armour', 'name': 'Crusader Chainmail', 'tier': 4},
			{'drop': 47, 'base': 'Body Armour', 'name': 'Ornate Ringmail', 'tier': 4},
			{'drop': 51, 'base': 'Body Armour', 'name': 'Chain Hauberk', 'tier': 4},
			{'drop': 55, 'base': 'Body Armour', 'name': 'Devout Chainmail', 'tier': 4},
			{'drop': 58, 'base': 'Body Armour', 'name': 'Loricated Ringmail', 'tier': 4},
			{'drop': 61, 'base': 'Body Armour', 'name': 'Conquest Chainmail', 'tier': 3},
			{'drop': 64, 'base': 'Body Armour', 'name': 'Elegant Ringmail', 'tier': 2},
			{'drop': 67, 'base': 'Body Armour', 'name': "Saint's Hauberk", 'tier': 3},
			{'drop': 70, 'base': 'Body Armour', 'name': 'Saintly Chainmail', 'tier': 1},
		],
		"Armour|Body Armour|Dex|Str": [
			{'drop': 4, 'base': 'Body Armour', 'name': 'Scale Vest', 'tier': 4},
			{'drop': 8, 'base': 'Body Armour', 'name': 'Light Brigandine', 'tier': 4},
			{'drop': 17, 'base': 'Body Armour', 'name': 'Scale Doublet', 'tier': 4},
			{'drop': 21, 'base': 'Body Armour', 'name': 'Infantry Brigandine', 'tier': 4},
			{'drop': 28, 'base': 'Body Armour', 'name': 'Full Scale Armour', 'tier': 4},
			{'drop': 32, 'base': 'Body Armour', 'name': "Soldier's Brigandine", 'tier': 4},
			{'drop': 35, 'base': 'Body Armour', 'name': 'Field Lamellar', 'tier': 4},
			{'drop': 38, 'base': 'Body Armour', 'name': 'Wyrmscale Doublet', 'tier': 4},
			{'drop': 42, 'base': 'Body Armour', 'name': 'Hussar Brigandine', 'tier': 4},
			{'drop': 46, 'base': 'Body Armour', 'name': 'Full Wyrmscale', 'tier': 4},
			{'drop': 50, 'base': 'Body Armour', 'name': "Commander's Brigandine", 'tier': 4},
			{'drop': 54, 'base': 'Body Armour', 'name': 'Battle Lamellar', 'tier': 3},
			{'drop': 57, 'base': 'Body Armour', 'name': 'Dragonscale Doublet', 'tier': 3},
			{'drop': 60, 'base': 'Body Armour', 'name': 'Desert Brigandine', 'tier': 2},
			{'drop': 63, 'base': 'Body Armour', 'name': 'Full Dragonscale', 'tier': 1},
			{'drop': 66, 'base': 'Body Armour', 'name': "General's Brigandine", 'tier': 2},
			{'drop': 69, 'base': 'Body Armour', 'name': 'Triumphant Lamellar', 'tier': 1},
		],
		"Armour|Boots|Str": [
			{'drop': 1, 'base': 'Boots', 'name': 'Iron Greaves', 'tier': 4},
			{'drop': 9, 'base': 'Boots', 'name': 'Steel Greaves', 'tier': 4},
			{'drop': 23, 'base': 'Boots', 'name': 'Plated Greaves', 'tier': 4},
			{'drop': 33, 'base': 'Boots', 'name': 'Reinforced Greaves', 'tier': 4},
			{'drop': 37, 'base': 'Boots', 'name': 'Antique Greaves', 'tier': 4},
			{'drop': 46, 'base': 'Boots', 'name': 'Ancient Greaves', 'tier': 4},
			{'drop': 54, 'base': 'Boots', 'name': 'Goliath Greaves', 'tier': 3},
			{'drop': 62, 'base': 'Boots', 'name': 'Vaal Greaves', 'tier': 2},
			{'drop': 68, 'base': 'Boots', 'name': 'Titan Greaves', 'tier': 1},
],
		"Armour|Boots|Int": [
			{'drop': 3, 'base': 'Boots', 'name': 'Wool Shoes', 'tier': 4},
			{'drop': 9, 'base': 'Boots', 'name': 'Velvet Slippers', 'tier': 4},
			{'drop': 22, 'base': 'Boots', 'name': 'Silk Slippers', 'tier': 4},
			{'drop': 32, 'base': 'Boots', 'name': 'Scholar Boots', 'tier': 4},
			{'drop': 38, 'base': 'Boots', 'name': 'Satin Slippers', 'tier': 4},
			{'drop': 44, 'base': 'Boots', 'name': 'Samite Slippers', 'tier': 4},
			{'drop': 53, 'base': 'Boots', 'name': 'Conjurer Boots', 'tier': 3},
			{'drop': 61, 'base': 'Boots', 'name': 'Arcanist Slippers', 'tier': 2},
			{'drop': 67, 'base': 'Boots', 'name': 'Sorcerer Boots', 'tier': 1},
		],
		"Armour|Boots|Dex": [
			{'drop': 3, 'base': 'Boots', 'name': 'Rawhide Boots', 'tier': 4},
			{'drop': 12, 'base': 'Boots', 'name': 'Goathide Boots', 'tier': 4},
			{'drop': 22, 'base': 'Boots', 'name': 'Deerskin Boots', 'tier': 4},
			{'drop': 34, 'base': 'Boots', 'name': 'Nubuck Boots', 'tier': 4},
			{'drop': 39, 'base': 'Boots', 'name': 'Eelskin Boots', 'tier': 4},
			{'drop': 44, 'base': 'Boots', 'name': 'Sharkskin Boots', 'tier': 4},
			{'drop': 55, 'base': 'Boots', 'name': 'Shagreen Boots', 'tier': 3},
			{'drop': 62, 'base': 'Boots', 'name': 'Stealth Boots', 'tier': 2},
			{'drop': 69, 'base': 'Boots', 'name': 'Slink Boots', 'tier': 1},
		],
		"Armour|Boots|Int|Str": [
			{'drop': 5, 'base': 'Boots', 'name': 'Chain Boots', 'tier': 4},
			{'drop': 13, 'base': 'Boots', 'name': 'Ringmail Boots', 'tier': 4},
			{'drop': 28, 'base': 'Boots', 'name': 'Mesh Boots', 'tier': 4},
			{'drop': 36, 'base': 'Boots', 'name': 'Riveted Boots', 'tier': 4},
			{'drop': 40, 'base': 'Boots', 'name': 'Zealot Boots', 'tier': 4},
			{'drop': 49, 'base': 'Boots', 'name': 'Soldier Boots', 'tier': 4},
			{'drop': 58, 'base': 'Boots', 'name': 'Legion Boots', 'tier': 3},
			{'drop': 64, 'base': 'Boots', 'name': 'Crusader Boots', 'tier': 2},
		],
		"Armour|Boots|Dex|Int": [
			{'drop': 6, 'base': 'Boots', 'name': 'Wrapped Boots', 'tier': 4},
			{'drop': 16, 'base': 'Boots', 'name': 'Strapped Boots', 'tier': 4},
			{'drop': 27, 'base': 'Boots', 'name': 'Clasped Boots', 'tier': 4},
			{'drop': 34, 'base': 'Boots', 'name': 'Shackled Boots', 'tier': 4},
			{'drop': 41, 'base': 'Boots', 'name': 'Trapper Boots', 'tier': 4},
			{'drop': 47, 'base': 'Boots', 'name': 'Ambush Boots', 'tier': 4},
			{'drop': 55, 'base': 'Boots', 'name': 'Carnal Boots', 'tier': 3},
			{'drop': 63, 'base': 'Boots', 'name': "Assassin's Boots", 'tier': 2},
			{'drop': 69, 'base': 'Boots', 'name': 'Murder Boots', 'tier': 2},
			{'drop': 70, 'base': 'Boots', 'name': 'Fugitive Boots', 'tier': 1},
		],
		"Armour|Boots|Dex|Str": [
			{'drop': 6, 'base': 'Boots', 'name': 'Leatherscale Boots', 'tier': 4},
			{'drop': 18, 'base': 'Boots', 'name': 'Ironscale Boots', 'tier': 4},
			{'drop': 30, 'base': 'Boots', 'name': 'Bronzescale Boots', 'tier': 4},
			{'drop': 36, 'base': 'Boots', 'name': 'Steelscale Boots', 'tier': 4},
			{'drop': 42, 'base': 'Boots', 'name': 'Serpentscale Boots', 'tier': 4},
			{'drop': 51, 'base': 'Boots', 'name': 'Wyrmscale Boots', 'tier': 4},
			{'drop': 59, 'base': 'Boots', 'name': 'Hydrascale Boots', 'tier': 3},
			{'drop': 65, 'base': 'Boots', 'name': 'Dragonscale Boots', 'tier': 2},
		],
		"Armour|Boots|Dex|Int|Str": [
			{'drop': 70, 'base': 'Boots', 'name': 'Two-Toned Boots', 'tier': 0},  # Fire And Lightning Damage Resistance (15 to 20) or Fire And Cold Damage Resistance (15 to 20) or Cold And Lightning Damage Resistance (15 to 20)
		],
		"Armour|Gloves|Str": [
			{'drop': 1, 'base': 'Gloves', 'name': 'Iron Gauntlets', 'tier': 4},
			{'drop': 11, 'base': 'Gloves', 'name': 'Plated Gauntlets', 'tier': 4},
			{'drop': 23, 'base': 'Gloves', 'name': 'Bronze Gauntlets', 'tier': 4},
			{'drop': 35, 'base': 'Gloves', 'name': 'Steel Gauntlets', 'tier': 4},
			{'drop': 39, 'base': 'Gloves', 'name': 'Antique Gauntlets', 'tier': 4},
			{'drop': 47, 'base': 'Gloves', 'name': 'Ancient Gauntlets', 'tier': 4},
			{'drop': 53, 'base': 'Gloves', 'name': 'Goliath Gauntlets', 'tier': 3},
			{'drop': 63, 'base': 'Gloves', 'name': 'Vaal Gauntlets', 'tier': 2},
			{'drop': 69, 'base': 'Gloves', 'name': 'Titan Gauntlets', 'tier': 1},
			{'drop': 70, 'base': 'Gloves', 'name': 'Spiked Gloves', 'tier': 0},  # Melee Damage +(16 to 20)
		],
		"Armour|Dex|Gloves": [
			{'drop': 3, 'base': 'Gloves', 'name': 'Rawhide Gloves', 'tier': 4},
			{'drop': 9, 'base': 'Gloves', 'name': 'Goathide Gloves', 'tier': 4},
			{'drop': 21, 'base': 'Gloves', 'name': 'Deerskin Gloves', 'tier': 4},
			{'drop': 33, 'base': 'Gloves', 'name': 'Nubuck Gloves', 'tier': 4},
			{'drop': 38, 'base': 'Gloves', 'name': 'Eelskin Gloves', 'tier': 4},
			{'drop': 45, 'base': 'Gloves', 'name': 'Sharkskin Gloves', 'tier': 4},
			{'drop': 54, 'base': 'Gloves', 'name': 'Shagreen Gloves', 'tier': 3},
			{'drop': 62, 'base': 'Gloves', 'name': 'Stealth Gloves', 'tier': 2},
			{'drop': 70, 'base': 'Gloves', 'name': 'Slink Gloves', 'tier': 1},
			{'drop': 70, 'base': 'Gloves', 'name': 'Gripped Gloves', 'tier': 0},  # Projectile Attack Damage +(14 to 18)
		],
		"Armour|Gloves|Int": [
			{'drop': 3, 'base': 'Gloves', 'name': 'Wool Gloves', 'tier': 4},
			{'drop': 12, 'base': 'Gloves', 'name': 'Velvet Gloves', 'tier': 4},
			{'drop': 25, 'base': 'Gloves', 'name': 'Silk Gloves', 'tier': 4},
			{'drop': 36, 'base': 'Gloves', 'name': 'Embroidered Gloves', 'tier': 4},
			{'drop': 41, 'base': 'Gloves', 'name': 'Satin Gloves', 'tier': 4},
			{'drop': 47, 'base': 'Gloves', 'name': 'Samite Gloves', 'tier': 4},
			{'drop': 55, 'base': 'Gloves', 'name': 'Conjurer Gloves', 'tier': 3},
			{'drop': 60, 'base': 'Gloves', 'name': 'Arcanist Gloves', 'tier': 2},
			{'drop': 69, 'base': 'Gloves', 'name': 'Sorcerer Gloves', 'tier': 1},
			{'drop': 70, 'base': 'Gloves', 'name': 'Fingerless Silk Gloves', 'tier': 0},  # Spell Damage +(12 to 16)
		],
		"Armour|Dex|Gloves|Str": [
			{'drop': 4, 'base': 'Gloves', 'name': 'Fishscale Gauntlets', 'tier': 4},
			{'drop': 15, 'base': 'Gloves', 'name': 'Ironscale Gauntlets', 'tier': 4},
			{'drop': 27, 'base': 'Gloves', 'name': 'Bronzescale Gauntlets', 'tier': 4},
			{'drop': 36, 'base': 'Gloves', 'name': 'Steelscale Gauntlets', 'tier': 4},
			{'drop': 43, 'base': 'Gloves', 'name': 'Serpentscale Gauntlets', 'tier': 4},
			{'drop': 49, 'base': 'Gloves', 'name': 'Wyrmscale Gauntlets', 'tier': 3},
			{'drop': 59, 'base': 'Gloves', 'name': 'Hydrascale Gauntlets', 'tier': 2},
			{'drop': 67, 'base': 'Gloves', 'name': 'Dragonscale Gauntlets', 'tier': 1},
		],
		"Armour|Dex|Gloves|Int": [
			{'drop': 5, 'base': 'Gloves', 'name': 'Wrapped Mitts', 'tier': 4},
			{'drop': 16, 'base': 'Gloves', 'name': 'Strapped Mitts', 'tier': 4},
			{'drop': 31, 'base': 'Gloves', 'name': 'Clasped Mitts', 'tier': 4},
			{'drop': 36, 'base': 'Gloves', 'name': 'Trapper Mitts', 'tier': 4},
			{'drop': 45, 'base': 'Gloves', 'name': 'Ambush Mitts', 'tier': 4},
			{'drop': 50, 'base': 'Gloves', 'name': 'Carnal Mitts', 'tier': 4},
			{'drop': 58, 'base': 'Gloves', 'name': "Assassin's Mitts", 'tier': 3},
			{'drop': 67, 'base': 'Gloves', 'name': 'Murder Mitts', 'tier': 2},
			{'drop': 67, 'base': 'Gloves', 'name': "Apothecary's Gloves", 'tier': 1},  # (14-18)% increased Damage Over Time
		],
		"Armour|Gloves|Int|Str": [
			{'drop': 7, 'base': 'Gloves', 'name': 'Chain Gloves', 'tier': 4},
			{'drop': 19, 'base': 'Gloves', 'name': 'Ringmail Gloves', 'tier': 4},
			{'drop': 32, 'base': 'Gloves', 'name': 'Mesh Gloves', 'tier': 4},
			{'drop': 37, 'base': 'Gloves', 'name': 'Riveted Gloves', 'tier': 4},
			{'drop': 43, 'base': 'Gloves', 'name': 'Zealot Gloves', 'tier': 4},
			{'drop': 51, 'base': 'Gloves', 'name': 'Soldier Gloves', 'tier': 4},
			{'drop': 57, 'base': 'Gloves', 'name': 'Legion Gloves', 'tier': 3},
			{'drop': 66, 'base': 'Gloves', 'name': 'Crusader Gloves', 'tier': 2},
		],
		"Armour|Helmet|Str": [
			{'drop': 1, 'base': 'Helmet', 'name': 'Iron Hat', 'tier': 4},
			{'drop': 7, 'base': 'Helmet', 'name': 'Cone Helmet', 'tier': 4},
			{'drop': 18, 'base': 'Helmet', 'name': 'Barbute Helmet', 'tier': 4},
			{'drop': 26, 'base': 'Helmet', 'name': 'Close Helmet', 'tier': 4},
			{'drop': 35, 'base': 'Helmet', 'name': 'Gladiator Helmet', 'tier': 4},
			{'drop': 40, 'base': 'Helmet', 'name': 'Reaver Helmet', 'tier': 4},
			{'drop': 48, 'base': 'Helmet', 'name': 'Siege Helmet', 'tier': 4},
			{'drop': 55, 'base': 'Helmet', 'name': 'Samnite Helmet', 'tier': 3},
			{'drop': 60, 'base': 'Helmet', 'name': 'Ezomyte Burgonet', 'tier': 2},
			{'drop': 65, 'base': 'Helmet', 'name': 'Royal Burgonet', 'tier': 1},
			{'drop': 69, 'base': 'Helmet', 'name': 'Eternal Burgonet', 'tier': 1},
		],
		"Armour|Dex|Helmet": [
			{'drop': 3, 'base': 'Helmet', 'name': 'Leather Cap', 'tier': 4},
			{'drop': 10, 'base': 'Helmet', 'name': 'Tricorne', 'tier': 4},
			{'drop': 20, 'base': 'Helmet', 'name': 'Leather Hood', 'tier': 4},
			{'drop': 30, 'base': 'Helmet', 'name': 'Wolf Pelt', 'tier': 4},
			{'drop': 41, 'base': 'Helmet', 'name': 'Hunter Hood', 'tier': 4},
			{'drop': 47, 'base': 'Helmet', 'name': 'Noble Tricorne', 'tier': 4},
			{'drop': 55, 'base': 'Helmet', 'name': 'Ursine Pelt', 'tier': 4},
			{'drop': 60, 'base': 'Helmet', 'name': 'Silken Hood', 'tier': 3},
			{'drop': 64, 'base': 'Helmet', 'name': 'Sinner Tricorne', 'tier': 2},
			{'drop': 70, 'base': 'Helmet', 'name': 'Lion Pelt', 'tier': 1},
		],
		"Armour|Helmet|Int": [
			{'drop': 3, 'base': 'Helmet', 'name': 'Vine Circlet', 'tier': 4},
			{'drop': 8, 'base': 'Helmet', 'name': 'Iron Circlet', 'tier': 4},
			{'drop': 17, 'base': 'Helmet', 'name': 'Torture Cage', 'tier': 4},
			{'drop': 26, 'base': 'Helmet', 'name': 'Tribal Circlet', 'tier': 4},
			{'drop': 34, 'base': 'Helmet', 'name': 'Bone Circlet', 'tier': 4},
			{'drop': 39, 'base': 'Helmet', 'name': 'Lunaris Circlet', 'tier': 4},
			{'drop': 48, 'base': 'Helmet', 'name': 'Steel Circlet', 'tier': 4},
			{'drop': 54, 'base': 'Helmet', 'name': 'Necromancer Circlet', 'tier': 4},
			{'drop': 59, 'base': 'Helmet', 'name': 'Solaris Circlet', 'tier': 3},
			{'drop': 65, 'base': 'Helmet', 'name': 'Mind Cage', 'tier': 2},
			{'drop': 69, 'base': 'Helmet', 'name': 'Hubris Circlet', 'tier': 1},
		],
		"Armour|Dex|Helmet|Int": [
			{'drop': 4, 'base': 'Helmet', 'name': 'Scare Mask', 'tier': 4},
			{'drop': 10, 'base': 'Helmet', 'name': 'Plague Mask', 'tier': 4},
			{'drop': 17, 'base': 'Helmet', 'name': 'Iron Mask', 'tier': 4},
			{'drop': 28, 'base': 'Helmet', 'name': 'Festival Mask', 'tier': 4},
			{'drop': 35, 'base': 'Helmet', 'name': 'Golden Mask', 'tier': 4},
			{'drop': 38, 'base': 'Helmet', 'name': 'Raven Mask', 'tier': 4},
			{'drop': 45, 'base': 'Helmet', 'name': 'Callous Mask', 'tier': 4},
			{'drop': 52, 'base': 'Helmet', 'name': 'Regicide Mask', 'tier': 4},
			{'drop': 57, 'base': 'Helmet', 'name': 'Harlequin Mask', 'tier': 4},
			{'drop': 62, 'base': 'Helmet', 'name': 'Vaal Mask', 'tier': 3},
			{'drop': 67, 'base': 'Helmet', 'name': 'Deicide Mask', 'tier': 2},
		],
		"Armour|Dex|Helmet|Str": [
			{'drop': 4, 'base': 'Helmet', 'name': 'Battered Helm', 'tier': 4},
			{'drop': 13, 'base': 'Helmet', 'name': 'Sallet', 'tier': 4},
			{'drop': 23, 'base': 'Helmet', 'name': 'Visored Sallet', 'tier': 4},
			{'drop': 33, 'base': 'Helmet', 'name': 'Gilded Sallet', 'tier': 4},
			{'drop': 36, 'base': 'Helmet', 'name': 'Secutor Helm', 'tier': 4},
			{'drop': 43, 'base': 'Helmet', 'name': 'Fencer Helm', 'tier': 4},
			{'drop': 51, 'base': 'Helmet', 'name': 'Lacquered Helmet', 'tier': 4},
			{'drop': 58, 'base': 'Helmet', 'name': 'Fluted Bascinet', 'tier': 3},
			{'drop': 63, 'base': 'Helmet', 'name': 'Pig-Faced Bascinet', 'tier': 2},
			{'drop': 67, 'base': 'Helmet', 'name': 'Nightmare Bascinet', 'tier': 1},
		],
		"Armour|Helmet|Int|Str": [
			{'drop': 5, 'base': 'Helmet', 'name': 'Rusted Coif', 'tier': 4},
			{'drop': 12, 'base': 'Helmet', 'name': 'Soldier Helmet', 'tier': 4},
			{'drop': 22, 'base': 'Helmet', 'name': 'Great Helmet', 'tier': 4},
			{'drop': 31, 'base': 'Helmet', 'name': 'Crusader Helmet', 'tier': 4},
			{'drop': 37, 'base': 'Helmet', 'name': 'Aventail Helmet', 'tier': 4},
			{'drop': 44, 'base': 'Helmet', 'name': 'Zealot Helmet', 'tier': 4},
			{'drop': 53, 'base': 'Helmet', 'name': 'Great Crown', 'tier': 4},
			{'drop': 58, 'base': 'Helmet', 'name': 'Magistrate Crown', 'tier': 4},
			{'drop': 63, 'base': 'Helmet', 'name': 'Prophet Crown', 'tier': 3},
			{'drop': 68, 'base': 'Helmet', 'name': 'Praetor Crown', 'tier': 2},
			{'drop': 73, 'base': 'Helmet', 'name': 'Bone Helmet', 'tier': 0},  # Minion Damage increase (30 to 40)
		],
		"Armour|Shield|Str": [
			{'drop': 1, 'base': 'Shield', 'name': 'Splintered Tower Shield', 'tier': 4},
			{'drop': 5, 'base': 'Shield', 'name': 'Corroded Tower Shield', 'tier': 4},  # Base Maximum Life (10 to 20)
			{'drop': 11, 'base': 'Shield', 'name': 'Rawhide Tower Shield', 'tier': 4},  # Base Maximum Life (10 to 20)
			{'drop': 17, 'base': 'Shield', 'name': 'Cedar Tower Shield', 'tier': 4},  # Base Maximum Life (20 to 30)
			{'drop': 24, 'base': 'Shield', 'name': 'Copper Tower Shield', 'tier': 4},  # Base Maximum Life (30 to 40)
			{'drop': 30, 'base': 'Shield', 'name': 'Reinforced Tower Shield', 'tier': 4},  # Base Maximum Life (10 to 20)
			{'drop': 35, 'base': 'Shield', 'name': 'Painted Tower Shield', 'tier': 4},  # Base Maximum Life (20 to 30)
			{'drop': 39, 'base': 'Shield', 'name': 'Buckskin Tower Shield', 'tier': 4},  # Base Maximum Life (10 to 20)
			{'drop': 43, 'base': 'Shield', 'name': 'Mahogany Tower Shield', 'tier': 4},  # Base Maximum Life (20 to 30)
			{'drop': 47, 'base': 'Shield', 'name': 'Bronze Tower Shield', 'tier': 4},  # Base Maximum Life (30 to 40)
			{'drop': 51, 'base': 'Shield', 'name': 'Girded Tower Shield', 'tier': 4},  # Base Maximum Life (10 to 20)
			{'drop': 55, 'base': 'Shield', 'name': 'Crested Tower Shield', 'tier': 4},  # Base Maximum Life (20 to 30)
			{'drop': 58, 'base': 'Shield', 'name': 'Shagreen Tower Shield', 'tier': 4},  # Base Maximum Life (10 to 20)
			{'drop': 61, 'base': 'Shield', 'name': 'Ebony Tower Shield', 'tier': 3},  # Base Maximum Life (20 to 30)
			{'drop': 64, 'base': 'Shield', 'name': 'Ezomyte Tower Shield', 'tier': 1},  # Base Maximum Life (30 to 40)
			{'drop': 67, 'base': 'Shield', 'name': 'Colossal Tower Shield', 'tier': 1},  # Base Maximum Life (10 to 20)
			{'drop': 70, 'base': 'Shield', 'name': 'Pinnacle Tower Shield', 'tier': 2},  # Base Maximum Life (20 to 30)
		],
		"Armour|Dex|Shield": [
			{'drop': 2, 'base': 'Shield', 'name': 'Goathide Buckler', 'tier': 4},  # Base Movement Velocity +(3)
			{'drop': 8, 'base': 'Shield', 'name': 'Pine Buckler', 'tier': 4},  # Base Movement Velocity +(3)
			{'drop': 16, 'base': 'Shield', 'name': 'Painted Buckler', 'tier': 4},  # Base Movement Velocity +(6)
			{'drop': 23, 'base': 'Shield', 'name': 'Hammered Buckler', 'tier': 4},  # Base Movement Velocity +(3)
			{'drop': 29, 'base': 'Shield', 'name': 'War Buckler', 'tier': 4},  # Base Movement Velocity +(9)
			{'drop': 34, 'base': 'Shield', 'name': 'Gilded Buckler', 'tier': 4},  # Base Movement Velocity +(6)
			{'drop': 38, 'base': 'Shield', 'name': 'Oak Buckler', 'tier': 4},  # Base Movement Velocity +(3)
			{'drop': 42, 'base': 'Shield', 'name': 'Enameled Buckler', 'tier': 4},  # Base Movement Velocity +(6)
			{'drop': 46, 'base': 'Shield', 'name': 'Corrugated Buckler', 'tier': 4},  # Base Movement Velocity +(3)
			{'drop': 50, 'base': 'Shield', 'name': 'Battle Buckler', 'tier': 4},  # Base Movement Velocity +(9)
			{'drop': 54, 'base': 'Shield', 'name': 'Golden Buckler', 'tier': 4},  # Base Movement Velocity +(6)
			{'drop': 57, 'base': 'Shield', 'name': 'Ironwood Buckler', 'tier': 4},  # Base Movement Velocity +(3)
			{'drop': 60, 'base': 'Shield', 'name': 'Lacquered Buckler', 'tier': 1},  # Base Movement Velocity +(6)
			{'drop': 63, 'base': 'Shield', 'name': 'Vaal Buckler', 'tier': 4},  # Base Movement Velocity +(3)
			{'drop': 66, 'base': 'Shield', 'name': 'Crusader Buckler', 'tier': 3},  # Base Movement Velocity +(9)
			{'drop': 69, 'base': 'Shield', 'name': 'Imperial Buckler', 'tier': 2},  # Base Movement Velocity +(6)
		],
		"Armour|Int|Shield": [
			{'drop': 3, 'base': 'Shield', 'name': 'Twig Spirit Shield', 'tier': 4},  # Spell Damage +(10 to 15)
			{'drop': 9, 'base': 'Shield', 'name': 'Yew Spirit Shield', 'tier': 4},  # Spell Damage +(5 to 10)
			{'drop': 15, 'base': 'Shield', 'name': 'Bone Spirit Shield', 'tier': 4},  # Spell Damage +(15 to 20)
			{'drop': 23, 'base': 'Shield', 'name': 'Tarnished Spirit Shield', 'tier': 4},  # Spell Damage +(5 to 10)
			{'drop': 28, 'base': 'Shield', 'name': 'Jingling Spirit Shield', 'tier': 4},  # Spell Damage +(10 to 15)
			{'drop': 33, 'base': 'Shield', 'name': 'Brass Spirit Shield', 'tier': 4},
			{'drop': 37, 'base': 'Shield', 'name': 'Walnut Spirit Shield', 'tier': 4},  # Spell Damage +(5 to 10)
			{'drop': 41, 'base': 'Shield', 'name': 'Ivory Spirit Shield', 'tier': 4},  # Spell Damage +(15 to 20)
			{'drop': 45, 'base': 'Shield', 'name': 'Ancient Spirit Shield', 'tier': 4},  # Spell Damage +(5 to 10)
			{'drop': 49, 'base': 'Shield', 'name': 'Chiming Spirit Shield', 'tier': 4},  # Spell Damage +(10 to 15)
			{'drop': 53, 'base': 'Shield', 'name': 'Thorium Spirit Shield', 'tier': 4},
			{'drop': 56, 'base': 'Shield', 'name': 'Lacewood Spirit Shield', 'tier': 4},  # Spell Damage +(5 to 10)
			{'drop': 59, 'base': 'Shield', 'name': 'Fossilised Spirit Shield', 'tier': 2},  # Spell Damage +(15 to 20)
			{'drop': 62, 'base': 'Shield', 'name': 'Vaal Spirit Shield', 'tier': 3},  # Spell Damage +(5 to 10)
			{'drop': 65, 'base': 'Shield', 'name': 'Harmonic Spirit Shield', 'tier': 2},  # Spell Damage +(10 to 15)
			{'drop': 68, 'base': 'Shield', 'name': 'Titanium Spirit Shield', 'tier': 1},
		],
		"Armour|Dex|Int|Shield": [
			{'drop': 5, 'base': 'Shield', 'name': 'Spiked Bundle', 'tier': 4},  # Base Chance To Dodge (2)
			{'drop': 12, 'base': 'Shield', 'name': 'Driftwood Spiked Shield', 'tier': 4},  # Base Chance To Dodge (2)
			{'drop': 20, 'base': 'Shield', 'name': 'Alloyed Spiked Shield', 'tier': 4},  # Base Chance To Dodge Spells (2)
			{'drop': 27, 'base': 'Shield', 'name': 'Burnished Spiked Shield', 'tier': 4},  # Base Chance To Dodge (4)
			{'drop': 33, 'base': 'Shield', 'name': 'Ornate Spiked Shield', 'tier': 4},  # Base Chance To Dodge Spells (4)
			{'drop': 39, 'base': 'Shield', 'name': 'Redwood Spiked Shield', 'tier': 4},  # Base Chance To Dodge (2)
			{'drop': 45, 'base': 'Shield', 'name': 'Compound Spiked Shield', 'tier': 4},  # Base Chance To Dodge Spells (2)
			{'drop': 49, 'base': 'Shield', 'name': 'Polished Spiked Shield', 'tier': 4},  # Base Chance To Dodge (4)
			{'drop': 54, 'base': 'Shield', 'name': 'Sovereign Spiked Shield', 'tier': 3},  # Base Chance To Dodge Spells (4)
			{'drop': 58, 'base': 'Shield', 'name': 'Alder Spiked Shield', 'tier': 2},  # Base Chance To Dodge (2)
			{'drop': 62, 'base': 'Shield', 'name': 'Ezomyte Spiked Shield', 'tier': 4},  # Base Chance To Dodge Spells (2)
			{'drop': 66, 'base': 'Shield', 'name': 'Mirrored Spiked Shield', 'tier': 4},  # Base Chance To Dodge (4)
			{'drop': 70, 'base': 'Shield', 'name': 'Supreme Spiked Shield', 'tier': 1},  # Base Chance To Dodge Spells (4)
		],
		"Armour|Dex|Shield|Str": [
			{'drop': 5, 'base': 'Shield', 'name': 'Rotted Round Shield', 'tier': 4},  # Block Recovery Increase (60)
			{'drop': 12, 'base': 'Shield', 'name': 'Fir Round Shield', 'tier': 4},  # Block Recovery Increase (180)
			{'drop': 20, 'base': 'Shield', 'name': 'Studded Round Shield', 'tier': 4},  # Block Recovery Increase (60)
			{'drop': 27, 'base': 'Shield', 'name': 'Scarlet Round Shield', 'tier': 4},
			{'drop': 33, 'base': 'Shield', 'name': 'Splendid Round Shield', 'tier': 4},  # Block Recovery Increase (120)
			{'drop': 39, 'base': 'Shield', 'name': 'Maple Round Shield', 'tier': 4},  # Block Recovery Increase (180)
			{'drop': 45, 'base': 'Shield', 'name': 'Spiked Round Shield', 'tier': 4},  # Block Recovery Increase (60)
			{'drop': 49, 'base': 'Shield', 'name': 'Crimson Round Shield', 'tier': 4},
			{'drop': 54, 'base': 'Shield', 'name': 'Baroque Round Shield', 'tier': 4},  # Block Recovery Increase (120)
			{'drop': 58, 'base': 'Shield', 'name': 'Teak Round Shield', 'tier': 4},  # Block Recovery Increase (180)
			{'drop': 62, 'base': 'Shield', 'name': 'Spiny Round Shield', 'tier': 4},  # Block Recovery Increase (60)
			{'drop': 66, 'base': 'Shield', 'name': 'Cardinal Round Shield', 'tier': 3},
			{'drop': 70, 'base': 'Shield', 'name': 'Elegant Round Shield', 'tier': 2},  # Block Recovery Increase (120)
		],
		"Armour|Int|Shield|Str": [
			{'drop': 7, 'base': 'Shield', 'name': 'Plank Kite Shield', 'tier': 4},  # Resist all Elements (4)
			{'drop': 13, 'base': 'Shield', 'name': 'Linden Kite Shield', 'tier': 4},  # Resist all Elements (4)
			{'drop': 20, 'base': 'Shield', 'name': 'Reinforced Kite Shield', 'tier': 4},
			{'drop': 27, 'base': 'Shield', 'name': 'Layered Kite Shield', 'tier': 3},  # Resist all Elements (8)
			{'drop': 34, 'base': 'Shield', 'name': 'Ceremonial Kite Shield', 'tier': 2},  # Resist all Elements (12)
			{'drop': 40, 'base': 'Shield', 'name': 'Etched Kite Shield', 'tier': 4},  # Resist all Elements (4)
			{'drop': 46, 'base': 'Shield', 'name': 'Steel Kite Shield', 'tier': 4},
			{'drop': 50, 'base': 'Shield', 'name': 'Laminated Kite Shield', 'tier': 3},  # Resist all Elements (8)
			{'drop': 55, 'base': 'Shield', 'name': 'Angelic Kite Shield', 'tier': 2},  # Resist all Elements (12)
			{'drop': 59, 'base': 'Shield', 'name': 'Branded Kite Shield', 'tier': 4},  # Resist all Elements (4)
			{'drop': 62, 'base': 'Shield', 'name': 'Champion Kite Shield', 'tier': 2},
			{'drop': 65, 'base': 'Shield', 'name': 'Mosaic Kite Shield', 'tier': 3},  # Resist all Elements (8)
			{'drop': 68, 'base': 'Shield', 'name': 'Archon Kite Shield', 'tier': 1},  # Resist all Elements (12)
		],
	},
	"Accessory": {
		"Accessory|Amulet": [
			{'drop': 3, 'base': 'Amulet', 'name': 'Paua Amulet', 'tier': 4},  # Mana Regeneration Rate +(20 to 30)
			{'drop': 3, 'base': 'Amulet', 'name': 'Coral Amulet', 'tier': 4},  # Life Regeneration Rate per Minute (120 to 240)
			{'drop': 7, 'base': 'Amulet', 'name': 'Jade Amulet', 'tier': 1},  # Additional Dexterity (20 to 30)
			{'drop': 7, 'base': 'Amulet', 'name': 'Amber Amulet', 'tier': 1},  # Additional Strength (20 to 30)
			{'drop': 7, 'base': 'Amulet', 'name': 'Lapis Amulet', 'tier': 1},  # Additional Intelligence (20 to 30)
			{'drop': 15, 'base': 'Amulet', 'name': 'Gold Amulet', 'tier': 3},  # Base Item Found Rarity +(12 to 20)
			{'drop': 20, 'base': 'Amulet', 'name': 'Agate Amulet', 'tier': 1},  # Additional Strength And Intelligence (16 to 24)
			{'drop': 20, 'base': 'Amulet', 'name': 'Turquoise Amulet', 'tier': 1},  # Additional Dexterity And Intelligence (16 to 24)
			{'drop': 20, 'base': 'Amulet', 'name': 'Citrine Amulet', 'tier': 1},  # Additional Strength And Dexterity (16 to 24)
			{'drop': 25, 'base': 'Amulet', 'name': 'Onyx Amulet', 'tier': 1},  # Additional All Attributes (10 to 16)
			{'drop': 74, 'base': 'Amulet', 'name': 'Marble Amulet', 'tier': 0},  # Life Regeneration Rate Per Minute (72 to 96)
			{'drop': 74, 'base': 'Amulet', 'name': 'Seaglass Amulet', 'tier': 1},  # (10-15)% faster start of energy shield recharge
			{'drop': 77, 'base': 'Amulet', 'name': 'Blue Pearl Amulet', 'tier': 2},  # Mana Regeneration Rate +(48 to 56)
		],
		"Accessory|Belt": [
			{'drop': 1, 'base': 'Belt', 'name': 'Stygian Vise', 'tier': 0},  # Local Has (1) Abyss Sockets
			{'drop': 2, 'base': 'Belt', 'name': 'Rustic Sash', 'tier': 1},  # Physical Damage +(12 to 24)
			{'drop': 2, 'base': 'Belt', 'name': 'Chain Belt', 'tier': 3},  # Base Maximum Energy Shield (9 to 20)
			{'drop': 10, 'base': 'Belt', 'name': 'Heavy Belt', 'tier': 1},  # Additional Strength (25 to 35)
			{'drop': 10, 'base': 'Belt', 'name': 'Leather Belt', 'tier': 1},  # Base Maximum Life (25 to 40)
			{'drop': 20, 'base': 'Belt', 'name': 'Cloth Belt', 'tier': 3},  # Base Stun Recovery +(15 to 25)
			{'drop': 20, 'base': 'Belt', 'name': 'Studded Belt', 'tier': 3},  # Base Stun Duration +(20 to 30)
			{'drop': 73, 'base': 'Belt', 'name': 'Vanguard Belt', 'tier': 2},  # Base Physical Damage Reduction and Evasion Rating (260 to 320)
			{'drop': 73, 'base': 'Belt', 'name': 'Crystal Belt', 'tier': 1},  # Base Maximum Energy Shield (60 to 80)
		],
		"Accessory|Ring": [
			{'drop': 2, 'base': 'Ring', 'name': 'Iron Ring', 'tier': 4},  # Minimum Added Physical Damage (1), Maximum Added Physical Damage (4)
			{'drop': 4, 'base': 'Ring', 'name': 'Coral Ring', 'tier': 1},  # Base Maximum Life (20 to 30)
			{'drop': 5, 'base': 'Ring', 'name': 'Paua Ring', 'tier': 4},  # Base Maximum Mana (20 to 25)
			{'drop': 8, 'base': 'Ring', 'name': 'Sapphire Ring', 'tier': 1},  # Base Cold Damage Resistance (20 to 30)
			{'drop': 12, 'base': 'Ring', 'name': 'Topaz Ring', 'tier': 1},  # Base Lightning Damage Resistance (20 to 30)
			{'drop': 16, 'base': 'Ring', 'name': 'Ruby Ring', 'tier': 1},  # Base Fire Damage Resistance (20 to 30)
			{'drop': 20, 'base': 'Ring', 'name': 'Gold Ring', 'tier': 4},  # Base Item Found Rarity +(6 to 15)
			{'drop': 20, 'base': 'Ring', 'name': 'Two-Stone Ring', 'tier': 1},  # Fire And Lightning Damage Resistance (12 to 16) or Cold And Lightning Damage Resistance (12 to 16) or Fire And Cold Damage Resistance (12 to 16)
			{'drop': 25, 'base': 'Ring', 'name': 'Diamond Ring', 'tier': 2},  # Critical Strike Chance +(20 to 30)
			{'drop': 25, 'base': 'Ring', 'name': 'Moonstone Ring', 'tier': 2},  # Base Maximum Energy Shield (15 to 25)
			{'drop': 30, 'base': 'Ring', 'name': 'Prismatic Ring', 'tier': 0},  # Resist all Elements (8 to 10)
			{'drop': 38, 'base': 'Ring', 'name': 'Amethyst Ring', 'tier': 2},  # Base Chaos Damage Resistance (9 to 13)
			{'drop': 45, 'base': 'Ring', 'name': 'Unset Ring', 'tier': 1},  # Local Has (1) Sockets
			{'drop': 78, 'base': 'Ring', 'name': 'Iolite Ring', 'tier': 0},  # (17-23)% increased Chaos Damage
			{'drop': 78, 'base': 'Ring', 'name': 'Opal Ring', 'tier': 0},  # Elemental Damage +(15 to 25)
			{'drop': 78, 'base': 'Ring', 'name': 'Steel Ring', 'tier': 0},  # Minimum Added Physical Damage (3 to 4), Maximum Added Physical Damage (10 to 14)
			{'drop': 80, 'base': 'Ring', 'name': 'Vermillion Ring', 'tier': 0},  # (5 to 7)% increased maximum Life
			{'drop': 80, 'base': 'Ring', 'name': 'Cerulean Ring', 'tier': 2},  # (8 to 10)% increased maximum Mana
		],
		"Quiver": [
			{'drop': 4, 'base': 'Quiver', 'name': 'Two-Point Arrow Quiver', 'tier': 4},  # (20-30)% increased Global Accuracy Rating
			{'drop': 5, 'base': 'Quiver', 'name': 'Serrated Arrow Quiver', 'tier': 4},  # Adds 1 to 4 Physical Damage to Bow Attacks
			{'drop': 10, 'base': 'Quiver', 'name': 'Sharktooth Arrow Quiver', 'tier': 4},  # +(3-4) Life gained for each Enemy hit by your Attacks
			{'drop': 16, 'base': 'Quiver', 'name': 'Blunt Arrow Quiver', 'tier': 4},  # (25-35)% increased Stun Duration on Enemies
			{'drop': 22, 'base': 'Quiver', 'name': 'Fire Arrow Quiver', 'tier': 4},  # Adds 4 to 8 Fire Damage to Bow Attacks
			{'drop': 28, 'base': 'Quiver', 'name': 'Broadhead Arrow Quiver', 'tier': 3},  # Adds 6 to 12 Physical Damage to Bow Attacks
			{'drop': 36, 'base': 'Quiver', 'name': 'Penetrating Arrow Quiver', 'tier': 2},  # Arrows Pierce an additional Target
			{'drop': 45, 'base': 'Quiver', 'name': 'Ornate Quiver', 'tier': 0},  # Has 1 Socket
			{'drop': 45, 'base': 'Quiver', 'name': 'Spike-Point Arrow Quiver', 'tier': 2},  # (20-30)% increased Global Critical Strike Chance
			{'drop': 74, 'base': 'Quiver', 'name': 'Artillery Quiver', 'tier': 1},  # (20-30)% increased Totem Placement Speed

		],
		"Other": [
			{'drop': 100, 'base': 'Jewel', 'name': 'Cobalt Jewel', 'tier': 1},
			{'drop': 100, 'base': 'Jewel', 'name': 'Crimson Jewel', 'tier': 1},
			{'drop': 100, 'base': 'Jewel', 'name': 'Viridian Jewel', 'tier': 1},
		]
	},
}
