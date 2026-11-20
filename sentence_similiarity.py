def mul(vector: list):
  product = 1
  for num in vector:
    product *= num
  return product

def get_magnitude(vector: list):
  squared_vector = [el**2 for el in vector]
  magnitude = sum(squared_vector) ** 0.5
  return magnitude

def get_dot(vector1: list, vector2: list):
  mul_result = []
  for i, el in enumerate(vector1):
    mul_result.append(el * vector2[i])
  return sum(mul_result)

def get_cos_sim(vec_sent1:list, vec_sent2:list):
  dot_product = get_dot(vec_sent1, vec_sent2)
  sentences_length_product = mul([get_magnitude(vec_sent1), get_magnitude(vec_sent2)])
  cosine_similiarity = dot_product / sentences_length_product
  return cosine_similiarity