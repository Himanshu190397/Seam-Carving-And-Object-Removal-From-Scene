# Examples:

# python main.py --remove --input ./in/eiffel.jpg --output ./out/eiffel_remove.jpg --remove_mask ./in/eiffel_mask.jpg
# python main.py --resize --input in/image6.jpg --output out/op_resize.jpg  --nh 200 --nw 512
# import numpy as np
import cv2
import argparse

from seamCarver import SeamCarver



SHOULD_DOWNSIZE = True                    # if True, downsize image for faster carving
DOWNSIZE_WIDTH = 500                      # resized image width if SHOULD_DOWNSIZE is True



# resize image for faster processing. Aspect ratio of 4:3 is maintained with new width set to 500.
def resize(image, width):
    dim = None
    dim = (width, int(3 * width / 4))
    return cv2.resize(image, dim)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implements seam carving to resize image using forward and backward energy. Also performs object detection and removal using masks ')
    parser.add_argument("--resize", action='store_true')
    parser.add_argument("--remove", action='store_true')

    parser.add_argument("--input", help="Image Path", required=True)
    parser.add_argument("--output", help="Output file name", required=True)
    parser.add_argument("--input_mask", default='',help="Path to (protective) mask")
    parser.add_argument("--remove_mask", help="Path to removal mask")
    parser.add_argument("--nh", help="New Hieght", type=int, default=0)
    parser.add_argument("--nw", help="New Width", type=int, default=0)
 
    parser.add_argument("--forward_energy", help="Use forward energy map", action='store_true')
    args = parser.parse_args()



    im = cv2.imread(args.input)
    assert im is not None
    mask = cv2.imread(args.input_mask, 0) if args.input_mask else None
    rmask = cv2.imread(args.remove_mask, 0) if args.remove_mask else None

    

    # downsize image for faster processing
    h, w = im.shape[:2]
    if SHOULD_DOWNSIZE and w > DOWNSIZE_WIDTH:
        im = resize(im, width=DOWNSIZE_WIDTH)
        if mask is not None:
            mask = resize(mask, width=DOWNSIZE_WIDTH)
        if rmask is not None:
            rmask = resize(rmask, width=DOWNSIZE_WIDTH)
    h, w = im.shape[:2]

    op = SeamCarver(im,args.forward_energy)
    # image resize mode
   
    if args.resize:

        dr, dc = int(args.nh - h), int(args.nw - w)
        assert dr is not None and dc is not None
        
        output = op.seam_carve(im, dr, dc, mask)
        cv2.imwrite(args.output, output)


    
    # object removal mode
    elif args.remove:
        assert rmask is not None
        output = op.object_removal(im, rmask, mask)
        cv2.imwrite(args.output, output)