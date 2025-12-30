import argparse
import os
import json
import subprocess
import sys

def load_config():
    config_path = 'config.json'
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {"default_model": "gemini-1.5-pro"}

def read_file(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.read()
    return ""

def main():
    config = load_config()
    
    parser = argparse.ArgumentParser(description="Gemini Job Application Tool")
    parser.add_argument("job_name", help="Name of the folder in jobs/")
    parser.add_argument("--model", default=config.get("default_model"), help="Gemini model to use")
    parser.add_argument("--tool", choices=["cover_letter", "interview_prep"], required=True, help="Tool to run")
    
    args = parser.parse_args()
    
    job_dir = os.path.join("jobs", args.job_name)
    if not os.path.isdir(job_dir):
        print(f"Error: Job directory '{job_dir}' not found.")
        sys.exit(1)
        
    jd_path = os.path.join(job_dir, "job_description.md")
    if not os.path.exists(jd_path):
        print(f"Error: {jd_path} not found.")
        sys.exit(1)
    job_description = read_file(jd_path)
        
    resume_path = "user_info/resume.md"
    if not os.path.exists(resume_path):
        print(f"Error: {resume_path} not found.")
        sys.exit(1)

    job_application = read_file(os.path.join(job_dir, "job_application.md"))
    resume = read_file(resume_path)
    experiences = read_file("user_info/experiences.md")
    
    example_cover_letters = ""
    examples_dir = "user_info/cover_letter_examples"
    if os.path.exists(examples_dir):
        for filename in os.listdir(examples_dir):
            if filename.endswith(".md"):
                example_cover_letters += f"\n--- Example: {filename} ---\n"
                example_cover_letters += read_file(os.path.join(examples_dir, filename))

    context = f"""
    RESUME:
    {resume}

    MY EXPERIENCES:
    {experiences}

    JOB DESCRIPTION:
    {job_description}

    JOB APPLICATION SPECIFICS:
    {job_application}

    EXAMPLE COVER LETTERS:
    {example_cover_letters}
    """

    if args.tool == "cover_letter":
        prompt = f"{context}\n\nBased on the above information, please generate a professional cover letter and answer any questions found in the job application specifics or job description."
    elif args.tool == "interview_prep":
        prompt = f"{context}\n\nBased on the above information, please generate a list of likely interview questions and suggest strong answers based on my resume and experiences."

    # Execute Gemini CLI
    print(f"Generating {args.tool.replace('_', ' ')} using {args.model}...")
    
    try:
        # Using pipe to send prompt to gemini-cli
        result = subprocess.run(
            ['gemini', '--model', args.model],
            input=prompt,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Error from Gemini CLI: {result.stderr}", file=sys.stderr)
            sys.exit(result.returncode)
        else:
            print("\n" + "="*40 + "\n")
            print(result.stdout)
            print("\n" + "="*40)
            
    except FileNotFoundError:
        print("Error: 'gemini' CLI not found. Please ensure it is installed and in your PATH.")
        sys.exit(1)

if __name__ == "__main__":
    main()
