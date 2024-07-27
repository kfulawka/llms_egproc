# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:48:39 2024

@author: fulawka
"""
import re 
import textwrap
from IPython.display import display, HTML

# function for constructing the full prompt
def generate_prompt(prompt, decision_problem, decision_reason, verbal_report):
    """
    Replaces placeholders in the prompt with the given decision problem, decision reason, and verbal report.
    """
    # Replace placeholders with actual values
    filled_prompt = prompt.replace("DECISION_PROBLEM", decision_problem)
    filled_prompt = filled_prompt.replace("DECISION_REASON", decision_reason)
    filled_prompt = filled_prompt.replace("VERBAL_REPORT", verbal_report)

    return filled_prompt

# Function for extracting confidence assessments
def extract_confidence(s):
    """
    Extracts an integer value from a string enclosed between @ or @@ symbols.
    """
    # Regular expression to match patterns like @number@ or @@number@@
    pattern = r'@+(\s*\d+\s*)@+'
    
    # Search for the pattern in the string
    match = re.search(pattern, s)
    
    if match:
        # Extract the number and convert it to an integer
        number_str = match.group(1).strip()
        return int(number_str)
    
    return None

# Function to wrap text
def wrap_text(text, width=100):
    return "<br>".join(textwrap.wrap(text, width))

def disp_tab(dd):
    dd = dd.to_html(escape=False)
    return display(HTML(dd))

# Function to show verbal reports with assigned numbers in a specified range
def show_verbal_reports_in_range(data, reason, min_confidence, max_confidence):
    """
    Shows verbal reports for which the model assigned a confidence within the specified range.
    """
    filtered_data = data[(data[reason] >= min_confidence) & (data[reason] <= max_confidence)] # filter by the specified range

     # wrap the text for nicer display
    filtered_data.loc[:, 'verbal_report'] = filtered_data['verbal_report'].apply(wrap_text)
    filtered_data.loc[:, 'decision_problem'] = filtered_data['decision_problem'].apply(lambda x: wrap_text(x, width=40))

    # select only the columns with report and confidence assesment
    filtered_data = filtered_data[['decision_problem', 'verbal_report', 'choice', reason]]
    filtered_data = filtered_data.to_html(escape=False) # to html
    
    return display(HTML(filtered_data))
    # return filtered_data[['verbal_report', reason]]