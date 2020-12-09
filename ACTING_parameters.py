#!/usr/bin/env python
# coding: utf-8

# Most parameters in this file a taken/adapted from the group simulator model code 
# written by Heise in netlogo for the publication "Heise, D. R. (2013). Modeling 
# Interactions in Small Groups. Social Psychology Quarterly, 76(1), 52–72. doi:
# 10.1177/0190272512467654"  and the 2007 book by Heise "Expreesive Order - 
# Confirming sentiments in Social Actions"

import numpy as np

abo_coefficients_dict = {}
emotion_coefficients_dict = {}

#male equations us
raw="""-1 0 0 0 0 0 0 0 0 -0.26 0.41 0 0 0.42 -0.02 -0.10 0.03 0.06 0 0.05 0 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0.12 -0.05 0 -0.05 0 0 0 0 0 0.03 -0.02 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 -1 0 0 0 0 0 0 0 -0.10 0 0.56 0.06 -0.07 0.44 0 0.04 0 0 0 0 0 0 0 0 0 -0.05 0 0 0 0 0 0 0 0 0 0 0.01 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 -1 0 0 0 0 0 0 0.14 0.05 0 0.64 -0.06 0 0.29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.06 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 -1 0 0 0 0 0 -0.19 0.11 0 0 0.53 0 -0.12 0 0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.11 -0.05 0 -0.02 0 0 0 0 0 0.02 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 -1 0 0 0 0 0.06 0 0.16 0 -0.13 0.70 0 0.03 0.01 0 0.01 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 -1 0 0 0 0.11 0.02 -0.06 0.27 0.04 0 0.64 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 -1 0 0 -0.11 0 0 0 0.11 0 0 0.61 0 0.03 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.04 0 0 -0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 -1 0 -0.37 0 0 0 0.18 -0.11 0 -0.08 0.66 0.07 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.03 0.03 0 0 -0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 -1 0.02 0 0 0 0.02 0 0 0.03 -0.05 0.66 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["us_male"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.32 0.69 -0.36 0 0.47 0.01 -0.07 0.12 0 0 0 0 0 0 0 0
      -0.18 -0.18 0.65 0.01 -0.01 0.59 0.05 0 0 0 0 0 0 0 0 0
      -0.11 -0.04 0.07 0.53 -0.02 -0.02 0.64 0 0 0 0 0 0 0 0 0
""".split()
emotion_coefficients_dict["us_male"] = np.array([float(x) for x in raw_emo])


#male equations canada
raw="""-1 0 0 0 0 0 0 0 0 -0.24 0.45 0 0 0.51 0 0 0 0 0 0.09 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 -1 0 0 0 0 0 0 0 -0.21 0 0.54 0 0 0.45 0.12 0 -0.08 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 -1 0 0 0 0 0 0 -0.07 0 0 0.71 0 0.16 0.29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.06 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 -1 0 0 0 0 0 0.00 0.08 0 0 0.73 0 0 0 0 0 0.06 0 0.07 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 -1 0 0 0 0 0.00 0 0 0 0 0.63 0.19 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 -1 0 0 0 0.02 0 0 0.21 -0.04 0.12 0.52 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 -1 0 0 -0.11 0 0 0 0.18 0 0 0.52 -0.08 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 -1 0 -0.21 0 -0.09 0 0 0 -0.28 0 0.54 0.13 0 0 0.05 0 0 -0.04 0 0 0 0 0 0 0.04 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 -1 -0.12 0 0 0 0 0 0 0 0.09 0.59 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["canada_male"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.26 0.67 -0.29 -0.11 0.47 -0.02 0 0.12 0 0 0 0 0 0 0 0
      -0.18 -0.15 0.76 0.06 -0.02 0.56 0.07 0 0 0 0 0 0 0 0 0
      0.07 0.05 -0.09 0.67 0.01 -0.09 0.67 0 0 0 0 0 0 0 0 0
""".split()
emotion_coefficients_dict["canada_male"] = np.array([float(x) for x in raw_emo])


