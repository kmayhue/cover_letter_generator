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
        
    job_description = read_file(os.path.join(job_dir, "job_description.md"))
    if not job_description:
        print(f"Error: job_description.md not found in {job_dir}")
        sys.exit(1)
        
    job_application = read_file(os.path.join(job_dir, "job_application.md"))
    resume = read_file("user_info/resume.md")
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
    # Assuming the CLI is available as 'gemini' and accepts a prompt via stdin or argument.
    # We'll use subprocess to run it. 
    try:
        # Using pipe to send prompt to gemini-cli
        process = subprocess.Popen(['gemini', '--model', args.model], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=prompt)
        
        if process.returncode != 0:
            print(f"Error from Gemini CLI: {stderr}")
        else:
            print(stdout)
            
    except FileNotFoundError:
        print("Error: 'gemini' CLI not found. Please ensure it is installed and in your PATH.")
        sys.exit(1)

if __name__ == "__main__":
    main()
