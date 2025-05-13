import streamlit as st
import datetime
from enum import Enum

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

# VALIDATION DOCUMENT GENERATORS
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
Prepared By: ________________________   Date: _______________
Reviewed By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
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
Prepared By: ________________________   Date: _______________
Reviewed By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
"""

def generate_frs(system_name, system_category):
    template = get_system_template(system_category)
    return f"""
FUNCTIONAL REQUIREMENTS SPECIFICATION
For: {system_name} ({system_category.value})
Document Number: FRS-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

1. SYSTEM OVERVIEW
{template['description']}

2. FUNCTIONAL REQUIREMENTS
2.1 User Interface:
- Role-based access control with at least 5 distinct roles
- Intuitive navigation with menu structure
- Audit trail visualization interface

2.2 Data Management:
- Secure data storage with encryption
- Automated daily backups
- Data export in multiple formats (PDF, CSV, XML)

2.3 System Functions:
- [Add specific system functions based on type]
- [Example for HPLC: Peak integration algorithms]
- [Example for LIMS: Sample tracking workflow]

3. TECHNICAL SPECIFICATIONS
3.1 Hardware Requirements:
- Server: [Specify requirements]
- Workstations: [Specify requirements]
- Peripherals: [If applicable]

3.2 Software Requirements:
- Operating System: [Specify]
- Database: [Specify]
- Middleware: [If applicable]

4. INTERFACES
4.1 System Interfaces:
- {template['interfaces']}
- Data exchange protocols
- API specifications

5. APPROVAL
Prepared By: ________________________   Date: _______________
Reviewed By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
"""

def generate_dq(system_name, system_category):
    return f"""
DESIGN QUALIFICATION PROTOCOL
For: {system_name} ({system_category.value})
Document Number: DQ-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

1. DESIGN OVERVIEW
1.1 System Architecture:
- [Describe hardware/software architecture]
- [Diagram reference if available]

1.2 Design Specifications:
- [List key design specifications]
- [Reference technical documents]

2. COMPLIANCE VERIFICATION
2.1 Regulatory Compliance:
- Verifies compliance with {get_system_template(system_category)['regulations']}

2.2 Requirements Traceability:
- [Table mapping design features to URS requirements]

3. APPROVAL
Verified By: ________________________   Date: _______________
Reviewed By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
"""

def generate_iq(system_name, system_category):
    return f"""
INSTALLATION QUALIFICATION PROTOCOL
For: {system_name} ({system_category.value})
Document Number: IQ-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

1. INSTALLATION VERIFICATION
1.1 Hardware Installation:
- Verified correct installation of all components
- Confirmed proper power supply and connections
- Verified environmental conditions

1.2 Software Installation:
- Verified correct version installed
- Confirmed all required components present
- Verified license activation

2. DOCUMENTATION REVIEW
2.1 Received Documents:
- User manuals
- Installation guides
- Release notes

3. TEST RESULTS
Test ID | Description | Acceptance Criteria | Result | Remarks
--------|-------------|---------------------|--------|--------
IQ-001 | Hardware Install | As per specifications | Pass/Fail | 
IQ-002 | Software Install | Correct version | Pass/Fail |
IQ-003 | Documentation | Complete set | Pass/Fail |

4. APPROVAL
Executed By: ________________________   Date: _______________
Reviewed By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
"""

def generate_oq(system_name, system_category):
    return f"""
OPERATIONAL QUALIFICATION PROTOCOL
For: {system_name} ({system_category.value})
Document Number: OQ-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

1. TEST OBJECTIVE
Verify that the system operates according to specifications under all expected operating conditions.

2. TEST CASES
2.1 Normal Operation:
- [Describe test cases for normal operation]

2.2 Error Conditions:
- [Describe test cases for error handling]

3. ACCEPTANCE CRITERIA
All functions must perform as specified in the FRS.

4. TEST RESULTS
Test ID | Description | Expected Result | Actual Result | Pass/Fail
--------|-------------|-----------------|---------------|----------
OQ-001 | [Test case] | [Expected] | [Actual] | Pass/Fail

5. APPROVAL
Executed By: ________________________   Date: _______________
Reviewed By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
"""

def generate_pq(system_name, system_category):
    return f"""
PERFORMANCE QUALIFICATION PROTOCOL
For: {system_name} ({system_category.value})
Document Number: PQ-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

1. PURPOSE
Verify that the system performs as required under actual operating conditions.

2. TESTING APPROACH
2.1 Testing Conditions:
- Real-world operating environment
- Typical workload conditions

2.2 Performance Metrics:
- [List key performance indicators]
- [Example: System response times]

3. TEST RESULTS
Test ID | Metric | Expected | Actual | Pass/Fail
--------|--------|----------|--------|----------
PQ-001 | [Metric] | [Value] | [Value] | Pass/Fail

4. APPROVAL
Executed By: ________________________   Date: _______________
Reviewed By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
"""

def generate_rtm(system_name, system_category):
    return f"""
REQUIREMENTS TRACEABILITY MATRIX
For: {system_name} ({system_category.value})
Document Number: RTM-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

