import re

from app.utils.api_response import success_response


SECTION_MAPPING = {
    "education": "education",
    "academic background": "education",
    "academic qualifications": "education",
    "technical skills": "skills",
    "core skills": "skills",
    "skills": "skills",
    "projects": "projects",
    "personal projects": "projects",
    "experience": "experience",
    "work experience": "experience",
    "professional experience": "experience",
    "employment history": "experience",
    "certificates": "certifications",
    "certifications": "certifications"
}

COMPACT_SECTION_MAPPING = {
    heading.replace(" ", ""): section
    for heading, section in SECTION_MAPPING.items()
}


def _normalise_heading(value: str) -> str:
    # PDF extraction often leaves bullets, colons, or extra spaces around headings.
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return " ".join(value.split())


def _mapped_section(value: str) -> str | None:
    heading = _normalise_heading(value)
    return (
        SECTION_MAPPING.get(heading)
        or COMPACT_SECTION_MAPPING.get(heading.replace(" ", ""))
    )


def _section_heading(line: str) -> tuple[str | None, str]:
    section = _mapped_section(line)
    if section:
        return section, ""

    # Also support compact resume lines such as "Skills: Python, FastAPI".
    heading_part, separator, content = line.partition(":")
    if separator:
        section = _mapped_section(heading_part)
        if section:
            return section, content.strip()

    return None, ""


def parser(resume_text: str) -> dict:
    sections = {
        "education": [],
        "skills": [],
        "projects": [],
        "experience": [],
        "certifications": []
    }
    current_section = None

    for line in resume_text.splitlines():
        clean_line = line.strip()

        if not clean_line:
            continue

        section, inline_content = _section_heading(clean_line)
        if section:
            current_section = section
            if inline_content:
                sections[current_section].append(inline_content)
            continue

        if current_section:
            sections[current_section].append(clean_line)

    return success_response(sections)
