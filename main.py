import re
from difflib import SequenceMatcher


# ============================================================
# GKS APPLICANT ASSISTANT
# Version 1.0
# Student-built rule-based NLP-style chatbot
# ============================================================


BOT_NAME = "GKS Applicant Assistant"
CURRENT_GKS_CYCLE = "2027"


# ============================================================
# SYNONYMS
# ============================================================

synonyms = {
    "required": [
        "required",
        "require",
        "needed",
        "need",
        "necessary",
        "compulsory",
        "mandatory"
    ],

    "documents": [
        "documents",
        "document",
        "papers",
        "paperwork",
        "certificates"
    ],

    "apply": [
        "apply",
        "application",
        "submit",
        "submission"
    ],

    "eligibility": [
        "eligibility",
        "eligible",
        "qualify",
        "qualification"
    ],

    "university": [
        "university",
        "universities",
        "college",
        "institution"
    ],

    "major": [
        "major",
        "course",
        "program",
        "programme",
        "field",
        "department"
    ],

    "interview": [
        "interview",
        "interviews",
        "oral interview",
        "selection interview"
    ],

    "scholarship": [
        "scholarship",
        "funding",
        "financial support"
    ],

    "english_test": [
        "ielts",
        "toefl",
        "english test",
        "english proficiency"
    ],

    "korean_test": [
        "topik",
        "korean test",
        "korean proficiency"
    ],

    "transcript": [
        "transcript",
        "academic transcript",
        "grade transcript"
    ],

    "recommendation": [
        "recommendation letter",
        "recommendation",
        "lor",
        "letter of recommendation"
    ]
}


# ============================================================
# TYPO / SIMILARITY FUNCTIONS
# ============================================================

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def tokenize(text):
    return re.findall(r"\b[a-zA-Z0-9'-]+\b", text)


# ============================================================
# KNOWLEDGE BASE
# ============================================================

