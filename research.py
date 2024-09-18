from utils import fetch_wikipedia_summary

def generate_prospect_research_report(prospect_name, company_name, additional_info=None): #takes prospect's name, company name, additional information and generates research report using wikipedia API. Secondary functions are in utils.py file.
    print(f"Generating research report for: \nCompany: {company_name}\n")
    company_info = fetch_wikipedia_summary(company_name)
    
    report = f"--- Research Report ---\n\n"
    report += f"Prospect Name: {prospect_name}\n\n"
    report += f"Company Name: {company_name}\n\n"
    
    if additional_info:
        report += f"Additional Information: {additional_info}\n\n"
    
    report += f"Company Info from Wikipedia:\n{company_info}\n\n"
    
    return report