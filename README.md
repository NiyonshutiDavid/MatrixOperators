# Sparse Matrix Operations

This project performs operations on sparse matrices stored in files. The supported operations are addition, subtraction, and multiplication. The program reads two sparse matrix files, performs the specified operation, and saves the result to an output file.

## Directory Structure

```
/MatrixOperators/
│
├── SparseMatrixOperators.py    # Main Python script
├──output/  # Directory for output files
│
└── sample_inputs/    # Directory for input files
```

## Cloning the Repository

To clone the repository, run the following command:

```bash
git clone https://github.com/NiyonshutiDavid/MatrixOperators.git
```
## Input File Format

The input files should follow this format:

```
rows=<number_of_rows>
cols=<number_of_cols>
(row_index, col_index, value)
...
```

Example:

```
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)
(0, 165, -933)
(0, 1350, -89)
```

## Usage

### Command-Line Arguments

The script expects two input filenames as command-line arguments.

### Running the Script

Navigate to the `MatrixOperators` directory and run the script with the input filenames:
```bash
cd MatrixOperators
```

```bash
python3 SparseMatrixOperators.py sample1.txt sample2.txt
```

You will be prompted to select an operation
![image](https://github.com/NiyonshutiDavid/MatrixOperators/assets/144002340/7586c8c4-7387-4910-a457-e2ba76a7c1d5)


### Output

The result will be saved in the `output` directory with a filename based on the input filenames and the operation. For example:

```
Processed the result in 0.0123 seconds, saved in output/sample1.txt|adding|sample2.txt_sum.txt
```

## Functions

The `SparseMatrix` class includes the following methods:

- **`__init__(self, numRows, numCols)`**: Initializes the sparse matrix with the specified number of rows and columns.
- **`from_file(cls, file_path)`**: Class method to create a sparse matrix from a file.
- **`set_element(self, row, col, value)`**: Sets the value of an element in the matrix.
- **`get_element(self, row, col)`**: Gets the value of an element in the matrix.
- **`add(self, other)`**: Adds two sparse matrices.
- **`subtract(self, other)`**: Subtracts one sparse matrix from another.
- **`multiply(self, other)`**: Multiplies two sparse matrices.
- **`to_string(self)`**: Converts the sparse matrix to a string representation.
- **`save_to_file(self, file_path)`**: Saves the sparse matrix to a file.

The `main()` function handles:

- Parsing command-line arguments.
- Loading matrices from input files.
- Performing the selected operation.
- Measuring the time taken for the operation.
- Saving the result to the output file.

## Error Handling

- The script will raise an error if the input files have incorrect formats.
- The script will check if the files exist in the specified input directory.
- The script will raise an error if the matrix dimensions do not match the requirements for the selected operation.

## Example

Here’s an example session:

1. Place `sample1.txt` and `sample2.txt` in the `sample_inputs` directory.

2. Run the script:

    ```bash
    python3 SparseMatrixOperators.py sample1.txt sample2.txt
    ```

3. Select an operation:

    ```
    Select operation (add, subtract, multiply): add
    ```

4. The script will output:

    ```
    Processed the result in 0.0123 seconds, saved in /output/sample1.txt|adding|sample2.txt_sum.txt
    ```

## Notes

- Ensure the input files are correctly formatted.
- Adjust paths as necessary based on your actual file structure in your system.

## Author

This project was developed by `David Niyonshuti`. For more information, visit [NiyonshutiDavid](https://github.com/NiyonshutiDavid).

This `README.md` provides a comprehensive overview of the project, including how to clone the repository, usage instructions, function descriptions, and author information.