#unisex equations canada
raw="""-1 0 0 0 0 0 0 0 0 -0.24 0.45 0 0 0.51 0 0 0 0 0 0.09 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 -1 0 0 0 0 0 0 0 -0.21 0 0.54 0 0 0.45 0.12 0 -0.08 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 -1 0 0 0 0 0 0 -0.07 0 0 0.71 0 0.16 0.29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.06 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 -1 0 0 0 0 0 0.00 0.08 0 0 0.73 0 0 0 0 0 0.06 0 0.07 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 -1 0 0 0 0 0.00 0 0 0 0 0.63 0.19 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 -1 0 0 0 0.02 0 0 0.21 -0.04 0.12 0.52 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 -1 0 0 -0.11 0 0 0 0.18 0 0 0.52 -0.08 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 -1 0 -0.21 0 -0.09 0 0 0 -0.28 0 0.54 0.13 0 0 0.05 0 0 -0.04 0 0 0 0 0 0 0.04 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 -1 -0.12 0 0 0 0 0 0 0 0.09 0.59 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["canada_unisex"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.26 0.67 -0.29 -0.11 0.47 -0.02 0 0.12 0 0 0 0 0 0 0 0
        -0.18 -0.15 0.76 0.06 -0.02 0.56 0.07 0 0 0 0 0 0 0 0 0
        0.07 0.05 -0.09 0.67 0.01 -0.09 0.67 0 0 0 0 0 0 0 0 0
""".split()
emotion_coefficients_dict["canada_unisex"] = np.array([float(x) for x in raw_emo])


#female equations us
raw="""-1 0 0 0 0 0 0 0 0 -0.05 0.41 0 0 0.42 -0.02 -0.10 0.03 0.06 0 0.05 0 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0.12 -0.05 0 -0.05 0 0 0 0 0 0.03 -0.02 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 -1 0 0 0 0 0 0 0 -0.10 0 0.56 0.06 -0.14 0.44 0 0.04 0 0 0 0 0 0 0 0 0 -0.05 0 0 0 0 0 0 0 0 0 0 0.01 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 -1 0 0 0 0 0 0 0.14 0.05 0 0.77 -0.06 0 0.29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.06 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 -1 0 0 0 0 0 -0.09 0.11 0 0 0.58 0 -0.12 0 0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.11 -0.05 0 -0.02 0 0 0 0 0 0.02 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 -1 0 0 0 0 0.06 0 0.16 0 -0.17 0.67 0 0.03 -0.04 0 0.01 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.01 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 -1 0 0 0 0.23 0.02 -0.06 0.33 0.04 0 0.64 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 -1 0 0 0.16 0 0 0 0.11 0 0 0.61 0 -0.05 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.04 0 0 -0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 -1 0 -0.42 0 0 0 0.12 -0.11 0 -0.15 0.66 0.07 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.03 0.03 0 0 -0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 -1 -0.09 0 0 0 0.02 0 0 0.03 -0.05 0.83 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["us_female"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.32 0.69 -0.36 0 0.47 0.01 -0.07 0.12 0 0 0 0 0 0 0 0
      -0.18 -0.18 0.65 0.01 -0.01 0.59 0.05 0 0 0 0 0 0 0 0 0
      -0.11 -0.04 0.07 0.53 -0.02 -0.02 0.64 0 0 0 0 0 0 0 0 0
""".split()
emotion_coefficients_dict["us_female"] = np.array([float(x) for x in raw_emo])



#female equations canada
raw="""-1 0 0 0 0 0 0 0 0 -0.24 0.45 0 0 0.51 0 0 0 0 0 0.09 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 -1 0 0 0 0 0 0 0 -0.21 0 0.63 0 0 0.45 0.21 0 -0.08 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 -1 0 0 0 0 0 0 -0.07 0 0 0.71 0 0.16 0.29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.06 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 -1 0 0 0 0 0 0.00 0.08 0 0 0.83 0 0 0 0 0 0.06 0 0.07 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 -1 0 0 0 0 0.00 0 0 0 0 0.63 0.19 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 -1 0 0 0 0.02 0 0 0.21 -0.04 0.12 0.52 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 -1 0 0 0.02 0 0 0 0.12 0 0 0.65 -0.08 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 -1 0 -0.21 0 -0.09 0 0 0 -0.28 0 0.70 0.13 0 0 0.05 0 0 -0.04 0 0 0 0 0 0 0.04 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 -1 -0.12 0 0 0 0 0 0 0 0.09 0.68 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["canada_female"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.26 0.67 -0.29 -0.11 0.47 -0.02 0 0.12 0 0 0 0 0 0 0 0
      -0.18 -0.15 0.76 0.06 -0.02 0.56 0.07 0 0 0 0 0 0 0 0 0
      0.07 0.05 -0.09 0.67 0.01 -0.09 0.67 0 0 0 0 0 0 0 0 0
""".split()
emotion_coefficients_dict["canada_female"] = np.array([float(x) for x in raw_emo])