Requirement ID | URS Reference | FRS Reference | Test Case | Status
--------------|---------------|---------------|-----------|-------
[ID] | [URS Section] | [FRS Section] | [TC-XXX] | Verified

Approved By: ________________________   Date: _______________
"""

def generate_val_summary(system_name, system_category):
    return f"""
VALIDATION SUMMARY REPORT
For: {system_name} ({system_category.value})
Document Number: VSR-{datetime.datetime.now().strftime('%Y-%m')}-001
Version: 1.0

1. VALIDATION ACTIVITIES
1.1 Documents Generated:
- URS, FRS, DQ, IQ, OQ, PQ protocols

1.2 Testing Performed:
- Installation Qualification
- Operational Qualification
- Performance Qualification

2. SUMMARY OF RESULTS
All acceptance criteria were met with no critical deviations.

3. CONCLUSION
The {system_name} has been successfully validated for its intended use.

Approved By: ________________________   Date: _______________
"""

# QMS DOCUMENT GENERATORS
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

Approved By: ________________________   Date: _______________
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

Approved By: ________________________   Date: _______________
"""

def generate_capa(system_name, system_category):
    return f"""
CORRECTIVE AND PREVENTIVE ACTION REPORT
Document Number: CAPA-{datetime.datetime.now().strftime('%Y-%m')}-001
Related System: {system_name} ({system_category.value})

1. PROBLEM STATEMENT
[Describe the quality issue or non-conformance]

2. ROOT CAUSE
[Identified root cause of the issue]

3. CORRECTIVE ACTIONS
[Immediate actions to correct the issue]

4. PREVENTIVE ACTIONS
[Long-term actions to prevent recurrence]

5. EFFECTIVENESS CHECK
[Plan for verifying action effectiveness]

Approved By: ________________________   Date: _______________
"""

def generate_change_control(system_name, system_category):
    return f"""
CHANGE CONTROL RECORD
Document Number: CCR-{datetime.datetime.now().strftime('%Y-%m')}-001
Affected System: {system_name} ({system_category.value})

1. CHANGE DESCRIPTION
[Describe the proposed change in detail]

2. IMPACT ASSESSMENT
[Potential impact on quality, safety, and efficacy]

3. VALIDATION REQUIREMENTS
[Required validation activities for this change]

4. APPROVALS
Requested By: ________________________   Date: _______________
Approved By: ________________________   Date: _______________
"""

def generate_fmea(system_name, system_category):
    template = get_system_template(system_category)
    return f"""
FAILURE MODE AND EFFECTS ANALYSIS
For: {system_name} ({system_category.value})
Document Number: FMEA-{datetime.datetime.now().strftime('%Y-%m')}-001

1. SYSTEM DESCRIPTION
{template['description']}

2. RISK ASSESSMENT
ID | Failure Mode | Effects | S | Causes | O | Controls | D | RPN | Action
---|-------------|--------|---|-------|---|--------|---|-----|------
1 | [Failure] | [Effect] | [1-10] | [Cause] | [1-10] | [Control] | [1-10] | [RPN] | [Action]

3. RISK CONTROL
All RPNs above [threshold] require mitigation actions.

Approved By: ________________________   Date: _______________
"""

DOCUMENT_TYPES = {
    "Validation": {
        "Validation Master Plan (VMP)": generate_vmp,
        "User Requirements (URS)": generate_urs,
        "Functional Requirements (FRS)": generate_frs,
        "Design Qualification (DQ)": generate_dq,
        "Installation Qualification (IQ)": generate_iq,
        "Operational Qualification (OQ)": generate_oq,
        "Performance Qualification (PQ)": generate_pq,
        "Traceability Matrix (RTM)": generate_rtm,
        "Validation Summary Report": generate_val_summary
    },
    "QMS": {
        "Deviation Report": generate_deviation,
        "Risk Assessment": generate_risk_assessment,
        "CAPA Report": generate_capa,
        "Change Control": generate_change_control,
        "FMEA Analysis": generate_fmea
    }
}

def main():
    st.set_page_config(page_title="Pharma Document Generator", layout="wide")
    st.title("🏭 Pharmaceutical Document Generator")
    (
        """
        <meta name="google-site-verification" content="IWzO4ekPofXLKG9Wp187Z2TDvXJStw_NDBZXizqk-Hw" />
        """,
        height=0,  # Set height to 0 to prevent it from taking visible space
    )
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
    doc_category = st.radio("Document Category", ["Validation", "QMS"], horizontal=True)
    
    # Document type selection
    doc_type = st.selectbox("Select Document Type", list(DOCUMENT_TYPES[doc_category].keys()))
    
    if st.button("Generate Document"):
        generator = DOCUMENT_TYPES[doc_category][doc_type]
        document = generator(system_name, system_category)
        
        st.subheader(f"Generated {doc_type}")
        with st.expander("View Document", expanded=True):
            st.text(document)
        
        st.download_button(
            label="📄 Download Document",
            data=document,
            file_name=f"{system_name.replace(' ', '_')}_{doc_type.replace(' ', '_')}.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