knowledge_base = {

    "gks": {
        "patterns": [
            r"\bgks\b",
            r"global korea scholarship",
            r"what is gks"
        ],
        "answer": (
            "GKS stands for Global Korea Scholarship. It is a Korean "
            "government scholarship program for international students. "
            "For undergraduate applicants, the program can include Korean "
            "language training and degree study, along with scholarship "
            "support. Always check the latest official GKS-U guidelines "
            "for the application year."
        )
    },

    "gks_u": {
        "patterns": [
            r"\bgks[- ]?u\b",
            r"undergraduate gks",
            r"gks undergraduate",
            r"bachelor.*gks"
        ],
        "answer": (
            "GKS-U refers to the undergraduate Global Korea Scholarship. "
            "It is intended for international students applying for "
            "undergraduate or eligible associate-degree programs. "
            "The exact eligibility, schedule, documents and university "
            "list depend on the application cycle."
        )
    },

    "eligibility": {
        "patterns": [
            r"eligib",
            r"qualif",
            r"who can apply",
            r"can i apply"
        ],
        "answer": (
            "GKS-U eligibility includes requirements related to nationality, "
            "age, education and academic performance. Applicants and their "
            "parents must meet the applicable nationality requirements, and "
            "the applicant must satisfy the age and academic criteria in "
            "the current GKS-U guidelines. Check the official guideline "
            "for your exact application year."
        )
    },

    "age": {
        "patterns": [
            r"\bage\b",
            r"how old",
            r"age limit",
            r"maximum age"
        ],
        "answer": (
            "The GKS-U age requirement is defined in the official guideline "
            "for each application cycle. For the current 2027 cycle, check "
            "the official GKS-U Application Guidelines for the exact "
            "cut-off date and age condition."
        )
    },

    "academic_requirement": {
        "patterns": [
            r"academic requirement",
            r"academic score",
            r"minimum score",
            r"marks required",
            r"percentage required",
            r"80 percent",
            r"top 20"
        ],
        "answer": (
            "GKS-U has an academic performance requirement. The current "
            "official information includes routes based on cumulative "
            "academic performance or class ranking/CGPA criteria. "
            "The exact calculation and acceptable academic records should "
            "be checked in the current application guideline."
        )
    },

    "school_grades": {
        "patterns": [
            r"class 10",
            r"class 11",
            r"class 12",
            r"school marks",
            r"school grades"
        ],
        "answer": (
            "GKS-U applications may require academic records from your "
            "school years. Which records must be submitted and how they "
            "should be calculated depends on the current application "
            "guidelines and your education system."
        )
    },

    "pending_graduation": {
        "patterns": [
            r"expected to graduate",
            r"pending graduation",
            r"still in school",
            r"not graduated"
        ],
        "answer": (
            "Students who are expected to graduate may be eligible if they "
            "meet the conditions stated in the current GKS-U guideline. "
            "You must submit the required graduation-related certificate "
            "or proof by the applicable deadline."
        )
    },

    "gap_year": {
        "patterns": [
            r"gap year",
            r"gap-year",
            r"year gap",
            r"drop year"
        ],
        "answer": (
            "A gap year does not automatically mean you cannot apply. "
            "However, you should check the current GKS-U eligibility "
            "conditions and accurately explain your academic timeline "
            "where required."
        )
    },

    "academic_stream": {
        "patterns": [
            r"stream",
            r"pcb",
            r"pcm",
            r"commerce",
            r"biology background",
            r"science stream"
        ],
        "answer": (
            "Your academic stream matters mainly in relation to the "
            "eligibility and department requirements of the university "
            "and major you choose. Always check the university information "
            "file for the specific department."
        )
    },

    "cs_without_math": {
        "patterns": [
            r"computer science without math",
            r"cs without maths",
            r"computer science no math",
            r"ai without math",
            r"no mathematics"
        ],
        "answer": (
            "Not having Mathematics does not automatically answer whether "
            "you can enter a particular CS or AI program. The decisive "
            "factor is the eligibility requirement of the specific "
            "university and department. Check the official university "
            "information for the program before applying."
        )
    },

    "ielts": {
        "patterns": [
            r"\bielts\b",
            r"\btoefl\b",
            r"english test",
            r"english proficiency",
            r"english certificate"
        ],
        "answer": (
            "English-test requirements can depend on the application "
            "track, university and program. IELTS is not something you "
            "should assume is universally mandatory for every GKS-U "
            "application. Check the current GKS-U guideline and the "
            "specific university information."
        )
    },

    "topik": {
        "patterns": [
            r"\btopik\b",
            r"korean proficiency",
            r"korean test"
        ],
        "answer": (
            "TOPIK is the Test of Proficiency in Korean. Korean-language "
            "ability can be useful, but whether a TOPIK score is required "
            "depends on the current GKS-U requirements and program."
        )
    },

    "korean_before_application": {
        "patterns": [
            r"korean before applying",
            r"learn korean before",
            r"do i need korean",
            r"korean language before application"
        ],
        "answer": (
            "You do not need to assume that you must already be fluent in "
            "Korean before applying. GKS undergraduate programs can include "
            "Korean language training. However, check the current guideline "
            "and your chosen university's requirements."
        )
    },

    "embassy_track": {
        "patterns": [
            r"embassy track",
            r"embassy",
            r"apply through embassy"
        ],
        "answer": (
            "Embassy Track means applying through the Korean embassy or "
            "consulate according to the current GKS-U application procedure. "
            "The exact submission method, quota and university-choice rules "
            "must be checked in the current year's guideline."
        )
    },

    "university_track": {
        "patterns": [
            r"university track",
            r"university directly",
            r"apply directly to university"
        ],
        "answer": (
            "University Track means applying directly to a GKS-designated "
            "university. The university conducts its part of the selection "
            "process according to the current GKS-U rules."
        )
    },

    "uic": {
        "patterns": [
            r"\buic\b",
            r"university industry cooperation",
            r"industry university cooperation",
            r"university[- ]industry cooperation"
        ],
        "answer": (
            "UIC stands for University-Industry Cooperation. In GKS-U, "
            "the UIC program is a University Track specialization focused "
            "on science and engineering fields with customized curriculum "
            "and industry-university cooperation. The current 2027 official "
            "information lists Inje University among the UIC bachelor's "
            "universities. Always verify the available department in the "
            "current University Information file."
        )
    },

    "track_comparison": {
        "patterns": [
            r"which track",
            r"track.*better",
            r"better.*track",
            r"compare.*track",
            r"difference.*track",
            r"tracks"
        ],
        "answer": (
            "Embassy Track and University Track are different application "
            "routes. Embassy Track goes through the Korean embassy/official "
            "application system, while University Track is submitted "
            "directly to a designated university. UIC is a University Track "
            "program. The best route depends on your eligibility, university "
            "choice and the current year's rules."
        )
    },

    "application_schedule": {
        "patterns": [
            r"application date",
            r"application deadline",
            r"when.*apply",
            r"when.*open",
            r"schedule",
            r"deadline"
        ],
        "answer": (
            "GKS-U application dates vary by year and track. For the 2027 "
            "cycle, the official GKS notice and application guideline are "
            "the authoritative sources for exact deadlines. Do not rely "
            "on dates from an older GKS cycle."
        )
    },

    "application_fee": {
        "patterns": [
            r"application fee",
            r"apply fee",
            r"registration fee",
            r"how much.*apply"
        ],
        "answer": (
            "Do not assume that every part of the GKS application has the "
            "same fee structure. Check the current GKS guideline and any "
            "university-specific submission instructions for your track."
        )
    },

    "application_editing": {
        "patterns": [
            r"edit application",
            r"change application",
            r"modify application",
            r"mistake.*application"
        ],
        "answer": (
            "Whether you can edit an application after submission depends "
            "on the application system and stage. If you notice an error, "
            "check the current official instructions immediately rather "
            "than assuming that changes are possible."
        )
    },

    "application_status": {
        "patterns": [
            r"application status",
            r"check status",
            r"result status",
            r"selection status"
        ],
        "answer": (
            "Application status and results are announced through the "
            "relevant official channel for your track. Check the official "
            "GKS system, embassy or university instructions as applicable."
        )
    },

    "documents": {
        "patterns": [
            r"what documents",
            r"documents.*gks",
            r"required documents",
            r"documents.*required",
            r"paperwork"
        ],
        "answer": (
            "Typical GKS-U documentation can include academic records, "
            "citizenship/family documents, personal statement, study plan, "
            "recommendation letter and other forms or certificates. "
            "The exact document list, authentication requirements and "
            "submission format must be taken from the current GKS-U "
            "guideline and your track's instructions."
        )
    },

    "transcript": {
        "patterns": [
            r"\btranscript\b",
            r"academic transcript",
            r"grade transcript"
        ],
        "answer": (
            "A transcript is an official academic record showing grades or "
            "subjects according to the issuing institution. If your school "
            "does not issue a conventional transcript, do not automatically "
            "replace it with another document. Check the current GKS-U "
            "guideline and ask the relevant application authority what "
            "substitute documentation is accepted."
        )
    },

    "school_certificate": {
        "patterns": [
            r"school certificate",
            r"graduation certificate",
            r"certificate.*school"
        ],
        "answer": (
            "School certificates may be required to prove enrollment, "
            "graduation or expected graduation. The exact certificate "
            "depends on the applicant's status and the current guideline."
        )
    },

    "apostille": {
        "patterns": [
            r"apostille",
            r"apostilled",
            r"apostille certificate"
        ],
        "answer": (
            "Apostille requirements depend on the document and the current "
            "GKS-U instructions. Do not apostille every document blindly. "
            "Follow the current guideline and the instructions of the "
            "authority receiving your documents."
        )
    },

    "notarization": {
        "patterns": [
            r"notar",
            r"notary",
            r"notarization",
            r"notarized"
        ],
        "answer": (
            "Notarization and authentication are different processes. "
            "Whether a document needs notarization depends on the current "
            "GKS-U document instructions and the authority receiving it."
        )
    },

    "translation": {
        "patterns": [
            r"translation",
            r"translated document",
            r"translate documents",
            r"korean translation"
        ],
        "answer": (
            "If a required document is not in an accepted language, a "
            "translation may be required. Follow the current GKS-U "
            "guideline for the accepted language, certification and "
            "authentication method."
        )
    },

    "citizenship_documents": {
        "patterns": [
            r"citizenship document",
            r"nationality document",
            r"proof of nationality"
        ],
        "answer": (
            "Citizenship or nationality documents may be required to verify "
            "the applicant's and parents' nationality. Use the documents "
            "specified in the current GKS-U guideline."
        )
    },

    "parent_documents": {
        "patterns": [
            r"parents.*document",
            r"parent.*nationality",
            r"father.*document",
            r"mother.*document"
        ],
        "answer": (
            "Parent-related documents may be required for nationality or "
            "family-relation verification. The exact acceptable documents "
            "are specified in the current GKS-U application guideline."
        )
    },

    "family_relationship": {
        "patterns": [
            r"family relationship",
            r"proof.*relationship",
            r"family.*certificate",
            r"birth certificate"
        ],
        "answer": (
            "Family-relation documents may be used to establish the "
            "relationship between the applicant and parents. Follow the "
            "current document checklist for acceptable evidence."
        )
    },

    "passport": {
        "patterns": [
            r"\bpassport\b",
            r"passport required",
            r"passport document"
        ],
        "answer": (
            "Passport requirements depend on the current application "
            "procedure. If a passport is not available at an early stage, "
            "check the current guideline for what identity document or "
            "alternative is accepted."
        )
    },

    "document_scanning": {
        "patterns": [
            r"scan documents",
            r"scanned documents",
            r"pdf documents",
            r"document format"
        ],
        "answer": (
            "Submit documents in the exact file format, size and resolution "
            "specified by the current application system or university. "
            "Keep scans clear and make sure every required page is visible."
        )
    },

    "personal_statement": {
        "patterns": [
            r"personal statement",
            r"personal essay",
            r"sop",
            r"statement of purpose"
        ],
        "answer": (
            "A strong GKS personal statement should explain your background, "
            "motivation, experiences and reasons for pursuing study in "
            "Korea. Focus on authentic experiences rather than generic "
            "claims or copied scholarship language."
        )
    },

    "personal_statement_story": {
        "patterns": [
            r"story.*personal statement",
            r"storytelling.*sop",
            r"how.*write.*personal statement",
            r"make.*sop.*interesting"
        ],
        "answer": (
            "Storytelling can make a personal statement stronger when it is "
            "used to demonstrate genuine development. A useful structure is "
            "experience → realization → action → growth → future direction."
        )
    },

    "why_korea": {
        "patterns": [
            r"why korea",
            r"why.*study.*korea"
        ],
        "answer": (
            "For 'Why Korea?', connect your academic goals with specific "
            "features of Korean higher education, technology, industry or "
            "academic opportunities. Avoid relying only on entertainment "
            "or pop-culture reasons."
        )
    },

    "why_gks": {
        "patterns": [
            r"why gks",
            r"why.*scholarship",
            r"why.*global korea"
        ],
        "answer": (
            "For 'Why GKS?', explain how the scholarship supports your "
            "academic and personal goals. Focus on opportunities, education, "
            "international experience and your intended contribution."
        )
    },

    "why_major": {
        "patterns": [
            r"why.*major",
            r"why.*course",
            r"why.*department"
        ],
        "answer": (
            "For 'Why this major?', connect your previous experiences, "
            "skills and interests with the specific field. Then explain "
            "what you want to learn and how you plan to use it in the future."
        )
    },

    "career_goals": {
        "patterns": [
            r"career goal",
            r"future career",
            r"career plans",
            r"future plans"
        ],
        "answer": (
            "Career goals should be realistic and connected to your chosen "
            "major. Explain what skills you want to develop, what kind of "
            "work interests you and how your studies will help you reach "
            "that direction."
        )
    },

    "achievements_activities": {
        "patterns": [
            r"achievement",
            r"extracurricular",
            r"activities",
            r"volunteer",
            r"award"
        ],
        "answer": (
            "Include achievements and activities that genuinely demonstrate "
            "your skills, initiative, leadership, curiosity or growth. "
            "Quality and relevance are generally more useful than listing "
            "everything you have ever done."
        )
    },

    "low_marks": {
        "patterns": [
            r"low marks",
            r"bad marks",
            r"weak marks",
            r"low score",
            r"poor grades"
        ],
        "answer": (
            "If you have weaker marks in a particular period, do not hide "
            "or misrepresent them. Focus on your overall academic record, "
            "improvement, relevant strengths and what you learned."
        )
    },

    "study_plan": {
        "patterns": [
            r"study plan",
            r"academic plan",
            r"study.*plan"
        ],
        "answer": (
            "A strong study plan should explain what you intend to learn, "
            "how you will develop academically, and how your chosen "
            "university and major fit into that plan. Keep it specific and "
            "realistic."
        )
    },

    "study_plan_vs_personal_statement": {
        "patterns": [
            r"study plan.*personal statement",
            r"personal statement.*study plan",
            r"difference.*study plan",
            r"difference.*personal statement"
        ],
        "answer": (
            "The personal statement is mainly about who you are, your "
            "background, motivation and experiences. The study plan is more "
            "focused on what you intend to study, how you will study it and "
            "your academic direction."
        )
    },

    "recommendation_letter": {
        "patterns": [
            r"recommendation letter",
            r"\blor\b",
            r"letter of recommendation"
        ],
        "answer": (
            "A recommendation letter should come from an appropriate "
            "recommender who can genuinely evaluate your academic ability, "
            "character and potential. Follow the current GKS-U guideline "
            "for the exact recommender and submission requirements."
        )
    },

    "lor_teacher": {
        "patterns": [
            r"teacher.*lor",
            r"teacher.*recommendation",
            r"professor.*recommendation"
        ],
        "answer": (
            "A teacher can be a strong recommender when they have directly "
            "taught you and can provide specific evidence about your "
            "academic ability, work habits and potential. Follow the current "
            "application guideline for eligibility."
        )
    },

    "lor_signature": {
        "patterns": [
            r"lor.*signature",
            r"recommendation.*signature",
            r"signed.*recommendation"
        ],
        "answer": (
            "Follow the current GKS-U instructions regarding signatures, "
            "seals and submission format. Do not assume that an informal "
            "digital signature is acceptable."
        )
    },

    "lor_length": {
        "patterns": [
            r"lor.*length",
            r"recommendation.*length",
            r"how long.*recommendation"
        ],
        "answer": (
            "Recommendation-letter length and formatting should follow the "
            "current GKS-U application form or guideline. Avoid making the "
            "letter unnecessarily long just to increase word count."
        )
    },

    "university_selection": {
        "patterns": [
            r"choose university",
            r"select university",
            r"which university",
            r"university choice"
        ],
        "answer": (
            "Choose universities based on your academic eligibility, major "
            "availability, curriculum, language, location and career goals. "
            "For GKS, always confirm that the university and department are "
            "actually included in the current University Information file."
        )
    },

    "major_availability": {
        "patterns": [
            r"major available",
            r"is.*major.*available",
            r"department available",
            r"course available"
        ],
        "answer": (
            "Major availability can change between GKS cycles. Check the "
            "current University Information file for the exact university "
            "and department before finalizing your application."
        )
    },

    "major_change": {
        "patterns": [
            r"change major",
            r"change department",
            r"switch major",
            r"change course"
        ],
        "answer": (
            "Changing a major after selection may be restricted and depends "
            "on the scholarship rules and university. Do not assume that "
            "a major can be freely changed after selection."
        )
    },

    "english_program": {
        "patterns": [
            r"english program",
            r"program in english",
            r"english taught"
        ],
        "answer": (
            "Whether a program is taught in English depends on the specific "
            "department and university. Check the official university "
            "information rather than assuming the whole university uses "
            "English."
        )
    },

    "university_research": {
        "patterns": [
            r"research university",
            r"research.*university",
            r"how.*research.*university"
        ],
        "answer": (
            "When researching a university, compare the exact department, "
            "curriculum, faculty, labs, industry connections, language of "
            "instruction and student opportunities."
        )
    },

    "selection_process": {
        "patterns": [
            r"selection process",
            r"how.*selected",
            r"selection.*gks",
            r"rounds"
        ],
        "answer": (
            "GKS selection generally involves multiple stages, but the exact "
            "process differs by track and application year. Read the current "
            "GKS-U guideline and the instructions from the authority handling "
            "your first-round selection."
        )
    },

    "interview": {
        "patterns": [
            r"\binterview\b",
            r"interview round",
            r"oral"
        ],
        "answer": (
            "GKS interviews can assess your motivation, academic goals, "
            "study plans, personality and understanding of your chosen "
            "program. Prepare concise, honest answers and know your own "
            "application thoroughly."
        )
    },

    "interview_why_questions": {
        "patterns": [
            r"interview.*why",
            r"why.*interview",
            r"common interview questions"
        ],
        "answer": (
            "Common areas include: Why Korea? Why GKS? Why this university? "
            "Why this major? What are your career goals? What challenges "
            "might you face in Korea? Prepare from your own application "
            "rather than memorizing generic answers."
        )
    },

    "interview_mistakes": {
        "patterns": [
            r"interview mistakes",
            r"mistakes.*interview",
            r"what not to say"
        ],
        "answer": (
            "Avoid memorized-sounding answers, exaggerated achievements, "
            "contradictions with your application and unsupported claims. "
            "If you do not know something, answer honestly instead of "
            "inventing information."
        )
    },

    "benefits": {
        "patterns": [
            r"scholarship benefits",
            r"benefits.*gks",
            r"what.*gks.*cover",
            r"what does gks cover"
        ],
        "answer": (
            "GKS benefits can include airfare, Korean language training "
            "support, tuition and monthly allowances. Exact benefits and "
            "amounts are determined by the current GKS-U guidelines."
        )
    },

    "monthly_allowance": {
        "patterns": [
            r"monthly allowance",
            r"monthly stipend",
            r"stipend",
            r"monthly money"
        ],
        "answer": (
            "GKS provides monthly financial support under the scholarship "
            "benefits. The exact amount can change by program and cycle, so "
            "check the current official GKS-U guideline rather than relying "
            "on an old figure."
        )
    },

    "settlement": {
        "patterns": [
            r"settlement allowance",
            r"settlement money",
            r"initial allowance"
        ],
        "answer": (
            "Some GKS benefits can include support related to settlement or "
            "arrival. The exact amount and conditions should be checked in "
            "the current GKS-U guideline."
        )
    },

    "language_program": {
        "patterns": [
            r"language program",
            r"korean language training",
            r"language training"
        ],
        "answer": (
            "GKS undergraduate programs can include Korean language training "
            "before degree study. The duration and conditions depend on the "
            "current scholarship rules and any applicable exemption."
        )
    },

    "language_program_difficulty": {
        "patterns": [
            r"korean language.*difficult",
            r"language training.*hard",
            r"is korean.*difficult"
        ],
        "answer": (
            "Learning Korean can be challenging, especially while adapting "
            "to a new academic environment. A practical approach is to "
            "start with basic reading, vocabulary, grammar and everyday "
            "communication before arrival."
        )
    },

    "topik_exemption": {
        "patterns": [
            r"topik exemption",
            r"language exemption",
            r"exempt.*korean"
        ],
        "answer": (
            "Language-training exemptions or exceptions depend on the "
            "current GKS rules and your qualifications. Check the current "
            "guideline for the exact conditions."
        )
    },

    "after_selection": {
        "patterns": [
            r"after selection",
            r"after getting selected",
            r"selected.*what next",
            r"what happens after selection"
        ],
        "answer": (
            "After selection, successful candidates generally need to "
            "complete the required confirmation, documentation, visa and "
            "arrival procedures. Follow the official instructions provided "
            "after each selection stage."
        )
    },

    "visa": {
        "patterns": [
            r"\bvisa\b",
            r"student visa",
            r"visa process"
        ],
        "answer": (
            "GKS students need the appropriate Korean student visa/status "
            "for their program. Visa procedures depend on the scholarship "
            "stage and current Korean immigration/embassy requirements."
        )
    },

    "travel_to_korea": {
        "patterns": [
            r"travel to korea",
            r"flight to korea",
            r"airfare",
            r"when.*korea"
        ],
        "answer": (
            "GKS can provide airfare support according to the scholarship "
            "rules. Travel dates and procedures are communicated to selected "
            "scholars through the relevant official channels."
        )
    },

    "arrival": {
        "patterns": [
            r"arrival in korea",
            r"after arriving",
            r"first day.*korea",
            r"arrival procedure"
        ],
        "answer": (
            "After arrival, students may need to complete university, "
            "immigration and scholarship-related procedures. Your university "
            "and the relevant Korean authorities will provide instructions."
        )
    },

    "dormitory": {
        "patterns": [
            r"dormitory",
            r"dorm",
            r"hostel",
            r"student housing"
        ],
        "answer": (
            "Dormitory availability and cost depend on the university. "
            "Check your university's official housing information for room "
            "types, fees, meals, application dates and rules."
        )
    },

    "arc": {
        "patterns": [
            r"\barc\b",
            r"alien registration",
            r"residence card"
        ],
        "answer": (
            "International students in Korea generally need the appropriate "
            "residence registration/card process. Your university's "
            "international office should guide you through the procedure."
        )
    },

    "bank_account": {
        "patterns": [
            r"bank account",
            r"open.*bank",
            r"korean bank"
        ],
        "answer": (
            "Many international students open a Korean bank account for "
            "everyday payments and scholarship-related transactions. "
            "Requirements vary by bank and immigration status."
        )
    },

    "sim_card": {
        "patterns": [
            r"sim card",
            r"phone.*korea",
            r"korean number"
        ],
        "answer": (
            "You can arrange mobile service after arriving in Korea. "
            "Requirements and plans vary by provider and your identification "
            "or residence status."
        )
    },

    "student_life": {
        "patterns": [
            r"student life",
            r"life in korea",
            r"international student life"
        ],
        "answer": (
            "Student life in Korea can involve academics, language learning, "
            "clubs, campus activities and adapting to a different culture. "
            "Good time management and willingness to communicate can help."
        )
    },

    "cost_of_living": {
        "patterns": [
            r"cost of living",
            r"living cost",
            r"expenses in korea"
        ],
        "answer": (
            "Living costs depend on city, housing, food and lifestyle. "
            "Seoul can be more expensive than many regional cities. GKS "
            "scholarship support is designed to help with study and living "
            "expenses, subject to the current scholarship terms."
        )
    },

    "clubs": {
        "patterns": [
            r"clubs",
            r"student clubs",
            r"extracurricular.*korea"
        ],
        "answer": (
            "Korean universities commonly offer student clubs and campus "
            "activities. Check your university's international student "
            "office or student organizations for current options."
        )
    },

    "travel": {
        "patterns": [
            r"travel.*korea",
            r"places.*korea",
            r"tour.*korea"
        ],
        "answer": (
            "Students can explore Korea during free time while balancing "
            "their academic responsibilities. Follow university rules and "
            "manage your budget carefully."
        )
    },

    "academic_rules": {
        "patterns": [
            r"academic rules",
            r"gpa",
            r"attendance",
            r"academic performance"
        ],
        "answer": (
            "GKS scholars are expected to maintain satisfactory academic "
            "performance and follow university and scholarship rules. "
            "Exact GPA, attendance and continuation conditions should be "
            "checked in the current scholarship regulations."
        )
    },

    "scholarship_cancellation": {
        "patterns": [
            r"scholarship cancellation",
            r"lose scholarship",
            r"cancel scholarship",
            r"scholarship terminated"
        ],
        "answer": (
            "Scholarship continuation can depend on academic performance, "
            "conduct and compliance with scholarship rules. Serious "
            "violations may affect scholarship status. Check the current "
            "GKS regulations for exact conditions."
        )
    },

    "leave_absence": {
        "patterns": [
            r"leave",
            r"absence",
            r"take a break",
            r"leave from university"
        ],
        "answer": (
            "Leave or absence rules depend on the university and scholarship "
            "regulations. Do not take an extended leave without first "
            "checking the official rules and obtaining the required approval."
        )
    },

    "other_scholarship": {
        "patterns": [
            r"other scholarship",
            r"another scholarship",
            r"multiple scholarships"
        ],
        "answer": (
            "Receiving another scholarship while holding GKS may be "
            "restricted depending on the type and funding source. Check "
            "the current GKS regulations before accepting additional "
            "financial support."
        )
    }
}


