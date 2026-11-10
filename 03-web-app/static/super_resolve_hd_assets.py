#!/usr/bin/env python3
import os
from PIL import Image, ImageFilter, ImageEnhance

base_dir = '/home/minh/30-cong-viec/12-dieu-phoi-goi-xe-krong-pak-krong-ana/00-go-stitch-design-package'
img_dir = os.path.join(base_dir, 'images')
asset_dir = os.path.join(base_dir, 'assets')
os.makedirs(asset_dir, exist_ok=True)

# SCALE FACTOR: 2.5x (From 472x1024 -> 1180x2560 Ultra HD Retina)
SCALE = 2.5

def enhance_and_upscale(im, scale=SCALE):
    w, h = im.size
    new_w = int(w * scale)
    new_h = int(h * scale)
    
    # Stage 1: Lanczos high-order sinc interpolation
    upscaled = im.resize((new_w, new_h), resample=Image.Resampling.LANCZOS)
    
    # Stage 2: Dual-stage Unsharp Mask for micro-texture & edge sharpness
    # Sharp edges without haloing
    sharpened = upscaled.filter(ImageFilter.UnsharpMask(radius=2.0, percent=150, threshold=2))
    sharpened = sharpened.filter(ImageFilter.UnsharpMask(radius=0.8, percent=90, threshold=1))
    
    # Stage 3: Contrast & Color definition
    enh_sharp = ImageEnhance.Sharpness(sharpened).enhance(1.25)
    enh_contrast = ImageEnhance.Contrast(enh_sharp).enhance(1.04)
    enh_color = ImageEnhance.Color(enh_contrast).enhance(1.03)
    
    return enh_color

print('Super-resolving master images to Ultra HD (1180x2560)...')
masters = {}
for i in range(1, 7):
    fname = f'0{i}_'
    for f in os.listdir(img_dir):
        if f.startswith(fname) and f.endswith('.jpg'):
            p = os.path.join(img_dir, f)
            raw = Image.open(p).convert('RGB')
            hd = enhance_and_upscale(raw, SCALE)
            masters[i] = hd
            # Save HD master
            hd_path = os.path.join(img_dir, f.replace('.jpg', '_hd.jpg'))
            hd.save(hd_path, quality=98, subsampling=0)
            print(f'  [HD] {f} -> {hd.size} saved.')

def get_crop(hd_img, x1, y1, x2, y2):
    return hd_img.crop((int(x1 * SCALE), int(y1 * SCALE), int(x2 * SCALE), int(y2 * SCALE)))

# Now re-crop all components with ULTRA HD resolution
print('\nCropping Ultra HD assets...')

# Screen 1 Home
im1_hd = masters[1]
get_crop(im1_hd, 24, 45, 175, 160).save(os.path.join(asset_dir, 's1_logo_header.png'), optimize=True)
get_crop(im1_hd, 12, 238, 242, 545).save(os.path.join(asset_dir, 's1_feed_go_banner.jpg'), quality=98, subsampling=0)
get_crop(im1_hd, 250, 238, 460, 526).save(os.path.join(asset_dir, 's1_feed_hanoi.jpg'), quality=98, subsampling=0)
get_crop(im1_hd, 12, 558, 242, 742).save(os.path.join(asset_dir, 's1_feed_cat.jpg'), quality=98, subsampling=0)
get_crop(im1_hd, 250, 538, 460, 740).save(os.path.join(asset_dir, 's1_feed_pho.jpg'), quality=98, subsampling=0)
get_crop(im1_hd, 12, 752, 242, 908).save(os.path.join(asset_dir, 's1_feed_train.jpg'), quality=98, subsampling=0)
get_crop(im1_hd, 250, 750, 460, 908).save(os.path.join(asset_dir, 's1_feed_pig.jpg'), quality=98, subsampling=0)

# Screen 2 Ride Hailing
im2_hd = masters[2]
get_crop(im2_hd, 0, 0, 472, 465).save(os.path.join(asset_dir, 's2_map_full.jpg'), quality=98, subsampling=0)
get_crop(im2_hd, 50, 642, 125, 702).save(os.path.join(asset_dir, 's2_vehicle_bike.png'), optimize=True)
get_crop(im2_hd, 180, 645, 295, 702).save(os.path.join(asset_dir, 's2_vehicle_sedan.png'), optimize=True)
get_crop(im2_hd, 330, 645, 445, 702).save(os.path.join(asset_dir, 's2_vehicle_suv.png'), optimize=True)

