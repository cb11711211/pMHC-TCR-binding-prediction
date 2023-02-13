# pMHC-TCR binding prediction model
The model is trying to figure out whether the TCR could bound to the MHC-antigen complex using the sequence information of CDR1, CDR2, and CDR3 region from alpha-chain 1 and alpha-chain 2 of TCR, the first and last 3-tide amino acid of antigen peptide, and the classification of the HLA which is the gene name of MHC. During the initial stage, we could simplify the model that utilize the classfication of a rough scale for the HLA. As the experimental designed, the HLA data collected are mostly from Asian (mainly Chinese), and there are several antigen have been checked. In general, the binding pair of pMHC-TCR complex we have examined is nealy 1.6k which could not be sufficient for a large and complex model. We would design the model using simple neural network structures. May be just similar with pMTnet

## Data
The data used in this model contains 3 parts:
1. The TCR sequence data
2. The antigen sequence data
3. The classification of HLA
4. The binding information of TCR and MHC-antigen complex

### TCR data
The TCR data contains the following information:
1. TCR ID
2. CDR1 sequence of alpha-chain 1
3. CDR2 sequence of alpha-chain 1
4. CDR3 sequence of alpha-chain 1
5. CDR1 sequence of alpha-chain 2
6. CDR2 sequence of alpha-chain 2
7. CDR3 sequence of alpha-chain 2

### antigen data
The antigen data contains the following information:
1. Antigen ID
2. First 3-tide amino acid of the antigen peptide
3. Last 3-tide amino acid of the antigen peptide

### HLA data
The HLA data contains the following information:
1. HLA ID
2. HLA classification (mostly for HLA.A)

For most of the asian people, the HLA classification could be roughly divided into several groups:
1. 

## Model
The model of the pMHC-TCR binding prediction contains the following parts:
1. TCR encoding
2. MHC-antigen encoding
3. pMHC-TCR binding prediction

### TCR encoding
The TCR sequence contains several different parts, including the three CDR region of each alpha-chain and the total number of the regions is 6. And each part should be encoded as a vector. The encoding method we used is 