# ============================================================
# INTENT MATCHING
# ============================================================

def find_intent(user_input):

    text = clean_text(user_input)

    priority_intents = [
        "ielts",
        "topik",
        "documents",
        "transcript",
        "apostille",
        "notarization",
        "recommendation_letter",
        "personal_statement",
        "study_plan",
        "interview",
        "benefits",
        "uic",
        "embassy_track",
        "university_track",
        "visa",
        "dormitory",
        "cs_without_math",
        "academic_requirement",
        "gks_u",
        "gks"
    ]

    # --------------------------------------------------------
    # Synonym expansion
    # --------------------------------------------------------

    expanded_text = text

    for group, words in synonyms.items():

        for word in words:

            if word in text:
                expanded_text += " " + group

    # --------------------------------------------------------
    # Small typo correction
    # --------------------------------------------------------

    corrected_words = []

    for word in expanded_text.split():

        best_word = word
        best_similarity = 0

        for group, words in synonyms.items():

            for possible_word in words:

                score = similarity(word, possible_word)

                if score > best_similarity:

                    best_similarity = score
                    best_word = possible_word

        if best_similarity >= 0.80:

            corrected_words.append(best_word)

        else:

            corrected_words.append(word)

    expanded_text = " ".join(corrected_words)

    # --------------------------------------------------------
    # Find best intent
    # --------------------------------------------------------

    best_intent = None
    best_score = 0

    # Priority intents
    for priority, intent in enumerate(priority_intents):

        if intent not in knowledge_base:
            continue

        score = 0

        for pattern in knowledge_base[intent]["patterns"]:

            matches = re.findall(pattern, expanded_text)

            if matches:

                for match in matches:

                    if isinstance(match, tuple):
                        match_text = " ".join(match)
                    else:
                        match_text = match

                    score += len(match_text) + 10

        if score > 0:

            score += len(priority_intents) - priority

        if score > best_score:

            best_score = score
            best_intent = intent

    # Remaining intents
    for intent, data in knowledge_base.items():

        if intent in priority_intents:
            continue

        score = 0

        for pattern in data["patterns"]:

            matches = re.findall(pattern, expanded_text)

            if matches:

                for match in matches:

                    if isinstance(match, tuple):
                        match_text = " ".join(match)
                    else:
                        match_text = match

                    score += len(match_text)

        if score > best_score:

            best_score = score
            best_intent = intent

    # --------------------------------------------------------
    # Confidence
    # --------------------------------------------------------

    if best_intent is None:

        return None, 0

    if best_score >= 30:

        confidence = 0.95

    elif best_score >= 20:

        confidence = 0.85

    elif best_score >= 10:

        confidence = 0.70

    else:

        confidence = 0.50

    return best_intent, confidence


