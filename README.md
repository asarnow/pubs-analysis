# PUBS 2015 MS Data Analysis

## msanal.py
msanal.py is a skeletal MS data analysis program.

Currently, it supports the following operations:

+ Parse data files using PANDAS
+ "Denormalize" rows containing fields with multiple values
+ Use table join to merge multiple MS data files based on a shared field

## intensities.py
intensities.py reads the proteinGroups.txt table into a PANDAS data frame and
extracts relative intensity matrices for the four sample classes (WCL, WCLp, UB, UBp).