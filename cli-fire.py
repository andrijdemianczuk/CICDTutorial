#!/usr/bin/env python

import fire
# from src.WikiReader import summarize_wikipedia, search_wikipedia
# from src.WikiReader import search_wikipedia
import src.WikiReader


if __name__ == "__main__":
    fire.Fire(src.WikiReader)