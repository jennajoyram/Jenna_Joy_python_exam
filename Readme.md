## README

#### Jenna Joyram


### Table of Contents

-   [Project Overview](#project-overview)
-   [How to Run the Script](#how-to-run-the-script)
-   [Files](#files)
-   [Expected Output](#expected-output)

---

## **K-mer Analyzer: Analyzing DNA Sequences**


### Project Overview

This project focuses on analyzing DNA sequences by calculating the frequency of each k-mer (a substring of length k) and the frequency of the character immediately following each k-mer. The project includes:

- A Python script, `kmer_analyzer.py`, which processes the DNA sequences, calculates the k-mer frequencies, and generates an output file in a tab-delimited format.
- A test script, `test_kmer_analyzer.py`, which validates the functionality of the main script using `pytest`.

### How to Run the Script

1. **Clone the repository** 

2. **Install the required Python packages**:
   - `pytest` for testing.
   - Any other necessary packages should be installed as described in the script or project setup.
   
3. **Prepare the input file**: Ensure you have the input file `reads.fa`, which is located in the shared folder. This file contains the DNA sequences for analysis.

4. **Run the main script**:
   - Open your terminal or command prompt.
   - Navigate to the folder containing the Python scripts.
   - Use the following command to run the script:
     ```bash
     python3 kmer_analyzer.py <input_file> <k> <output_file>
     ```
     - `reads.fa`: The input file containing the DNA sequences.
     - `k`: The value of k is the length of k-mers to be used for the analysis.
     - `output_file`: The name of the output file where the results will be saved.
     
5. **Run the test script** (optional, but recommended to ensure the script works as expected):
   - In the terminal, run the following command:
     ```bash
     pytest test_kmer_analyzer.py
     ```

### Files

-   `reads.fa`: This is the input file located in the shared folder. It contains the DNA sequences to be analyzed.

-   `kmer_analyzer.py`: The main Python script that processes the DNA sequences, calculates the k-mer frequencies, and writes the results to an output file, named `output_file`.

-   `test_kmer_analyzer.py`: A test script that uses `pytest` to validate the functionality of the `kmer_analyzer.py` script.

### Expected Output

The `output_file` will be in a tab-delimited format, where:

- `kmer` is the sequence of length k.
- `Count` is the number of times the k-mer appears in the input data.
- `NextChars` lists the frequency of the character that follows each k-mer in the DNA sequences.

---