#unisex-equations US
raw="""-1  0 0 0 0 0 0 0 0 -0.18 0.41 0 0 0.42 0 -0.11 0.03 0.06 0 0.05 0 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0.12 -0.05 0 -0.05 0 0 0 0 0 0.03 -0.02 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0  -1  0 0 0 0 0 0 0 -0.10 0 0.56 0.06 -0.10 0.44 0 0.04 0 0 0 0 0 0 0 0 0 -0.05 0 0 0 0 0 0 0 0 0 0 0.01 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0  -1  0 0 0 0 0 0 0.15 0.05 0 0.69 -0.06 0 0.29 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.06 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0  -1  0 0 0 0 0 -0.14 0.11 0 0 0.55 0 -0.13 0 0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.11 -0.05 0 -0.02 0 0 0 0 0 0.02 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0  -1  0 0 0 0 0.05 0 0.15 0 -0.14 0.69 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.02 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0  -1  0 0 0 0.17 0.02 -0.05 0.30 0.04 0 0.63 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0  -1  0 0 0.00 0 0 0 0.11 0 0 0.62 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0 0 -0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0  -1  0 -0.40 0 0 0 0.16 -0.11 0 -0.11 0.66 0.07 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.03 0.02 0 0 -0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0  -1  -0.02 0 0 0 0.02 0 0 0.02 -0.05 0.72 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["us_unisex"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.32 0.69 -0.36 0 0.47 0.01 -0.07 0.12 0 0 0 0 0 0 0 0
       -0.18 -0.18 0.65 0.01 -0.01 0.59 0.05 0 0 0 0 0 0 0 0 0
       -0.11 -0.04 0.07 0.53 -0.02 -0.02 0.64 0 0 0 0 0 0 0 0 0
""".split()
emotion_coefficients_dict["us_unisex"] = np.array([float(x) for x in raw_emo])


#unisex-equations china
raw="""-1 0 0 0 0 0 0 0 0 -0.13 0.54 0 0 0.64 0 -0.09 0 0 0 0.13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.3 -0.1 0 -0.05 0.08 0 0 0 0 0.11 -0.06 0 0 0.06 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.03 0
        0 -1 0 0 0 0 0 0 0 -0.12 -0.07 0.77 0.06 -0.26 0.44 0 0.05 0 0 0 0 0 0 0 0 0.11 -0.12 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.04 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 -1 0 0 0 0 0 0 0.08 0.09 -0.07 0.86 -0.17 0.09 0.31 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 -1 0 0 0 0 0 -0.08 0.13 0 0 0.85 0 -0.1 0 0 0 0.04 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.28 -0.07 0 0 0.03 0 0 0.04 0 0.09 -0.03 0 0 0.03 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 -1 0 0 0 0 0.07 0 0.21 0 -0.37 0.78 0 0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0 0 0 0 0 0 0.07 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 -1 0 0 0 0.06 0 -0.07 0.38 -0.14 0.13 0.72 0 0 0.04 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 -1 0 0 0.02 0 0 0 0.2 0 0 0.89 0 0 0.09 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.12 0 0 0 0 0 0 0 0 0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 -1 0 -0.04 0 -0.04 0 0.32 -0.11 0.05 -0.21 0.8 0.09 0 0.04 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0 0 0 0 0 0.05 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 -1 -0.04 0 0 0 0 0 0 0 -0.04 0.86 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["china_unisex"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.5 0.6 -0.1 -0.13 0.39 0.06 0 0.08 0 0 0 0 0 0.02 -0.05 0
        -0.36 0 0.6 0 0.09 0.48 0.07 0 0 0 0 0 0 0 0 0
        0.09 -0.12 0.11 0.59 0 0 0.36 0 0 0 0 0 0 0 -0.05 0.07
""".split()
emotion_coefficients_dict["china_unixes"] = np.array([float(x) for x in raw_emo])