# Screen 3 Delivery
im3_hd = masters[3]
get_crop(im3_hd, 0, 0, 472, 335).save(os.path.join(asset_dir, 's3_map_delivery.jpg'), quality=98, subsampling=0)
get_crop(im3_hd, 44, 765, 125, 835).save(os.path.join(asset_dir, 's3_shipper_bike.png'), optimize=True)

# Screen 4 Food Discovery
im4_hd = masters[4]
get_crop(im4_hd, 12, 248, 460, 412).save(os.path.join(asset_dir, 's4_promo_banner.jpg'), quality=98, subsampling=0)
get_crop(im4_hd, 12, 418, 232, 595).save(os.path.join(asset_dir, 's4_food_yihe.jpg'), quality=98, subsampling=0)
get_crop(im4_hd, 240, 418, 460, 575).save(os.path.join(asset_dir, 's4_food_samyang.jpg'), quality=98, subsampling=0)
get_crop(im4_hd, 12, 604, 232, 750).save(os.path.join(asset_dir, 's4_food_kfc.jpg'), quality=98, subsampling=0)
get_crop(im4_hd, 240, 584, 460, 750).save(os.path.join(asset_dir, 's4_food_fries.jpg'), quality=98, subsampling=0)
get_crop(im4_hd, 12, 758, 232, 908).save(os.path.join(asset_dir, 's4_food_banhtrang.jpg'), quality=98, subsampling=0)
get_crop(im4_hd, 240, 758, 460, 908).save(os.path.join(asset_dir, 's4_food_cake.jpg'), quality=98, subsampling=0)

# Screen 5 KFC Store
im5_hd = masters[5]
get_crop(im5_hd, 16, 92, 128, 198).save(os.path.join(asset_dir, 's5_kfc_avatar.png'), optimize=True)
get_crop(im5_hd, 18, 375, 88, 442).save(os.path.join(asset_dir, 's5_story1.png'), optimize=True)
get_crop(im5_hd, 112, 375, 180, 442).save(os.path.join(asset_dir, 's5_story2.png'), optimize=True)
get_crop(im5_hd, 204, 375, 274, 442).save(os.path.join(asset_dir, 's5_story3.png'), optimize=True)
get_crop(im5_hd, 298, 375, 368, 442).save(os.path.join(asset_dir, 's5_story4.png'), optimize=True)
get_crop(im5_hd, 392, 375, 460, 442).save(os.path.join(asset_dir, 's5_story5.png'), optimize=True)
get_crop(im5_hd, 0, 518, 234, 706).save(os.path.join(asset_dir, 's5_post_bucket.jpg'), quality=98, subsampling=0)
get_crop(im5_hd, 238, 518, 472, 706).save(os.path.join(asset_dir, 's5_post_promo50.jpg'), quality=98, subsampling=0)
get_crop(im5_hd, 0, 708, 156, 858).save(os.path.join(asset_dir, 's5_post_burger.jpg'), quality=98, subsampling=0)
get_crop(im5_hd, 158, 708, 314, 858).save(os.path.join(asset_dir, 's5_post_fries.jpg'), quality=98, subsampling=0)
get_crop(im5_hd, 316, 708, 472, 858).save(os.path.join(asset_dir, 's5_post_pepsi.jpg'), quality=98, subsampling=0)

# Screen 6 KFC Food Detail
im6_hd = masters[6]
get_crop(im6_hd, 0, 0, 472, 355).save(os.path.join(asset_dir, 's6_hero_detail.jpg'), quality=98, subsampling=0)
get_crop(im6_hd, 35, 680, 72, 725).save(os.path.join(asset_dir, 's6_addon_fries.png'), optimize=True)
get_crop(im6_hd, 40, 735, 68, 780).save(os.path.join(asset_dir, 's6_addon_pepsi.png'), optimize=True)
get_crop(im6_hd, 0, 0, 472, 355).save(os.path.join(asset_dir, 'kfc_hero_bucket.jpg'), quality=98, subsampling=0)

print('\nALL ASSETS SUPER-RESOLVED TO ULTRA HD SUCESSFULLY!')

