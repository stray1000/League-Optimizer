import json
import os
import ddragon as lol


item_dict = {}
item_stats_dict = {}
item = "Doran's Ring"

for x in lol.item_data['data']:
    item_dict[lol.item_data['data'][x]['name']] = x

item_stats = lol.item_data['data'][item_dict[item]]['stats']

total_item_cost = lol.item_data['data'][item_dict[item]]['gold']['total']
total_item_cost


for x in item_stats:
    item_stats_dict[x] = item_stats[x]

if 'FlatMagicDamageMod' not in item_stats:
        item_stats_dict['FlatMagicDamageMod'] = 0
if 'FlatPhysicalDamageMod' not in item_stats:
        item_stats_dict['FlatPhysicalDamageMod'] = 0
if 'PercentAttackSpeedMod' not in item_stats:
        item_stats_dict['PercentAttackSpeedMod'] = 0
if 'FlatCritChanceMod' not in item_stats:
        item_stats_dict['FlatCritChanceMod'] = 0
if 'FlatHPPoolMod' not in item_stats:
        item_stats_dict['FlatHPPoolMod'] = 0
if 'FlatMPPoolMod' not in item_stats:
        item_stats_dict['FlatMPPoolMod'] = 0
if 'FlatArmorMod' not in item_stats:
        item_stats_dict['FlatArmorMod'] = 0
if 'FlatSpellBlockMod' not in item_stats:
        item_stats_dict['FlatSpellBlockMod'] = 0
if 'PercentMovementSpeedMod' not in item_stats:
        item_stats_dict['PercentMovementSpeedMod'] = 0
if 'FlatMagicDamageMod' not in item_stats:
        item_stats_dict['FlatMagicDamageMod'] = 0

print(item_stats_dict)
