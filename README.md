# Seam-Carving-And-Object-Removal-From-Scene

This project presents resizing of an image without destroying the content using a seam carving algorithm, and also removing an object from the scene with the help of a binary mask.

The seam is a connected path of low energy pixels crossing the image from top to bottom, or from left to right.

# Libraries Used

- PyTorch
- Numpy
- Pandas

# Methods

## Image Resizing

To resize an image the algorithm I used was Seam Carving through seam insertion for scaling up the image and seam removal for scaling up the image. The basic idea of this approach is to remove unimportant pixels in case of seam removal and remove unimportant pixels and add important ones back in the case of seam insertion. An image energy function is then used to define the importance of pixels. Used two techniques to calculate the energy map

i) Backward Energy
The algorithm commutatively removes or adds low energy seams to an image. Using the energy map, used dynamic programming to find the minimum-energy path. This path is removed in the case of seam removal and added in the case of seam insertion.

ii) Forward Energy
After the seam is removed or added, the forward energy enhancement was implemented by me taking into account the energy created by the new neighbours. During the generation of the accumulated cost matrix, the original algorithm is updated by adding this extra forward energy. The forward energy from the associated new neighbours is added to each top neighbour's cumulative cost value when determining which top neighbour (top-left, top-centre, top-right) in the accumulated cost matrix has the lowest energy value

## Object Removal

Object removal is accomplished by first producing a binary mask of the object to be eliminated during pre-processing. First, the area of the masked zone is calculated to determine whether it is more effective to remove the object from top to bottom seams or from left to right seams. The areas under the masked region are then weighted with a very high negative value when creating the image's energy map. This ensures that the masked zone will have the fewest seams possible. The seams are then removed from both the image and mask.


# Getting Started

Run the following command 

python3 main.py (--resize|--remove) --input <input image path> --output<output image path> [--input_mask| --remove_mask]<path of masked object to be preserved| path of masked object to be removed> (--forward_energy(by default backward energy is done) (-- nh --nw)<if --resize>

I've added some input images for people to try using this algorithm, you could also add images of your choice to the in folder, also created the out
folder to display the output images.









