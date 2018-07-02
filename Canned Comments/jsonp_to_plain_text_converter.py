import json

content = open('canned_comments_json.js').read()
content = content.replace('callback(', '')
content = content[:-1]
print(content)
li = json.loads(content.strip())
li1 = ['###' + x['name'] + '\n' + x['description'] + '\n\n' for x in li]
with open('comments_plain_text.txt', 'w') as f1:
    f1.writelines(li1)
