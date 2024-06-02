# Lane Detection on Snowy Roads using Camera and LiDAR

This repository contains code for detecting lanes on snowy roads using data from both camera and LiDAR sensors. The project combines computer vision and machine learning techniques to improve lane detection accuracy in challenging weather conditions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Lane detection in snowy conditions is a complex problem due to the obscured lane markings and the presence of snow on the road. This project leverages both camera images and LiDAR data to detect lanes more reliably. The combination of these two sensor modalities helps in improving the robustness of the lane detection system.

## Features

- **Multi-sensor fusion**: Combines data from camera and LiDAR for enhanced lane detection.
- **Robustness**: Designed to handle challenging conditions such as snow-covered roads.
- **Machine Learning**: Uses advanced machine learning models for accurate lane detection.

## Installation

To get started with this project, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/yourusername/lane-detection-snowy-roads.git
cd lane-detection-snowy-roads
pip install -r requirements.txt
```

## Usage
1. Data Preparation: Ensure you have the necessary camera and LiDAR data. Place the data in the appropriate directories.

2. Preprocessing: Run the preprocessing script to prepare the data for training.

```bash
python preprocess.py --data_path /path/to/your/data
```
3. Training: Train the model using the prepared data.

```bash
python train.py --config config.yaml
```
4. Inference: Use the trained model to detect lanes on new data.

```bash
python infer.py --model_path /path/to/your/model --data_path /path/to/new/data
```
## Data
The project requires synchronized camera and LiDAR data. The data should be organized in a specific format, with corresponding timestamps for both camera images and LiDAR point clouds.

## Model Training
The training script allows customization through a configuration file (config.yaml). This file includes parameters for the model architecture, training settings, and data paths.

## Evaluation
Evaluate the performance of the trained model using the evaluation script. This will provide metrics such as accuracy, precision, and recall.

```bash
python evaluate.py --model_path /path/to/your/model --data_path /path/to/validation/data
```
## Results
The results of the lane detection will be saved in the specified output directory. Visualizations and performance metrics will also be provided.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the CADCD License. See the LICENSE file for more details.
