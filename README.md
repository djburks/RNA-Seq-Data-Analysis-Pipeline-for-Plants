# RNA-Seq Data Analysis Pipeline for Plants

Data, scripts, and example output to accompany "RNA-Seq Data Analysis Pipeline for Plants: Transcriptome Assembly, Alignment, and Differential Expression Analysis" by DJ Burks and RK Azad.

## Raw_Reads

This folder contains the untrimmed, artificially constructed *Arabidopsis thaliana* FASTQ files.  This should serve as your starting data as you follow along through the tutorial.
Paired-end read pairs are associated by _1 and _2 (e.g. CN1_1.fq.gz and CN1_2.fq.gz).
There are a total of 3 mock conditions (CN, MU, WT) and 3 replicates.

## Example Output

As you progress through the tutorial pipeline, you can compare your resulting output to the files provided here.  A single example from the FASTQC, Trimming, and STAR/Salmon Alignment steps has been provided, and should match your own output if performed correctly.

## Scripts

Scripts that can format your genecount data into import-friendly tables for DESeq2.  Instructions for use are provided in the tutorial.  The STAR2DESEQ.txt and Salmon2DESEQ.txt files need to be updated to reflect your own local file organization.  The first column should contain the file-path for your STAR/Salmon count files.  The second column should contain the condition and a single-digit for the replicate number.  For simplicity, please avoid using spaces in your file paths and condition titles.

## Formatted Count Data

STAR/Salmon-derived gene count data in tabular format for import into DESeq2.  These files can be generated locally by using the Python scripts in the main Scripts folder with the alignment output from STAR and Salmon.

