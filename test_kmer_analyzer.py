import pytest
from kmer_analyzer import read_sequence, get_kmer_counts, get_following_counts, write_output

def test_read_sequence(tmp_path):
    """
    Tests the read_sequence function, ensuring that it correctly reads all lines in a sequence
    file, strips whitespace (including \n), and combines all sequence lines into 
    a single uppercase string.

    This test:
    - Creates a temporary file with DNA sequence data.
    - Validates that read_sequence reads the file and returns the correct sequence.
    """
    # Create a temporary file with DNA sequence data
    fasta_file = tmp_path / "test_seq.txt"
    fasta_file.write_text("ACG\nTTG\n")
    # Ensure the function returns the correct concatenated and uppercase sequence
    assert read_sequence(str(fasta_file)) == "ACGTTG"

def test_get_kmer_counts_typical(): #typical test case
    """
    Tests the get_kmer_counts function with a typical DNA sequence and a k-mer length 
    of 3. It ensures that the function correctly counts all k-mers in the sequence.

    This test:
    - Uses a known sequence "ACGACG" and checks the frequency of k-mers of length 3.
    - Asserts that the function returns the correct count of each unique k-mer.
    """
    sequence = "ACGACG"  # Test sequence and k-mer size
    result = get_kmer_counts(sequence, 3) # Get k-mer counts for k=3
    expected = {"ACG": 2, "CGA": 1, "GAC": 1} # Expected k-mer counts
    assert result == expected # Validate that the function returns the expected k-mer counts

def test_get_kmer_counts_edge_k_too_large(): #edge case
    """
    Tests the get_kmer_counts function when the value of k is greater than the sequence length.
    It ensures that no k-mers are returned if k exceeds the length of the DNA sequence.

    This test:
    - Uses a sequence of length 3 ("ACG") and checks the result when k=5.
    - Asserts that the result is an empty dictionary, as no valid k-mers exist.
    """
    sequence = "ACG"  # Test sequence with length 3 and k-mer size 5
    result = get_kmer_counts(sequence, 5)  # Get k-mer counts for k=5, which is larger than the sequence length
    assert result == {}  # Validate that the result is an empty dictionary as no valid k-mers can be generated

def test_get_following_counts_typical():
    """
    Tests the get_following_counts function with a typical DNA sequence and a k-mer length of 2.
    It checks if the function counts the frequencies of the character following each k-mer.

    This test:
    - Uses the sequence "ACGTG" and ensures that the following characters for each k-mer are counted.
    - Asserts that the function returns the correct frequency of next characters after each k-mer.
    """
    sequence = "ACGTG" # Test sequence and k-mer size
    result = get_following_counts(sequence, 2) # Get following character counts for k-mer size 2
    expected = {        # Expected next character counts for each k-mer
        "AC": {"G": 1},
        "CG": {"T": 1},
        "GT": {"G": 1}
    }
    assert result == expected # Validate the result matches the expected counts

def test_get_following_counts_edge_no_follow():
    """
    Tests the get_following_counts function with a sequence where the last k-mer has no following character.
    It ensures the function handles this edge case correctly by not including a following character for the last k-mer.

    This test:
    - Uses a sequence "AAA" and ensures that only valid following characters are counted for k-mers.
    - Asserts that the last k-mer "AA" has a following character count, but the final character ("A") does not.
    """
    sequence = "AAA"  # Test sequence with no following character for the last k-mer
    result = get_following_counts(sequence, 2) # Get following character counts for k-mer size 2
    expected = {"AA": {"A": 1}} # Expected next character counts for k-mer "AA"
    assert result == expected # Validate that only valid k-mers with a following character are counted

def test_write_output(tmp_path):
    """
    Tests the write_output function, verifying that it writes the k-mer counts and 
    the following character frequencies to a tab-delimited output file in the correct format.

    This test:
    - Provides sample k-mer and following character counts.
    - Validates that the output file contains the expected header and data rows.
    - Ensures the format is correct, using tab-delimited values and matching the expected structure.
    """
    output_file = tmp_path / "results.tsv" # Create a temporary output file for the results
    kmer_counts = {"AA": 3, "AC": 1} # Sample k-mer and following character counts
    follow_counts = {"AA": {"A": 3}, "AC": {}} 

    write_output(kmer_counts, follow_counts, str(output_file)) # Call the function to write results to the file

    content = output_file.read_text().strip().split("\n") # Read the content of the output file and split by lines
    assert content[0] == "kmer\tCount\tNextChars"  # Validate the header
    assert content[1] == "AA\t3\tA:3"   # Validate the first data row (k-mer AA with following character A:3)
    assert content[2] == "AC\t1"  # # Validate the second data row (no following characters, so no trailing tab)

if __name__ == "__main__":
    """
    To run this test script, ensure you have pytest installed and use the following command:

    Usage:
        pytest test_kmer_analyzer.py

    This will automatically discover and run all tests defined in the script.
    """
    pytest.main()
