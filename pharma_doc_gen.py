import streamlit as st
import datetime
from enum import Enum

# Set page config as the first Streamlit command
st.set_page_config(page_title="Pharma Document Generator", layout="wide")

# Google Analytics tracking code
st.markdown(
    """
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-PJQNLLZRTS"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-PJQNLLZRTS');
    </script>
    """,
    unsafe_allow_html=True
)

# Restore Google site verification
st.markdown(
    """<meta name="google-site-verification" content="ICQemepVIXsFAqgoCeE2gZIkrqoGJZ6SQ4-sL18wCvU" />""",
    unsafe_allow_html=True
)

# Rest of the code remains the same as in the previous artifact
# (All the previous code for SystemCategory, document generation, etc.)

class SystemCategory(Enum):
    HPLC = "HPLC System"
    LIMS = "Laboratory Information Management System"
    SCADA = "SCADA System"
    EMS = "Environmental Monitoring System"
    MES = "Manufacturing Execution System"
    ERP = "Enterprise Resource Planning System"
    CDS = "Chromatography Data System"
    QMS = "Quality Management System"
    CUSTOM = "Custom System"

SYSTEM_TEMPLATES = {
    SystemCategory.HPLC: {
        "description": "High Performance Liquid Chromatography system used for drug substance and product analysis",
        "regulations": "21 CFR Part 11, EU Annex 11, USP <1058>",
        "gamp_category": "4",
        "risk_method": "FMEA",
        "interfaces": "LIMS, CDS, Electronic Notebook",
        "val_approach": "Includes IQ, OQ, PQ with performance verification"
    },
    SystemCategory.LIMS: {
        "description": "Laboratory Information Management System for managing lab workflows, samples, and test results",
        "regulations": "21 CFR Part 11, EU Annex 11, ISO 17025",
        "gamp_category": "4",
        "risk_method": "HACCP",
        "interfaces": "HPLC, CDS, ERP, QMS",
        "val_approach": "Full lifecycle validation including URS, FRS, DS, IQ, OQ, PQ"
    },
    SystemCategory.CUSTOM: {
        "description": "Custom system requiring validation",
        "regulations": "Applicable GMP regulations",
        "gamp_category": "As determined by risk assessment",
        "risk_method": "FMEA or HACCP",
        "interfaces": "To be determined",
        "val_approach": "Risk-based validation approach"
    }
}

def get_system_template(system_category):
    return SYSTEM_TEMPLATES.get(system_category, SYSTEM_TEMPLATES[SystemCategory.CUSTOM])

# Document Generation Functions
def generate_vmp(system_name, system_category):
    template = get_system_template(system_category)
    return f"""
VALIDATION MASTER PLAN

For: {system_name} ({system_category.value})
Document Number: VMP-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0
Effective Date: {datetime.datetime.now().strftime('%Y-%m-%d')}

1. PURPOSE
This Validation Master Plan (VMP) establishes the framework for qualifying and validating the {system_name}
to ensure it meets intended use requirements and complies with {template['regulations']}.

2. SYSTEM DESCRIPTION
{template['description']}

3. VALIDATION APPROACH
3.1 Lifecycle Methodology: GAMP 5 Category {template['gamp_category']}
3.2 Risk Assessment: {template['risk_method']} methodology will be applied
3.3 Validation Stages:
- User Requirements Specification (URS)
- Functional Requirements Specification (FRS)
- Design Qualification (DQ)
- Installation Qualification (IQ)
- Operational Qualification (OQ)
- Performance Qualification (PQ)
3.4 Interfaces: {template['interfaces']}

4. RESPONSIBILITIES
4.1 System Owner: [Name/Title]
4.2 Quality Assurance: QA Department
4.3 Validation Team: Validation Department
4.4 Technical Support: Engineering/IT Department

5. DOCUMENTATION
5.1 Required Documents:
- User Requirements Specification
- Functional Requirements Specification
- Design Documentation
- Test Protocols (IQ/OQ/PQ)
- Validation Summary Report
- Standard Operating Procedures

6. CHANGE CONTROL
All changes will be managed through the Change Control Procedure SOP-XXX.

7. TRAINING
All personnel must complete training on relevant SOPs prior to validation activities.

8. APPROVAL
Prepared By: ________________________    Date: _______________
Reviewed By: ________________________    Date: _______________
Approved By: ________________________    Date: _______________
"""

def generate_urs(system_name, system_category):
    template = get_system_template(system_category)
    return f"""
USER REQUIREMENTS SPECIFICATION

For: {system_name} ({system_category.value})
Document Number: URS-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

1. INTRODUCTION
This document defines the user requirements for the {system_name} to be implemented at [Company Name].

2. SYSTEM DESCRIPTION
{template['description']}

3. REGULATORY REQUIREMENTS
The system shall comply with:
- {template['regulations']}
- Data integrity ALCOA+ principles
- Audit trail requirements for all GxP-relevant changes
- Electronic signature requirements where applicable

4. FUNCTIONAL REQUIREMENTS
4.1 General Requirements:
- System shall be available 99.5% of scheduled uptime
- Data backup shall occur daily with 30-day retention
- System shall maintain complete audit trails
- User access control with role-based permissions

4.2 Specific Requirements:
- [Add system-specific functional requirements here]
- [Example: Automated calculation verification for HPLC results]
- [Example: LIMS shall track sample chain of custody]

5. TECHNICAL REQUIREMENTS
5.1 Hardware:
- Server specifications (if applicable)
- Client workstation requirements
- Network requirements

5.2 Software:
- Operating system requirements
- Database requirements
- Interface requirements

6. VALIDATION REQUIREMENTS
The system shall be validated according to {template['val_approach']}.

7. APPROVAL
Prepared By: ________________________    Date: _______________
Reviewed By: ________________________    Date: _______________
Approved By: ________________________    Date: _______________
"""

