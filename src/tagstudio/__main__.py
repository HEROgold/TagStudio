import argparse

from .args import TagStudio

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args(namespace=TagStudio())
