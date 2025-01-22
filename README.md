# Butterfly Dataset

This repository provides a dataset for butterfly species classification and segmentation. The dataset is structured for tasks such as visualization, machine learning model training, and evaluation. A Python script is included to demonstrate how to read and overlay masks onto images.

## Dataset Structure

### `Major_species_data/`
- Contains data for major butterfly species and hybrids.
- Subdirectories represent specific species or hybrid groups, such as:
  - `(malletti x plesseni) x malleti/`
  - `cyrbia/`
  - `lativitta/`
  - `malletti/`
  - `notabilis x lativitta/`

### `Minor_species_data/`
- Contains data for less prominent butterfly species, which can be used for additional comparisons or exploratory analysis.

### `train_test_separate/`
- Includes pre-split data for training and testing machine learning models.
- Subdirectories correspond to species or hybrid groups and contain:
  - `train_data.json`: Metadata and paths for training images.
  - `test_data.json`: Metadata and paths for testing images.

### Supporting Files
- **`minor_species.json`**: 
  - Contains metadata or supplementary details about minor butterfly species in the dataset.
  - Includes annotations for left-right symmetry patterns, allowing for simplified mask merging based on symmetry mappings (e.g., `1:0`, `2:1` to indicate symmetrical regions).

- **`check_mask_image.py`**: Python script for validating and visualizing image-mask overlays.

---

## Code Description

### `check_mask_image.py`

This Python script demonstrates how to read the dataset, download images, and overlay corresponding segmentation masks. It performs the following tasks:

#### 1. Load the Dataset
- Reads a JSON file (e.g., `train_test_separate/cyrbia/test_data.json`) containing image URLs and mask paths.
- Randomly selects 10 pairs for demonstration.

#### 2. Download Images
- Downloads images from the URLs provided in the JSON file.
- Converts images to RGBA format for easier overlay processing.

#### 3. Load and Resize Masks
- Loads grayscale masks from the relative paths specified in the JSON file.
- Resizes masks to match the size of their corresponding images.

#### 4. Apply Colors to Masks
- Uses a colormap (`matplotlib`'s `tab20`) to programmatically assign distinct colors to mask regions.

#### 5. Overlay Masks onto Images
- Combines the colored mask with the original image using alpha transparency for visualization.
- Displays the overlayed images using Matplotlib.

#### 6. Error Handling
- Ensures proper file existence and handles mismatches in image and mask sizes.

---

## How to Run the Script

### Prerequisites
- Install the required Python libraries:
  ```bash
  pip install matplotlib pillow numpy
