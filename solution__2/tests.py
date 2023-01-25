import csv
import os
import time
import unittest


from random_data_gen import CSVRandomDataGenerator


class TestRandomDataGenerator(unittest.TestCase):
    def test_generate_data(self) -> None :
        generator = CSVRandomDataGenerator(5, "test.csv")
        generator._random_to_file()

        # Check that file was created
        self.assertTrue(os.path.exists("test.csv"))

        # Check that file has correct number of rows
        with open("test.csv") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            self.assertEqual(len(rows), 5)

        # Check that first column is an integer and second column is a string
        for row in rows:
            self.assertIsInstance(int(row[0]), int)
            self.assertIsInstance(row[1], str)

    def test_file_overwrite(self) -> None :
        # Test the case where the filename passed in already exists. 
        # The script should overwrite the existing file.
        with open("test.csv", "w") as file:
            file.write("existing data")
        generator = CSVRandomDataGenerator(5, "test.csv")
        generator._random_to_file()
        with open("test.csv") as file:
            data = file.read()
            self.assertNotEqual(data, "existing data")

    def test_first_column_range(self) -> None :
        # Test that the values in the first column of the generated csv
        # file are within a certain range.
        generator = CSVRandomDataGenerator(5, "test.csv")
        generator._random_to_file()
        with open("test.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                self.assertTrue(int(row[0]) > 999 and int(row[0]) < 10000)

    def test_second_column_length(self) -> None :
        # Test that the values in the second column of the generated csv 
        # file are have a certain length
        generator = CSVRandomDataGenerator(5, "test.csv")
        generator._random_to_file()
        with open("test.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                self.assertEqual(len(row[1]), 13)

    def test_large_file(self) -> None :
        # Test that the script can handle large number of rows and 
        # ensure that the file is not too large
        generator = CSVRandomDataGenerator(1000000, "test.csv")
        generator._random_to_file()
        size = os.path.getsize("test.csv")
        self.assertLess(size, 200000000)

    def test_generate_data_randomness(self) -> None :
        # Test that the generated data is random
        generator = CSVRandomDataGenerator(10, "test.csv")
        generator._random_to_file()
        data = []
        with open("test.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data.append(row)
        generator2 = CSVRandomDataGenerator(10, "test2.csv")
        generator2._random_to_file()
        data2 = []
        with open("test2.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data2.append(row)
        self.assertNotEqual(data, data2)

    def test_generate_data_valid_format(self) -> None :
        # Test that the generated data has a valid file format
        generator = CSVRandomDataGenerator(10, "test.csv")
        generator._random_to_file()
        with open("test.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.assertEqual(len(row), 2)
                self.assertIsInstance(int(row[0]), int)
                self.assertIsInstance(row[1], str)

    def test_generate_data_chunk_size(self) -> None :
        # Test that generated data has a specific chunk size
        generator = CSVRandomDataGenerator(1000000, "test.csv")
        generator.chunk_size = 500000
        generator._random_to_file()
        with open("test.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

    def test_generate_data_zero_rows(self) -> None :
        # Test that the generator return zero rows when passed with a 0 num_rows
        generator = CSVRandomDataGenerator(0, "test.csv")
        generator._random_to_file()
        self.assertTrue(os.path.exists("test.csv"))
        with open("test.csv", "r") as f:
            data = csv.reader(f)
            for row in data:
                self.assertFalse("" in row, f"{row}")

    def tearDown(self) -> None :
        # Remove te test file
        os.remove("test.csv")


def main():
    unittest.main()


if __name__ == "__main__":
    main()