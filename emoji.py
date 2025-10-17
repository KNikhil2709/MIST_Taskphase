from collections import Counter

# Step 1: Read ciphertext from file
with open("book.txt", "r", encoding="utf-8") as f:
    cipher = f.read().strip()

# Step 2: Count frequency of each emoji/character (ignore punctuation)
emoji_counts = Counter([ch for ch in cipher if ch not in ",. :"])

# Step 3: Sort emojis by frequency
sorted_emojis = [emoji for emoji, count in emoji_counts.most_common()]

# Step 4: Approximate English letter frequency
english_freq_order = list("ETAOINSHRDLCUMWFGYPBVKJXQZ")

# Step 5: Build mapping (emoji -> letter)
mapping = {}
for i, emoji in enumerate(sorted_emojis):
    if i < len(english_freq_order):
        mapping[emoji] = english_freq_order[i]
    else:
        mapping[emoji] = '?'  # unknown letters

# Step 6: Decode text
decoded = ''.join([mapping.get(ch, ch) for ch in cipher])

# Step 7: Extract text after colon (usually challenge or flag)
parts = decoded.split(':', 1)
if len(parts) > 1:
    initial_message = parts[0].strip() + ':'
    challenge_text = parts[1].strip()
else:
    initial_message = decoded
    challenge_text = ''

# Step 8: Print results
print("Initial message:\n")
print(initial_message)
print("\nDecoded challenge text / flag:\n")
print(challenge_text)
