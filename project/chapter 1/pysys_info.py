#!/usr/bin/python3
# A simple script to show sys info
import subprocess

def call_uname():
    uname = "uname"
    uname_arg = "-a"

    print(f"Gathering system information with {uname} command:\n")
    subprocess.call([uname, uname_arg])

def call_df():
    df = "df"
    df_arg = "-l"
    print(f"Gathering system information with {df} command:\n")
    subprocess.call([df, df_arg])

def sep():
    print("*" * 100)

def main():
    sep()
    call_uname()
    sep()
    call_df()
    sep()

if __name__ == "__main__":
    main()
