import os
import shutil
import random

train_path = "./Fire_dataset/train"
image_path = "./Fire_dataset/train/images"
lab_path = "./Fire_dataset/train/labels"

val_img_path = "./Fire_dataset/valid/images"
val_lab_path = "./Fire_dataset/valid/labels"

full_train_img = "E:\presentation\Hetvi_Vaghasiya\fire-detection-from-images-master\pytorch\object-detection\yolov5\deepstack\Fire_dataset\train\images"
full_train_lb = "E:\presentation\Hetvi_Vaghasiya\fire-detection-from-images-master\pytorch\object-detection\yolov5\deepstack\Fire_dataset\train\labels"


train_images = os.listdir('./Fire_dataset/train/images')
random.shuffle(train_images)


for i,img in enumerate(train_images):

    if i==1800:
        break
    lb = img[:-4] +".txt"
    print(img,lb)
    print(os.path.exists(img))
    # img_pt = os.path.join(image_path,img)
    img_pt = image_path+"/"+img
    lb_pt = lab_path+"/"+lb
    # lb_pt = os.path.join(lab_path,lb)
    
    full_im_pt = os.path.join(image_path,img)
    full_lb_pt = os.path.join(lab_path,lb)
    
    # val_img_pt = os.path.join(val_img_path,img)
    # val_lb_pt = os.path.join(val_lab_path,lb)
    
    val_img_pt = val_img_path+"/"+img
    val_lb_pt = val_lab_path+"/"+lb
    
    shutil.move(img_pt,val_img_pt)
    shutil.move(lb_pt,val_lb_pt)
    
        
    print(img_pt,lb_pt,val_img_pt,val_lb_pt,full_im_pt,full_lb_pt)