def generate_deviation(system_name, system_category):
    return f"""
DEVIATION REPORT

Document Number: DEV-{datetime.datetime.now().strftime('%Y-%m')}-001
System: {system_name} ({system_category.value})

1. DEVIATION DESCRIPTION
[Describe the unexpected event or non-conformance]

2. IMPACT ASSESSMENT
[Describe potential impact on product quality, safety, or efficacy]

3. ROOT CAUSE ANALYSIS
[Investigation findings and identified root cause]

4. CORRECTIVE ACTIONS
[Immediate corrective actions taken]

5. PREVENTIVE ACTIONS
[Long-term preventive actions to avoid recurrence]

Approved By: ________________________    Date: _______________
"""

def generate_risk_assessment(system_name, system_category):
    template = get_system_template(system_category)
    return f"""
RISK ASSESSMENT REPORT

For: {system_name} ({system_category.value})
Document Number: RA-{datetime.datetime.now().strftime('%Y-%m')}-001

1. METHODOLOGY
Risk Assessment Method: {template['risk_method']}

2. RISK EVALUATION
Risk ID | Hazard | Severity | Likelihood | Detectability | RPN | Mitigation
-------|--------|----------|------------|--------------|-----|-----------
1 | [Risk] | [1-10] | [1-10] | [1-10] | [RPN] | [Actions]

3. CONCLUSION
Residual risk after mitigation is [Acceptable/Unacceptable]

Approved By: ________________________    Date: _______________
"""

# Add other document generation functions here (frs, dq, iq, oq, pq, etc.)

DOCUMENT_TYPES = {
    "Validation": {
        "Validation Master Plan (VMP)": generate_vmp,
        "User Requirements (URS)": generate_urs,
        # Add other validation document types
    },
    "QMS": {
        "Deviation Report": generate_deviation,
        "Risk Assessment": generate_risk_assessment,
        # Add other QMS document types
    }
}

def generate_merged_documents(system_name, system_category):
    """
    Generate a merged document containing all validation and QMS documents
    """
    merged_content = f"MERGED DOCUMENTS FOR {system_name} ({system_category.value})\n"
    merged_content += "="*50 + "\n\n"

    # Generate Validation Documents
    merged_content += "VALIDATION DOCUMENTS\n"
    merged_content += "-"*20 + "\n"
    for doc_type, generator in DOCUMENT_TYPES["Validation"].items():
        merged_content += f"\n{doc_type.upper()}\n"
        merged_content += "="*len(doc_type) + "\n"
        merged_content += generator(system_name, system_category)
        merged_content += "\n\n"

    # Generate QMS Documents
    merged_content += "\nQMS DOCUMENTS\n"
    merged_content += "-"*15 + "\n"
    for doc_type, generator in DOCUMENT_TYPES["QMS"].items():
        merged_content += f"\n{doc_type.upper()}\n"
        merged_content += "="*len(doc_type) + "\n"
        merged_content += generator(system_name, system_category)
        merged_content += "\n\n"

    return merged_content

def main():
    st.title("🏭 Pharmaceutical Document Generator")

    # System information
    col1, col2 = st.columns(2)
    with col1:
        system_name = st.text_input("System Name", "HPLC-01")
    with col2:
        system_category = st.selectbox(
            "System Category",
            options=list(SystemCategory),
            format_func=lambda x: x.value
        )

    # Document category selection
    doc_category = st.radio("Document Category", ["Validation", "QMS", "Merged"], horizontal=True)

    # Document type selection
    if doc_category == "Merged":
        doc_types = ["All Documents"]
        doc_type = "All Documents"
    else:
        doc_types = list(DOCUMENT_TYPES[doc_category].keys())
        doc_type = st.selectbox("Select Document Type", doc_types)

    if st.button("Generate Document"):
        if doc_category == "Merged":
            # Generate merged document
            document = generate_merged_documents(system_name, system_category)
            document_title = f"{system_name}_Merged_Documents"
        else:
            # Generate specific document
            generator = DOCUMENT_TYPES[doc_category][doc_type]
            document = generator(system_name, system_category)
            document_title = f"{system_name}_{doc_type.replace(' ', '_')}"

        st.subheader(f"Generated {doc_type}")
        with st.expander("View Document", expanded=True):
            st.text(document)

        st.download_button(
            label="📄 Download Document",
            data=document,
            file_name=f"{document_title}.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
