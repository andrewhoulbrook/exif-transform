#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Transform to extract EXIF using the mighty EXIFTOOL application (covers a massive range of document types)
# Passes a local filepath to EXIFTOOL via CLI. 
# Transform can be attached to a Maltego entity which holds the local filepath as the entity's value.
import sys
import codecs
from bs4 import BeautifulSoup
from MaltegoTransform import *
from subprocess import Popen, PIPE

# Initialize Maltego library
m = MaltegoTransform()

# Handle and clean input string (local filepath)
filepath = sys.argv[1].decode('utf8').strip()

# Form exiftool string to pass CLI
cmd = 'exiftool -h \"{}\"'.format(filepath.encode('utf8'))

try:
    # Use subprocess.Popen to execute the cmd string in CLI
    r = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # Handle results returned in HTML format (HTML table)
    stdout, stderr = r.communicate()
    r.terminate()

    # Check if exiftool threw an error
    if stderr:
        # Pass error message to Maltego UI
        m.addUIMessage("Exiftool Error = {}".format(stderr))

    else:
        meta_data = []

        # Parse exiftool's HTML table of results
        if stdout and stdout is not None:
            # Use the bs4 html parser
            soup = BeautifulSoup(stdout, 'html.parser')

            # Loop over all rows in the html table
            rows = soup.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                meta_data.append('{}: {}'.format(cells[0].text.encode('utf8'), cells[1].text.encode('utf8')))

        # Add each item of meta data as Maltego entities (using custom MetaData entity type)
        for data in meta_data:
            myEntity = m.addEntity('maltego.MetaData', data)
            myEntity.addAdditionalFields('meta-tag', 'Tag', False, data.split(':')[0].strip())
            myEntity.addAdditionalFields('meta-info', 'Data', False, data.split(':')[1].strip())

except Exception as e:
    # Pass error message to Maltego UI
    m.addUIMessage("Unable to launch exiftool via command line.")

# Return entity to Maltego chart
m.returnOutput()