# ============================================================
# FOLLOW-UP CONTEXT
# ============================================================

last_intent = None


def get_response(user_input):

    global last_intent

    intent, confidence = find_intent(user_input)

    text = clean_text(user_input)

    follow_up_phrases = [
        "which one",
        "what about",
        "how about",
        "tell me more",
        "more about it",
        "and then",
        "what about that",
        "what about this",
        "is it better",
        "which is better"
    ]

    is_follow_up = any(
        phrase in text
        for phrase in follow_up_phrases
    )

    # --------------------------------------------------------
    # Use previous topic for follow-up questions
    # --------------------------------------------------------

    if (intent is None or confidence < 0.70) and is_follow_up:

        if last_intent is not None:

            intent = last_intent
            confidence = 0.80

    # --------------------------------------------------------
    # Low confidence response
    # --------------------------------------------------------

    if intent is None or confidence < 0.70:

        return (
            "I'm not fully sure what you mean yet. 🤔\n\n"
            "Could you rephrase your question?\n\n"
            "You can ask about:\n"
            "• Eligibility\n"
            "• Documents\n"
            "• IELTS / TOPIK\n"
            "• UIC\n"
            "• Embassy / University Track\n"
            "• Personal Statement\n"
            "• Study Plan\n"
            "• Recommendation Letters\n"
            "• Interviews\n"
            "• Scholarship benefits\n"
            "• Student life in Korea"
        )

    last_intent = intent

    return knowledge_base[intent]["answer"]


