import json

with open('mods_registry.json', encoding='utf8') as f:
    strf = f.read()
    templates = json.loads(strf)

with open("mods_registry.json", encoding='utf8') as f:
    templates2 = json.load(f)

print(strf)
print(type(strf))
print('--------------------------------------')
print(templates)
print(type(templates))
print('--------------------------------------')
print(templates2)
print(type(templates2))