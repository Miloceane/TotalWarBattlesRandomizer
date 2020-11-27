import random

def get_faction(prefs, data):
    faction = None
    factions = list(set(data.keys()) and set(prefs['factions']))

    if not factions:
        return None

    count = 0
    while faction is None and count < 50:
        count += 1
        faction = random.choice(factions)
        if data.get(faction).get('dlc') and data.get(faction).get('dlc_name') not in prefs['dlcs']:
            faction = None

    return faction


def get_lord(faction, prefs, data):
    count = 0

    while count < 50:
        lord = random.choice(list(data.get(faction).get('lords').keys()))

        lord_info = data.get(faction).get('lords').get(lord)

        if lord_info.get('article'):
            lord = f"{lord_info.get('article')} {lord}"

        if lord_info.get('dlc'):
            dlc_name = lord_info.get('dlc_name') if lord_info.get('dlc_name') != "" else data.get(faction).get(
                'dlc_name')
            
            if dlc_name in prefs['dlcs']:
                return lord
        else:
            return lord

    return None