# ============================================================
# HELP MENU
# ============================================================

def show_help():

    print(
        "\nYou can ask me about:\n\n"

        "📚 APPLICATION\n"
        "• GKS / GKS-U\n"
        "• Eligibility\n"
        "• Age requirements\n"
        "• Academic requirements\n"
        "• Application schedule\n"
        "• Application status\n\n"

        "📄 DOCUMENTS\n"
        "• Required documents\n"
        "• Transcript\n"
        "• Certificates\n"
        "• Apostille\n"
        "• Notarization\n"
        "• Translation\n"
        "• Passport\n\n"

        "🎓 UNIVERSITY\n"
        "• Embassy Track\n"
        "• University Track\n"
        "• UIC\n"
        "• University selection\n"
        "• Major availability\n"
        "• Major change\n\n"

        "✍️ APPLICATION WRITING\n"
        "• Personal Statement\n"
        "• Study Plan\n"
        "• Why Korea?\n"
        "• Why GKS?\n"
        "• Why this major?\n"
        "• Recommendation Letter\n\n"

        "🎤 SELECTION\n"
        "• Interview\n"
        "• Interview questions\n"
        "• Selection process\n\n"

        "🇰🇷 AFTER SELECTION\n"
        "• Scholarship benefits\n"
        "• Korean language training\n"
        "• Visa\n"
        "• Arrival\n"
        "• Dormitory\n"
        "• Student life\n\n"

        "Type 'source' for information-source guidance.\n"
        "Type 'about' to learn about this project.\n"
        "Type 'exit' to close the chatbot."
    )


