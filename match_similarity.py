def tokenize(text):
  return set(text.lower().split(" "))

# Mesaures similarity between two data sets.
# Jaccard Index = Intersection (A, B) / Union (A, B)
def jaccardy_similarity(query, document):
  tokenize_query = tokenize(query)
  tokenize_document = tokenize(document)

  intersection = tokenize_query.intersection(tokenize_document)
  union = tokenize_query.union(tokenize_document)

  similarity = len(intersection) / len(union)
  return similarity