#unisex-equations germany
raw="""-1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  -0.38  0.42  0  -0.11  0.47  0  0  0.11  0  0  0.05  0  0  0  0  0.06  0  0  0  0  0  0  0  0  0  0.09  0  0.09  0.04  0  -0.07  -0.13  0  0  0  0  0  0  -0.03  0  0.02  0  0  0  0  0  0  0  0.03  -0.02  0  0  0  0  0  0  0  0  0  0  0  0  0  0
        0.00  -1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  -0.03  0  0.39  0.08  -0.07  0.57  0  0  -0.2  0.16  0  0  0  0  0  0  0  0  -0.04  0  0  0  0  0  0  0  -0.07  0  0  0  0  0  0  0  0.03  0.06  0  0  0  0  0  0  0.02  0  0  0  0  0  0  0  0  0  0  0  0.02  0  0  0  0  0  0  0  0  0
        0.00  0.00  -1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.1  0  0  0.39  -0.13  0.14  0.52  0  0  0  0  0  0  0  0  0  0  0  -0.03  -0.03  0  0  0  0  -0.06  0  0.04  0  0  0  0  0  0.07  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  -0.04  0
        0.00  0.00  0.00  -1.00  0.00  0.00  0.00  0.00  0.00  -0.72  0.23  0  0  0.51  0  0  0.2  0  0  0.06  0.08  0  0.04  -0.04  0  0  0  0  0  0  0  0  0  0  0  0.05  0.09  0.06  0  -0.09  -0.1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0.03  0  0  0  0  0  0  0  0  0  0  0  0  0  0  -0.05
        0.00  0.00  0.00  0.00  -1.00  0.00  0.00  0.00  0.00  -0.05  0  0.17  0.1  0  0.66  0  0  0  0  0  0  0.02  0  0  0.04  0  0  0  0  0  0  0  -0.09  0  0  0  0  0  0  -0.05  0.02  0  0  0  0  0  0  0  0  0  0  0  0  -0.01  0  0  0  0  0  0  0.02  0  0  0  0  0  0.03  0  0  0  0  0  0
        0.00  0.00  0.00  0.00  0.00  -1.00  0.00  0.00  0.00  0.18  0  0  0.28  -0.06  0  0.62  0  0  0  -0.02  0  0  0  0  0  0  0  0  -0.03  0  0  0  0  -0.07  0  0  0  0  0.04  0.04  0  0  0  0  0.08  0  0  0  0  0  0  0  0.02  0  0  0  0  0  0  0  0  0.02  0  0  0  0  0  0  0  0  0  -0.03  0.03
        0.00  0.00  0.00  0.00  0.00  0.00  -1.00  0.00  0.00  -0.15  0  0.1  0  0.13  0  0  0.38  0  0  0.06  0  0  0.03  0  0  0  -0.04  0  0  0  0  -0.03  0  0  0  0.04  0  0  0  0  0  0  -0.06  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
        0.00  0.00  0.00  0.00  0.00  0.00  0.00  -1.00  0.00  -0.26  0  -0.28  0  0.17  -0.54  0.15  0  0.4  0  0  0  0  0  0.03  0  0  0  0.08  0  0  0  0  0  0  0.09  0.06  0  0  0  0  -0.06  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  -0.02  0  0  0  0  0  0  0  0  0
        0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  -1.00  -0.57  0  -0.18  0  0  0  0  0  0  0.28  0  0  0  0  0  0  0  0  0.05  0  0.05  0  0.03  0  0  0  0  0  0  0  0  -0.08  0.08  0  0  0  0  0  0  0.01  0  0  0  0.01  0  0  0  0  0  0  -0.03  0  0  0  0  0  0  -0.03  0  0  0  0  0  -0.02""".split()
abo_coefficients = np.array([float(x) for x in raw])
abo_coefficients_dict["ger_unisex"]=abo_coefficients.reshape(9,73)

raw_emo="""-0.50  0.60  -0.10  -0.13  0.39  0.06  0.00  0.08  0.00  0.00  0.00  0.00  0.00  0.02  -0.05  0.00
        -0.36  0.00  0.60  0.00  0.09  0.48  0.07  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00
        0.09  -0.12  0.11  0.59  0.00  0.00  0.36  0.00  0.00  0.00  0.00  0.00  0.00  0.00  -0.05  0.07
""".split()
emotion_coefficients_dict["ger_unisex"] = np.array([float(x) for x in raw_emo])