# ============================================================
# TOPICS
# ============================================================

def show_topics():

    print(
        "\nMain GKS topics:\n\n"
        "1. Eligibility\n"
        "2. Documents\n"
        "3. Embassy Track\n"
        "4. University Track\n"
        "5. UIC\n"
        "6. IELTS / TOPIK\n"
        "7. Personal Statement\n"
        "8. Study Plan\n"
        "9. Recommendation Letter\n"
        "10. Interview\n"
        "11. Scholarship Benefits\n"
        "12. Visa & Arrival\n"
        "13. Student Life"
    )


# ============================================================
# SOURCE INFORMATION
# ============================================================

def show_source():

    print(
        "\nOfficial-source guidance:\n\n"

        "For current GKS rules, use the official Study in Korea / "
        "NIIED GKS notices and the current GKS-U Application Guidelines.\n\n"

        "Important:\n"
        "GKS rules, deadlines, university lists, departments, document "
        "requirements and scholarship amounts can change between cycles.\n\n"

        "This chatbot is a student-built educational project and is "
        "NOT an official GKS service.\n\n"

        "Always verify important application decisions using the latest "
        "official GKS-U guideline and the relevant embassy/university."
    )


# ============================================================
# ABOUT PROJECT
# ============================================================

def show_about():

    print(
        "\n" + "=" * 60
    )

    print(
        "              ABOUT THIS PROJECT"
    )

    print(
        "=" * 60
    )

    print(
        "\nProject: GKS Applicant Assistant\n"
        "Version: 1.0\n"
        "Application cycle reference: 2027\n\n"

        "This is a student-built rule-based NLP-style chatbot designed "
        "to help GKS undergraduate applicants explore common questions.\n\n"

        "Main technologies:\n"
        "• Python\n"
        "• Regular Expressions\n"
        "• Pattern-based Intent Classification\n"
        "• Synonym Matching\n"
        "• Similarity-based Typo Handling\n"
        "• Confidence Scoring\n"
        "• Session-level Context\n\n"

        "Important limitation:\n"
        "This is not an official GKS system and does not replace the "
        "official application guidelines."
    )


