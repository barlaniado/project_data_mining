import sys
import os
sys.path.append(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir))))
import main_file


def main():
    """
    This function will run the same way as main_file.py but the log set level will be DEBUG and not INFO.
    """
    main_file.main()


if __name__ == "__main__":
    main()
