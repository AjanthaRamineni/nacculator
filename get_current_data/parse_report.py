import sys
import os
import xml.etree.ElementTree as ET
from email.mime.text import MIMEText
from jinja2 import Environment

import send_email as sm


def generate_report_csv(input_file):

    print "Calling pdf2txt"

    cmd = 'pdf2txt.py -o out.xml ' + input_file
    os.system(cmd)
    filename = 'out.xml'

    print "Called Pdf2Txt"
    tree = ET.parse(filename)
    pages = tree.getroot()
    final_result = {}
    print "Checking xml IDS"
    for iter in pages[0].findall('textbox'):
        # ADC IDs Total
        if iter.attrib['id'] == '16':
            result = []
            for t_iter in iter.findall('textline')[-1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['ADC IDs Total'] = ''.join(result)

        # ADC Percentage
        if iter.attrib['id'] == '14':
            result = []
            for t_iter in iter.findall('textline')[-1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['ADC Percentage'] = ''.join(result)

        # Autopsies
        if iter.attrib['id'] == '17':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['Autopsies'] = ''.join(result)

        # Autopsies Percentage
        if iter.attrib['id'] == '15':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['Autopsies Percentage'] = ''.join(result)

        # NP Forms
        if iter.attrib['id'] == '17':
            result = []
            for t_iter in iter.findall('textline')[1].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['NP Forms'] = ''.join(result)

        # 6+
        if iter.attrib['id'] == '2':
            result = []
            for t_iter in iter.findall('textline')[3].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['6+'] = ''.join(result)

        # <6
        if iter.attrib['id'] == '3':
            result = []
            for t_iter in iter.findall('textline')[3].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            final_result['<6'] = ''.join(result)

        # Date Entered
        if iter.attrib['id'] == '1':
            result = []
            for t_iter in iter.findall('textline')[0].findall('text'):
                if t_iter.text.strip():
                    result.append(t_iter.text)
            result = str.replace(''.join(result), 'Asof', '')
            final_result['Date Entered'] = result

    print final_result


    TEMPLATE = """
    <html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
    <table style="width:100%"; border="1">
    <!-- table header -->
    {% if final_result %}
        <tr>
            {% for key in final_result.keys() %}
                <td> {{ key }} </td>
            {% endfor %}
        </tr>
    <!-- table rows -->
        <tr>
            {% for value in final_result.values() %}
                <td> {{ value }} </td>
            {% endfor %}
        </tr>
    {% endif %}
    </table>
    <body>
    </body>
    </html>
    """  # Our HTML Template

    # Create a text/html message from a rendered template
    msg = MIMEText(
        Environment().from_string(TEMPLATE).render(
            title='NACC REPORT',
            final_result=final_result
        ), "html"
    )
    sm.send_email('NACC REPORT', msg)


def main(argc):
    input_file = argc
    generate_report_csv(input_file)


if __name__ == '__main__':
    main(sys.argv[1])