# ============================================================
# MAIN CHATBOT
# ============================================================

def chatbot():

    print("\n" + "=" * 60)

    print(
        "              GKS APPLICANT ASSISTANT"
    )

    print("=" * 60)

    print(
        f"\nHello! 👋 I am the {BOT_NAME}."
        f"\n\nI can help you explore common GKS undergraduate topics "
        f"for the {CURRENT_GKS_CYCLE} cycle."
        "\n\nType 'help' to see available topics."
        "\nType 'source' for official-source guidance."
        "\nType 'about' to learn about this project."
        "\nType 'exit' to close the chatbot."
    )

    while True:

        try:

            user_input = input("\nYou: ")

            cleaned = clean_text(user_input)

            # ------------------------------------------------
            # Empty input
            # ------------------------------------------------

            if not cleaned:

                print(
                    "Bot: Please type a question."
                )

                continue

            # ------------------------------------------------
            # Exit
            # ------------------------------------------------

            if cleaned in [
                "exit",
                "quit",
                "bye",
                "close"
            ]:

                print(
                    "\nBot: Goodbye! 👋\n"
                    "Good luck with your GKS journey! 🇰🇷🎓"
                )

                break

            # ------------------------------------------------
            # Help
            # ------------------------------------------------

            if cleaned == "help":

                show_help()

                continue

            # ------------------------------------------------
            # Topics
            # ------------------------------------------------

            if cleaned == "topics":

                show_topics()

                continue

            # ------------------------------------------------
            # Source
            # ------------------------------------------------

            if cleaned == "source":

                show_source()

                continue

            # ------------------------------------------------
            # About
            # ------------------------------------------------

            if cleaned == "about":

                show_about()

                continue

            # ------------------------------------------------
            # Normal question
            # ------------------------------------------------

            response = get_response(user_input)

            print(
                f"\nBot: {response}"
            )

        except KeyboardInterrupt:

            print(
                "\n\nBot: Chatbot closed. 👋"
            )

            break

        except Exception as error:

            print(
                "\nBot: Something unexpected happened."
            )

            print(
                "Please try asking the question again."
            )

            print(
                f"(Technical information: {error})"
            )


# ============================================================
# PROGRAM START
# ============================================================


if __name__=="__main__":
    chatbot()