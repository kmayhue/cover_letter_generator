# Gemini CLI Instructions for Cover Letter Generator

This repository is designed to automate the creation of cover letters and interview preparation materials using the Gemini CLI.

## Repository Structure

- `jobs/`: Contains subfolders for each job application.
    - `job_description.md`: The job posting details.
    - `job_application.md` (Optional): Specific questions from the application form.
- `user_info/`: Your personal data.
    - `resume.md`: Your current resume in Markdown.
    - `experiences.md`: Detailed descriptions of your roles and achievements in plain English.
    - `cover_letter_examples/`: Markdown files of your previous successful cover letters.
- `main.py`: The entry point for generating content.

## How to use

Run the generator using:
```bash
python main.py <job_folder_name> --tool <cover_letter|interview_prep> --model <model_name>
```

## Prompting Guidelines

When the Python script calls you (Gemini), it will provide:
1. Your Resume.
2. Your detailed experiences.
3. The specific job description.
4. Any specific application questions.
5. Examples of your writing style from past cover letters.

**Your Goal:**
- If `tool` is `cover_letter`: Create a compelling, tailored cover letter that matches the user's voice and highlights the most relevant skills for the job. Answer any specific application questions provided.
- If `tool` is `interview_prep`: Identify key themes in the job description and create a list of likely interview questions. Provide tailored answers using the user's specific experiences.
