import json

tweets = []
doc = "5656182.json"
id = (doc.split('.'))[0]

for line in open(doc, "r"):
    tweets.append(json.loads(line))

new_doc =  'timelines/' + id + '.txt'

file = open(new_doc, 'a+', encoding='utf-8')
for i in tweets:
    split = i['text'].split()
    if split[0] == 'RT':
        for w in split[2:]:
            if not w == '\n':
                file.write(w +' ')
        file.write('\n')
file.close()
