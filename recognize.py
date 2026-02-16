from sentence_transformers import SentenceTransformer, util
from PIL import Image
import os
import shutil

# 1. Load the "Brain" (The CLIP model)
model = SentenceTransformer('clip-ViT-B-32')

# 2. Setup paths and keyword
search_query = "A photo of ocean or a big water mass" # CHANGE THIS 
image_folder = "Path to the photos" # CHANGE THIS 
matches_folder = "Path to the new folder (does not have exist)" # CHANGE THIS 

try:
    os.makedirs(matches_folder, exist_ok=True)
    print(f"Matches folder exists: {os.path.isdir(matches_folder)}")
except OSError as exc:
    print(f"Failed to create matches folder: {exc}")
    raise

# 3. Process images
image_names = [
    f for f in os.listdir(image_folder)
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
]
image_paths = [os.path.join(image_folder, name) for name in image_names]

if not image_paths:
    print("No images found in the source folder.")
    raise SystemExit(0)

# Encode the keyword and images into math (vectors)
query_embedding = model.encode(search_query)
images = []
for path in image_paths:
    with Image.open(path) as img:
        images.append(img.convert("RGB"))
image_embeddings = model.encode(images)

# 4. Compare and Save
hits = util.semantic_search(query_embedding, image_embeddings)[0]

#
#print("Top 5 matches:")
#for hit in hits[:5]:
#    img_name = image_names[hit['corpus_id']]
#    print(f"  {img_name} (Score: {hit['score']:.4f})")

copied_count = 0
for hit in hits:
    if hit['score'] > 0.21:  # Adjust this 'confidence' threshold
        img_name = image_names[hit['corpus_id']]
        src_path = image_paths[hit['corpus_id']]
        dst_path = os.path.join(matches_folder, img_name)
        shutil.copy2(src_path, dst_path)
        copied_count += 1
        # print(f"Copied: {img_name} (Score: {hit['score']:.2f})")

if copied_count == 0:
    print("No images exceeded the threshold. Try lowering it.")