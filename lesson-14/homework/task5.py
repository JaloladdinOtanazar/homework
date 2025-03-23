from PIL import Image
import numpy as np


# Function to flip image and save
def flip_img(image_array):  
    height, width = image_array.shape[:2]
    flipped = image_array[height-1::-1, width-1::-1, :]
    flipped_img = Image.fromarray(flipped)
    flipped_img.save('flipped_img.jpg')
    return flipped

# Function to add random noise and save
def add_noise(image_array):
    noise = np.random.normal(0, 25, image_array.shape)
    noisy_img = image_array + noise
    noisy_img_clipped = np.clip(noisy_img, 0, 255).astype(np.uint8) 
    noisy_img_pil = Image.fromarray(noisy_img_clipped) 
    noisy_img_pil.save('noisy_img.jpg')  
    return noisy_img_clipped 

# Function to brighten channels and save
def brighten_chan(image_array, value):
    brightened_img = np.clip(image_array + value, 0, 255).astype(np.uint8)  
    brighten_img_pil = Image.fromarray(brightened_img)
    brighten_img_pil.save('brightened_img.jpg')  
    return brightened_img

# Function to apply rectangular mask and save
def apply_mask(image_array, mask_size = 100):
    masked_img = image_array.copy()
    height, width = image_array.shape[:2]
    center_y, center_x = height//2, width//2
    y_start = max(0, center_y - mask_size // 2)
    y_end = min(height, center_y + mask_size // 2)
    x_start = max(0, center_x - mask_size // 2)
    x_end = min(width, center_x + mask_size // 2)
    masked_img[y_start:y_end, x_start:x_end] = [0, 0, 0]
    masked_img_pil = Image.fromarray(masked_img)
    masked_img_pil.save('masked_img.jpg')
    return masked_img

def process_images(output_dir = 'images'):
    try:
        image= Image.open('birds.jpg')
        image_array = np.array(image)
        flipped = flip_img(image_array) 
        noisy = add_noise(flipped)  
        bright = brighten_chan(noisy, 40)  
        masked = apply_mask(bright, 100)  
        print(f"All images processed and saved to {output_dir}/")
        print("Saved files: birds_flipped.jpg, birds_noisy.jpg, birds_bright.jpg, birds_masked.jpg")
    except Exception:
        print("error happened")

if __name__ == '__main__':
    process_images()
