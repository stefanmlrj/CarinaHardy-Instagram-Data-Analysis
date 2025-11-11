# src/image_processing.py
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_and_save_images(uris, image_folder, save_folder, prefix="Post"):
    os.makedirs(save_folder, exist_ok=True)

    for idx, uri in enumerate(uris, start=1):
        image_path = os.path.join(image_folder, uri)
        print(f"Constructed image path: {image_path}")

        if os.path.exists(image_path):
            img = mpimg.imread(image_path)
            plt.figure(figsize=(6, 6))
            plt.imshow(img)
            plt.title(f"{prefix} Performance Post: {uri}")
            plt.axis('off')

            save_path = os.path.join(save_folder, f"{prefix}_{idx}.png")
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.show()
            print(f"✅ Saved: {save_path}")
        else:
            print(f"❌ Image not found for URI: {uri}")