s_beta = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
       0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
       0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
       1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0,
       1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1])

s_beta = s_beta.reshape((3, 73))

g = np.array([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0,
       1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0])

#IPA setup-Bales-categories
SYMLOG_directions = ["U", "UP", "UPF", "UF", "UNF", "UN", "UNB", "UB", "UPB", "P", "PF", "F",   "NF", "N", "NB",
    "B", "PB", "DP", "DPF", "DF", "DNF",   "DN", "DNB", "DB",   "DPB", "D", "0"]


SYMLOG_topics = ["success, power, the future", "popularity, personal involvement", "teamwork, solidarity",
    "efficiency, loyalty, harmony", "authority, rules, obedience", "adventure, challenges, ambition",
    "sensualism, nonconformity, being anti-authority", "relativism, expressiveness", "being protective, supportive",
    "equality, democracy, tolerance", "benevolence, altruism", "established rules, morality, religion",
    "conscience, self-control", "self-sufficiency, individualism, isolationism", "cynicism, subversiveness",
    "creativity, innovation, anti-religion", "friendship, collaboration", "trust, appreciation",
    "faithfulness, dedication", "introspection, moderation", "self-sacrifice, asceticism",
    "reclusion, being anti-social", "detachment, resignation", "noncooperation, uncertainty",
    "permissiveness, indulgence", "self-denial, self-distain, abstinence", "ambivalence, uncertainty"]

SYMLOG_verbs = [
    #"U" "UP" "UPF" "UF"
    "commands, hollers at, disagrees with",
    "asks about __, tells __ to, answers",   
    "corrects, advises, confers with",   
    "orders, persuades, reprimands",
    # "UNF" "UN" "UNB" "UB" "UPB"
    "silences, forbids, ~interrogates",   
    "criticizes, scolds, quarrels with",   
    "dares, giggles at, taunts",  
    "joshes, banters with, is saracastic toward",
    "chatters to, ~encourages, ~jokes with",
    # "P" "PF" "F" "NF" "N"
     "admits __ to, consults,agrees with",
    "explains to, listens to, confides in",
    "~prays for, ~assures, ~calms",
    "~demeans, ~threatens, ~talks down to",
    "nags, ridicules, insults",
    #"NB" "B" "PB" "DP" "DPF"
    "wheedles, quibbles with, grouses at",
    "~babbles to, ~banters with, ~fusses over",
    "~chats with, ~cheers up, ~applauds",
    "~offers __ to, ~apologizes to, ~prays with",
    "~makes up with, ~reassures, ~thanks",
    #"DF" "DNF" "DN" "DNB" "DB"
    "whispers to, ~murmurs to, ~bows to",
    "defers to,~fibs to, ~scoffs at",
    "begs from. mumbles to, whines to",
    "begs, sucks up to, gibes" ,
    "~drones on at, ~pleads with, ~toadies to",
    #"DPB" "D"   "Neutral"
    "gives in to, ~chit chats with, ~flatters",
    "murmurs to, ~whispers to, ~stammers at",
    "implore, yield to, request _ from"]
  

SYMLOG_physical_verbs = [
    #"U" "UP" "UPF" "UF"
    "wrestle with, tackle, overthrow, force",
    "save, have sex with, kiss",
    "heal,guide, medicate" ,
    "jail, stop, subdue",
    # "UNF" "UN" "UNB" "UB"
    "stare down, confine constrain",
    "rape, sock, shove",
    "brawl with, slap, jump on" ,
    "chase, rough-house with, hurry",
    # "UPB" "P" "PF" "F"
    "lust for, ~tickle, ~horse around with",
    "snuggle, observe, suckle, feel",
    "comfort, cuddle, draw near to" ,
    "~mesmerize, ~test, ~fetter, ~inject with medicine",
    # "NF" "N" "NB" "B"
    "glare at, ~stare down, ~leer at, ~fetter",
    "torture, molest, injure",
    "maim, paw, run away from",
    "~fuss over, ~flee, ~imitate, ~run away from",
    # "PB" "DP" "DPF" "DF"
    "~look_at, ~visit, ~adorn, ~lust for",
    "lie_on, ~bow to, ~adorn, ~dress",
    "bow to, ~wash, ~lie_on, ~dress",
    "~fetter, ~bow to, ~stare at, ~inject with medicine",
    # "DNF" "DN" "DNB" "DB"
    "frown at, stare at, leer at",
    "peep at, cling to,  submit to, look away from",
    "spit on, hide from, avoid",
    "~submit to, ~hide from, ~avoid, ~cling to",
    # "DPB" "D"    "Neutral"
    "~lie_on, ~adorn, ~visit, ~__",
    "~cling to, ~submit to, ~fetter, ~look away from",
    "tap, nudge, gaze at"]
  

