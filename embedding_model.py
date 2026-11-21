import ollama
import sentence_similiarity as ss
def matrix_embed(strings: list):
  batch = ollama.embed(
    model='embeddinggemma-2:740m',
    input=strings.copy()
  )
  return batch['embeddings']

def vector_embed(string):
  batch = ollama.embed(
    model='embeddinggemma-2:740m',
    input=string
  )
  return batch['embeddings'][0]