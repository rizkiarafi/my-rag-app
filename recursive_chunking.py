import re
numlist = [3, 5, 2]

def repeat(numlist: list, curr_index: int = 0):
  if curr_index >= len(numlist):
    return 0
  return numlist[curr_index] + repeat(numlist, curr_index + 1)

with open('text.txt') as f:
  text = f.read()

hierarchy = [r"\.\s*\n", r'(?<!\()\.(?!\))']
def recursive_chunk(whole: str, hierarchy: list, index=0):
  done_chunks = []
  if index < len(hierarchy):
    chunks = [c.replace('\n', '').strip() for c in re.split(hierarchy[index], whole) if c]
    for c in chunks:
      if len(c) > 300:
        done_chunks += recursive_chunk(c, hierarchy, index + 1)
      else:
        done_chunks.append(c)
  else:
    done_chunks.append(whole)
  return done_chunks

processed_chunks = recursive_chunk(text, hierarchy)
for i, chunk in enumerate(processed_chunks):
  print(f'Chunk ke-{i}: {chunk}')
  print('\n')