#2004 sentiments
IPA_EPAs_2004 = np.array([2.78, 2.22, 1.20,   2.71, 1.90, 1.78,   1.24, 0.64, 0.32,
            1.03, 1.07, 0.64,   1.12, 0.96, 0.02,   1.98, 1.54, 0.42,
            0.68, 0.81, 0.38,   0.22, 0.25, 0.27,   0.21,  0.38,  0.64,
            -0.86, -0.01, -0.22,   -0.89, 0.19, 0.13,   -1.27, 0.68, 0.93]).reshape((12,3))

IPA_EPAs_1978 = np.array([1.78, 1.29, 0.21, 1.48, 0.91, 1.12, 1.60, 0.78, 0.01,
                          1.28, 1.18, 0.25, 0.88,  1.48,  0.46, 1.68, 1.62, -0.14,
                          0.50, 0.62, 0.45, 0.48, 0.74, 0.16, 0.30, 0.24, 0.09,        
                          -1.00, 0.35, 0.45, -0.89, -0.16, 0.35, -0.82, 0.71, 1.32]).reshape((12,3))

IPA_EPAs_2015 = np.array([
       [ 3.16,  2.83,  0.64],
       [ 2.22,  1.83,  2.09],
       [ 2.57,  1.95,  0.05],
       [ 2.36,  2.14,  1.06],
       [ 0.72,  1.14, -0.9 ],
       [ 2.64,  2.52,  0.33],
       [ 1.01,  1.05,  0.38],
       [ 1.01,  0.88,  0.02],
       [ 0.89,  0.99,  0.2 ],
       [-1.11,  0.77, -0.08],
       [-1.52, -0.26, -0.3 ],
       [-1.33,  1.01,  1.12]])


SYMLOG_directions_EPA_coordinates = np.array([[ 0.   ,  2.121,  2.121],
       [ 1.732,  1.732,  1.732],
       [ 2.121,  2.121,  0.   ],
       [ 0.   ,  3.   ,  0.   ],
       [-2.121,  2.121,  0.   ],
       [-1.732,  1.732,  1.732],
       [-2.121,  0.   ,  2.121],
       [ 0.   ,  0.   ,  3.   ],
       [ 2.121,  0.   ,  2.121],
       [ 3.   ,  0.   ,  0.   ],
       [ 1.732,  1.732, -1.732],
       [ 0.   ,  2.121, -2.121],
       [-1.732,  1.732, -1.732],
       [-3.   ,  0.   ,  0.   ],
       [-1.732, -1.732,  1.732],
       [ 0.   , -2.121,  2.121],
       [ 1.732, -1.732,  1.732],
       [ 1.732, -1.732, -1.732],
       [ 2.121,  0.   ,  2.121],
       [ 0.   ,  0.   , -3.   ],
       [-2.121,  0.   , -2.121],
       [-1.732, -1.732, -1.732],
       [-2.121, -2.121,  0.   ],
       [ 0.   , -3.   ,  0.   ],
       [ 2.121, -2.121,  0.   ],
       [ 0.   , -2.121, -2.121],
       [ 0.   ,  0.   ,  0.   ]])

IPA_categories = [ " gives reinforcement to ",
                  " provides tension release for ",
                  " offers agreement with ",
                  " makes suggestion to ",
                  " gives opinion to ",
                  " gives orientation to ",
                  " requests orientation from ",
                  " requests opinion from ",
                  " requests suggestion from ",
                  " disagrees with ",
                  " shows tension toward ",
                  " is antagonistic toward " ]





