# Run with: python wordcount.py my-file.ipynb
import sys
import json

for filename in sys.argv[1:]:
    wordCount = 0
    if not filename.endswith('.ipynb'):
        exit(filename + " doesn't appear to be an .ipynb file.")
    with open(filename) as f:
        notebookRaw = f.read()
        notebookParsed = json.loads(notebookRaw)
        for cell in notebookParsed['cells']:
            if cell['cell_type'] == "markdown":
                contents = ''.join(cell['source'])
                words = contents.replace('#','').strip().split(' ')
                wordCount += len(words)
                print(words)
    print(filename + ": {} words".format(wordCount))
