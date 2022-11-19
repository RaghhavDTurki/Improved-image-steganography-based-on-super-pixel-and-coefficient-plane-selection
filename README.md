## Improved image steganography based on super-pixel and coefficient-plane-selection

## Installation
Clone the repository:
```
git clone https://github.com/RaghhavDTurki/Improved-image-steganography-based-on-super-pixel-and-coefficient-plane-selection.git
```

This project requires the following dependencies:
- scikit-image
- matplotlib
- numpy
- opencv-python
- Pillow
- dtcwt
- pandas 
- plotly
  
Install all the dependencies using the following command:
```
pip install scikit-image matplotlib numpy opencv-python Pillow dtcwt pandas plotly
```
You will also need to instal the [Never-Compressed image database] and place it in the project folder.

## Usage
- To run the dtcwt process on an image from the database, run the following:
```
python test_dtcwt.py
```
- To run the super-pixel process on an image from the database, run the following:
```
python calc_superpixel.py
```
- To train the SVM classifier using the RBF function, run the following:
```
python svm.py
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Never-Compressed image database]: <http://www.shsu.edu/~qxl005/New/Database/never_compressed_images.zip>