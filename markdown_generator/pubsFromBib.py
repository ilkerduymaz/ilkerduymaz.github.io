#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    # "proceeding": {
    #     "file" : "proceedings.bib",
    #     "venuekey": "booktitle",
    #     "venue-pretext": "In the proceedings of ",
    #     "collection" : {"name":"publications",
    #                     "permalink":"/publication/"}
        
    # },
    "journal":{
        "file": "MyPubs.bib",
        "venuekey" : "journaltitle",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    } 
}

def clean_text(text):
    """Clean text for display, removing unwanted encoding."""
    # Don't escape ampersands and quotes for display
    return text


for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        
        try:
            # Handle both old 'year' field and new 'date' field
            if "date" in b.keys():
                # Parse date field (format: YYYY-MM-DD)
                date_parts = b["date"].split("-")
                pub_year = date_parts[0]
                if len(date_parts) > 1:
                    pub_month = date_parts[1].zfill(2)
                if len(date_parts) > 2:
                    pub_day = date_parts[2].zfill(2)
            elif "year" in b.keys():
                pub_year = f'{b["year"]}'

            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")

            md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
            html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

            #Build Citation from text (APA7 style)
            citation = ""
            
            # APA7 author formatting
            authors = bibdata.entries[bib_id].persons["author"]
            if len(authors) == 1:
                # Single author: Last, F. M.
                author = authors[0]
                citation += author.last_names[0] + ", " + ". ".join([name[0] for name in author.first_names]) + "."
            elif len(authors) <= 20:
                # Multiple authors (up to 20): Last1, F. M., Last2, F. M., & Last3, F. M.
                for i, author in enumerate(authors):
                    if i == len(authors) - 1 and len(authors) > 1:
                        citation += " & "
                    elif i > 0:
                        citation += ", "
                    citation += author.last_names[0] + ", " + ". ".join([name[0] for name in author.first_names]) + "."
            else:
                # More than 20 authors: First 19, ..., Last
                for i in range(19):
                    author = authors[i]
                    if i > 0:
                        citation += ", "
                    citation += author.last_names[0] + ", " + ". ".join([name[0] for name in author.first_names]) + "."
                citation += ", ..., "
                last_author = authors[-1]
                citation += last_author.last_names[0] + ", " + ". ".join([name[0] for name in last_author.first_names]) + "."

            # APA7 year in parentheses
            citation += " (" + pub_year + "). "

            # APA7 title formatting (sentence case, no quotes for articles)
            clean_title = b["title"].replace("{", "").replace("}", "").replace("\\", "")
            citation += clean_text(clean_title) + ". "

            #add venue logic depending on citation type
            # Check if preprint (either by type field or presence of eprinttype)
            is_preprint = (("type" in b.keys() and b["type"].lower() == "preprint") or 
                          "eprinttype" in b.keys())
            
            if is_preprint:
                if "eprinttype" in b.keys():
                    venue_key = "eprinttype"
                elif "publisher" in b.keys():
                    venue_key = "publisher"
                else:
                    # Fallback for preprints without eprinttype or publisher
                    venue = publist[pubsource]["venue-pretext"] + "Preprint"
                    venue_key = None
            else:
                venue_key = publist[pubsource]["venuekey"]

            # Only process venue_key if it's not None and field exists
            if venue_key is not None:
                if venue_key in b.keys():
                    venue = (publist[pubsource]["venue-pretext"] +
                             b[venue_key].replace("{", "").replace("}", "")
                             .replace("\\", ""))
                else:
                    # Handle missing venue field
                    venue = publist[pubsource]["venue-pretext"] + "Unknown Venue"

            # APA7 venue formatting
            if is_preprint:
                # For preprints: venue in italics
                citation += "<em>" + clean_text(venue) + "</em>."
            else:
                # For journal articles: venue in italics
                citation += "<em>" + clean_text(venue) + "</em>."

            
            ## YAML variables
            md = "---\ntitle: \"" + clean_text(b["title"].replace("{", "").replace("}", "").replace("\\", "")) + '"\n'
            
            md += """collection: """ +  publist[pubsource]["collection"]["name"]

            md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
            
            note = False
            if "note" in b.keys():
                if len(str(b["note"])) > 5:
                    md += "\nexcerpt: '" + clean_text(b["note"]) + "'"
                    note = True

            md += "\ndate: " + str(pub_date) 

            md += "\nvenue: '" + clean_text(venue) + "'"
            
            # Add category field based on publication type
            if is_preprint:
                md += "\ncategory: 'preprints'"
            else:
                md += "\ncategory: 'manuscripts'"
            
            url = False
            if "url" in b.keys():
                if len(str(b["url"])) > 5:
                    md += "\npaperurl: '" + b["url"] + "'"
                    url = True

            md += "\ncitation: '" + clean_text(citation) + "'"

            md += "\n---"

            
            ## Markdown description for individual page
            if note:
                md += "\n" + clean_text(b["note"]) + "\n"

            if url:
                md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
            else:
                md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"

            md_filename = os.path.basename(md_filename)

            with open("../_publications/" + md_filename, 'w', encoding="utf-8") as f:
                f.write(md)
            print(f'SUCCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue
