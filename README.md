# airtable-attachment-download
Simple Python 3 script to download attachments from Airtable

Your CSV:
Name | attachment
-----|-----
Bob | 4as3fd523sf.jpg
John | screenclip.png

Script downloads these files:
- Bob.jpg
- John.png

# Usage

The name in the first column is used as a name for corresponding attachment. Attachment is expected to be in the second column. File type of attachment is preserved. The names in the first column should to be unique otherwise attachment(s) will get overwritten if they share the same file type.

Download CSV from Airtable
https://support.airtable.com/hc/en-us/articles/202624339-Exporting-Records-in-a-View-to-CSV

Get Python 3
https://www.python.org/downloads/

Get the script
https://github.com/rluks/airtable-attachment-download/releases

Set the input file in aad.py
`filename = '<your csv>.csv'`

Run the aad.py
https://pythonprogramminglanguage.com/how-to-run/

# Notes

Feel free to fork and make changes
