from transformers import RobertaTokenizer, RobertaModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained RoBERTa model and tokenizer
model_name = 'roberta-base'
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = RobertaModel.from_pretrained(model_name)

# Define the two texts you want to compare
#text1 = "Thioquest DP8 Capsule is a combination medicine that helps in relieving muscular pain. It works by blocking the release of certain chemical messengers that cause pain, inflammation, and fever. This improves the movement of muscles and provides relief from pain and discomfort."
#text2 = "Thioquest Dp 8 Capsule is a non-steroidal anti-inflammation medication which is used as a painkiller in the treatment of conditions like Gout, migraines, Rheumatoid Arthritis, fever and to some degree of muscle spasms and joints. It is known to effectively relieve pain, swelling and joint stiffness caused by arthritis."

text1 = "Paracetamol (Panadol, Calpol, Alvedon) is an analgesic and antipyretic drug that is used to temporarily relieve mild-to-moderate pain and fever. It is commonly included as an ingredient in cold and flu medications and is also used on its own."
text2 = "This drug is used to treat mild to moderate pain (from headaches, menstrual periods, toothaches, backaches, osteoarthritis, or cold/flu aches and pains) and to reduce fever."


# Tokenize the texts and convert them to tensors
tokens1 = tokenizer.encode(text1, add_special_tokens=True, max_length=512, truncation=True)
tokens2 = tokenizer.encode(text2, add_special_tokens=True, max_length=512, truncation=True)

input_ids1 = torch.tensor(tokens1).unsqueeze(0)  # Add batch dimension
input_ids2 = torch.tensor(tokens2).unsqueeze(0)

# Use the RoBERTa model to obtain embeddings for the texts
with torch.no_grad():
    outputs1 = model(input_ids1)
    outputs2 = model(input_ids2)

# Compute the cosine similarity between the embeddings
embeddings1 = outputs1.last_hidden_state.mean(dim=1)
embeddings2 = outputs2.last_hidden_state.mean(dim=1)

similarity_score = cosine_similarity(embeddings1, embeddings2)[0][0]

# Set a similarity threshold (adjust as needed)
threshold = 0.8

# Determine if the texts are similar or different based on the threshold
if similarity_score >= threshold:
    result = "Similar"
else:
    result = "Different"

# Print the result
print(f"Texts are {result} (Similarity Score: {similarity_score})")
