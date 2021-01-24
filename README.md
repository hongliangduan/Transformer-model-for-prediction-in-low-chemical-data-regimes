# Transformer-model-for-prediction-in-low-chemical-data-regimes
This is the code for "Data augmentation and transfer learning strategies for reaction  prediction in low chemical data regimes" paper.
The preprint of this paper can be found in ChemRxiv with https://doi.org/10.26434/chemrxiv.13383275.v1
## Python 2.7
## Tensorflow 1.11
## RDkit 2019.03.4
# Dataset
The dataset we used is named as general chemical reaction dataset, which contains approximately 380,000 chemical reactions. These reaction examples were originally sourced from Lowe's dataset, which were extracted from United States Patent and Trademark Office (USPTO) patents, and then subjected to a collection of pre-reatments in which all the reagents and conditions were deleted. The input data for training and validation was in the tmp folder.
# Generate data
We preprocess the input data by running the datagen.sh script, and put the output data in the t2t_data folder.
# Data augmentation
We use a Python program 1 to perform data augmentation on the training data set of the Baeyer Villiger reaction data set with the SMILES form.
# Train
Model use the train.sh script to start training.
# Test
Model use the decode.sh script to start testing. 
