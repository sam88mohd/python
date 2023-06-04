#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import run, glob
from datetime import datetime

styles = getSampleStyleSheet()

def generate_report(attachment, title, contents):
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    story = [report_title]
    for c in contents:
        name = Paragraph("name: " + c['name'])
        weight = Paragraph("weight: " + str(c['weight']) + " lbs")
        # table = Table([["name:", name], ["weight:", weight]], hAlign="LEFT")
        story.append(name)
        story.append(weight)
        story.append(Spacer(10,10))
    report.build(story)

def main():
    contents = []
    attachment = "processed.pdf"
    title = "Processed Update on {}".format(str(datetime.now().date().strftime('%B %d, %Y')))
    for file in glob.glob("supplier-data/descriptions/*.txt"):
        content = run.get_contents(file)
        contents.append(content)
    generate_report(attachment, title, contents)

if __name__ == "__main__":
     main()