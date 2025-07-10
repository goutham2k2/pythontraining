# test_file_utils.py

from  fileutils import write_to_file, read_from_file

def test_file_io(tmp_path):
    test_file = tmp_path / "test.txt"
    write_to_file(test_file, "Hello, Pytest!")
    content = read_from_file(test_file)
    assert content == "Hello, Pytest!"
