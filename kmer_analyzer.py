#!/usr/bin/env python3

import sys

def read_sequence(file_path):
    """
    Reads a DNA sequence file that contains only raw sequence lines (no headers).
    
    Parameters:
        file_path (str): The path to the input sequence file.
    
    Returns:
        str: A single string representing the full DNA sequence (uppercase).
    """
    with open(file_path, "r") as file:
        # Read each line, strip whitespace (like newline characters), and join into one continuous string
        sequence = ''.join(line.strip() for line in file)
    return sequence.upper()  # Return sequence in uppercase for consistency


def get_kmer_counts(sequence, k):
    """
    Counts the frequency of each k-mer of length `k` in the DNA sequence.

    Parameters:
        sequence (str): The DNA sequence.
        k (int): The length of each k-mer to analyze.

    Returns:
        dict: Dictionary mapping each k-mer to the number of times it appears.
    """
    counts = {}  # Dictionary to store k-mer counts
    for i in range(len(sequence) - k + 1):  # Iterate through the sequence
        kmer = sequence[i:i + k]  # Extract k-mer starting at index i
        counts[kmer] = counts.get(kmer, 0) + 1  # Increment count (initialize to 0 if not present)
    return counts


def get_following_counts(sequence, k):
    """
    For each k-mer, count the frequency of the character that immediately follows it.

    Parameters:
        sequence (str): The DNA sequence.
        k (int): The length of the k-mer.

    Returns:
        dict: Dictionary where each key is a k-mer and each value is another dictionary
              mapping following characters to their counts.
    """
    follow_counts = {}  # Nested dictionary: {kmer: {next_char: count}}
    for i in range(len(sequence) - k):  # Stop before the last full k-mer (needs next char)
        kmer = sequence[i:i + k]        # Get the k-mer
        next_char = sequence[i + k]     # Character that follows the k-mer

        if kmer not in follow_counts:
            follow_counts[kmer] = {}  # Initialize nested dictionary for the k-mer

        # Update the count of the next character
        follow_counts[kmer][next_char] = follow_counts[kmer].get(next_char, 0) + 1

    return follow_counts


def write_output(kmer_counts, follow_counts, output_file):
    """
    Writes the k-mer counts and their following character frequencies to an output file.

    Parameters:
        kmer_counts (dict): Dictionary of k-mer frequencies.
        follow_counts (dict): Dictionary of character frequencies following each k-mer.
        output_file (str): Path to the output file where results will be saved.
    """
    with open(output_file, 'w') as f:
        # Write the header row
        f.write("kmer\tCount\tNextChars\n")

        # Write data for each k-mer in sorted order
        for kmer in sorted(kmer_counts):
            count = kmer_counts[kmer]  # Total count of the k-mer
            next_info = follow_counts.get(kmer, {})  # Get follow counts (or empty if none)

            # Format next characters like "A:5, T:2"
            next_str = ', '.join(f"{char}:{cnt}" for char, cnt in sorted(next_info.items()))

            # Write tab-separated row
            f.write(f"{kmer}\t{count}\t{next_str}\n")


def main():
    """
    Main function to parse command-line arguments and run the k-mer analysis.
    
    Usage:
        python3 kmer_analyzer.py <input_file> <k> <output_file>, where the input_file is the reads.fa file in the shared folder 
    """
    if len(sys.argv) != 4:
        print("Usage: python3 kmer_analyzer.py <input_file> <k> <output_file>")
        sys.exit(1)  # Exit if the wrong number of arguments are provided

    # Read input parameters
    input_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]

    # Step 1: Read the DNA sequence from file
    sequence = read_sequence(input_file)

    # Step 2: Count all k-mers
    kmer_counts = get_kmer_counts(sequence, k)

    # Step 3: Count characters that follow each k-mer
    follow_counts = get_following_counts(sequence, k)

    # Step 4: Write the result to the output file
    write_output(kmer_counts, follow_counts, output_file)

    # Summary output
    print(f"✅ Done! Processed {len(sequence)} bases.")
    print(f"📄 Output written to: {output_file}")


# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
