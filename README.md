# Cover Letter & Interview Prep Generator

This tool leverages the Gemini CLI to generate tailored cover letters and interview preparation guides based on your resume, experiences, and specific job descriptions.

## Setup

1. **Prerequisites**: Ensure you have Python installed and the `gemini` CLI available in the PATH.
2. **Verify Gemini CLI**:
   Run the following command to verify your Gemini CLI installation:
   ```bash
   gemini --version
   ```
   If successful, it should return the version number. Ensure you have configured your API key as per the Gemini CLI documentation.
3. **Configure**: Update `config.json` with your preferred default model.

## Folder Structure

- `jobs/`: Create a new folder here for every job you apply to.
  - `jobs/<job_name>/job_description.md`: Required. Paste the job description here.
  - `jobs/<job_name>/job_application.md`: Optional. Add specific questions or notes about the role.
- `user_info/`:
  - `resume.md`: Your resume in Markdown format.
  - `experiences.md`: Your experiences described in plain English.
  - `cover_letter_examples/`: Place your favorite cover letters here to help Gemini match your style.

## Usage

### 1. Generate a Cover Letter
```bash
python main.py <job_folder_name> --tool cover_letter
```

### 2. Prepare for an Interview
```bash
python main.py <job_folder_name> --tool interview_prep
```

## Configuration

You can specify a different model at runtime using the `--model` flag:
```bash
python main.py <job_folder_name> --tool cover_letter --model gemini-1.5-flash
```
 
