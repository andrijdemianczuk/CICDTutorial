#!/usr/bin/env python

import fire
from src.WikiReader import search_wikipedia


if __name__ == "__main__":
    fire.Fire(search_wikipedia)