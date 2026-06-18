import unittest

from app.services.parsering_resume import parser


class ResumeParserTests(unittest.TestCase):
    def test_parser_accepts_pdf_heading_formatting(self):
        result = parser(
            """
            JANE DOE
            EDUCATION:
            B.Tech in Computer Science
            TECHNICAL  SKILLS
            Python, FastAPI
            PROFESSIONAL EXPERIENCE
            Backend Developer at Example Ltd
            CERTIFICATIONS ***
            AWS Cloud Practitioner
            """
        )

        self.assertEqual(result["data"], {
            "education": ["B.Tech in Computer Science"],
            "skills": ["Python, FastAPI"],
            "projects": [],
            "experience": ["Backend Developer at Example Ltd"],
            "certifications": ["AWS Cloud Practitioner"],
        })

    def test_parser_accepts_heading_and_content_on_same_line(self):
        result = parser("Skills: Python, FastAPI\nProjects: Interview Copilot")

        self.assertEqual(result["data"]["skills"], ["Python, FastAPI"])
        self.assertEqual(result["data"]["projects"], ["Interview Copilot"])

    def test_parser_accepts_letter_spaced_pdf_headings(self):
        result = parser(
            "E D U C A T I O N\nB.Tech in Computer Science\n"
            "T E C H N I C A L  S K I L L S\nPython, FastAPI\n"
            "P R O J E C T S\nAI Interview Copilot"
        )

        self.assertEqual(result["data"]["education"], ["B.Tech in Computer Science"])
        self.assertEqual(result["data"]["skills"], ["Python, FastAPI"])
        self.assertEqual(result["data"]["projects"], ["AI Interview Copilot"])


if __name__ == "__main__":
    unittest.main()
