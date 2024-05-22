#!/usr/bin/python3
import os
import sys
import time

class SparseMatrix:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.elements = {}

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            numRows = int(lines[0].strip().split('=')[1])
            numCols = int(lines[1].strip().split('=')[1])
            matrix = cls(numRows, numCols)
            
            for line in lines[2:]:
                line = line.strip()
                if not line:
                    continue
                if line[0] != '(' or line[-1] != ')':
                    raise ValueError("Input file has wrong format")
                row, col, value = map(int, line[1:-1].split(','))
                matrix.set_element(row, col, value)
                
            return matrix

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions do not match for addition")
        result = SparseMatrix(self.numRows, self.numCols)
        all_keys = set(self.elements.keys()).union(set(other.elements.keys()))
        for key in all_keys:
            result.set_element(key[0], key[1], self.get_element(key[0], key[1]) + other.get_element(key[0], key[1]))
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions do not match for subtraction")
        result = SparseMatrix(self.numRows, self.numCols)
        all_keys = set(self.elements.keys()).union(set(other.elements.keys()))
        for key in all_keys:
            result.set_element(key[0], key[1], self.get_element(key[0], key[1]) - other.get_element(key[0], key[1]))
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        result = SparseMatrix(self.numRows, other.numCols)
        for (i, k), v in self.elements.items():
            for j in range(other.numCols):
                if (k, j) in other.elements:
                    result.set_element(i, j, result.get_element(i, j) + v * other.elements[(k, j)])
        return result

    def to_string(self):
        result = [f"rows={self.numRows}", f"cols={self.numCols}"]
        for (row, col), value in sorted(self.elements.items()):
            result.append(f"({row}, {col}, {value})")
        return "\n".join(result)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.to_string())

def main():
    input_dir = './sample_inputs/'

    if len(sys.argv) != 3:
        print("Usage: python3 SparseMatrixOperators.py <inputfile1> <inputfile2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    file1_path = os.path.join(input_dir, file1)
    file2_path = os.path.join(input_dir, file2)

    if not os.path.exists(file1_path):
        print(f"File {file1} not found in {input_dir}")
        return

    if not os.path.exists(file2_path):
        print(f"File {file2} not found in {input_dir}")
        return

    matrix1 = SparseMatrix.from_file(file1_path)
    matrix2 = SparseMatrix.from_file(file2_path)

    operation = input("Select operation (add, subtract, multiply): ").strip().lower()
    
    start_time = time.time()

    if operation == 'add':
        result = matrix1.add(matrix2)
        op_suffix = "_sum"
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
        op_suffix = "_diff"
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
        op_suffix = "_product"
    else:
        print("Invalid operation")
        return

    end_time = time.time()
    elapsed_time = end_time - start_time

    output_file = f"{file1}&&{file2}{op_suffix}.txt"
    output_dir = './output/'
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, output_file)

    result.save_to_file(output_file_path)
    print(f"Processed the result in {elapsed_time:.4f} seconds, saved in {output_file_path}")

if __name__ == "__main__":
    main()

