#!/usr/bin/env python

import fire
import src.WikiReader

if __name__ == "__main__":
    #Rather than passing in a specific function like this:
    #fire.Fire(src.WikiReader.summarize_wikipedia())

    #We can instead pass in the library and use the function as an input parameter from the cli invocation itself.
    fire.Fire(src.WikiReader)
