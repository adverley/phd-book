import re 
path = 'references.bib'
targetpath = 'reference-fixed.bib'

with open(path, "r") as f:
    references = f.readlines()

changes = {}
for line_idx, line in enumerate(references):
    if 'title' in line and 'booktitle' not in line:
        start_title = line.find('{')
        end_title = line.find('},')
        if start_title == -1 or end_title == -1:
            print(f'shit, start or end token not found at id {line_idx}: {line}')
            break
            
        as_is_title = line[start_title+1:end_title]
        to_be_title = 'title = {' + as_is_title[0] + as_is_title[1:].lower() + '},\n'

        changes[line_idx] = to_be_title

with open(targetpath, 'w') as f:
    for line_idx, line in enumerate(references):
        if line_idx in changes.keys():
            f.write(changes[line_idx])
        else:
            f.write(line)

print('done!')

