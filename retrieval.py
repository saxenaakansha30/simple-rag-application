import match_similarity as sim

songs_corpus = [
  {"title": "Bohemian Rhapsody", "details": "lyrics: Is this the real life?; genre: Roc"},
  {"title": "Shake It Off", "details": "lyrics: Players gonna play, hate; genre: Pop"},
  {"title": "Thriller", "details": "lyrics: Cause this is thriller; genre: Pop"},
  {"title": "Rolling in the Deep", "details": "lyrics: There's a fire start; genre: Pop"},
  {"title": "Smells Like Teen Spirit", "details": "lyrics: With the lights out; genre: Gru"},
  {"title": "Hotel California", "details": "lyrics: On a dark desert hwy; genre: Roc"},
  {"title": "Sweet Child o' Mine", "details": "lyrics: She's got eyes blue; genre: Roc"},
  {"title": "Wonderwall", "details": "lyrics: Because maybe, save; genre: Alt"},
  {"title": "Billie Jean", "details": "lyrics: But the kid is not; genre: Pop"},
  {"title": "Firework", "details": "lyrics: Do you ever feel so; genre: Pop"}
]

def get_relevant_document(query):
  relavant_song_title = ''
  max_similarity = 0
  for song in songs_corpus:
    details = song['details']

    similarity = sim.jaccardy_similarity(query, details)
    if similarity > max_similarity:
      max_similarity = similarity
      relavant_song_title = song['title']

  return relavant_song_title
