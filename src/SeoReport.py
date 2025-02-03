import subprocess
import json
from datetime import datetime

class SeoReport:
    @staticmethod
    def generate_report(domain_name):
        urls = [domain_name]
        print(f"Generating report for domain: {domain_name}")

        try:
            for url in urls:
                # Adding user-agent and disabling web security flags
                command = f'lighthouse {url} --output=json --quiet --chrome-flags="--headless --ignore-certificate-errors --disable-web-security --user-agent=\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\'"'
                print(f"Running command: {command}")

                result = subprocess.run(
                    command, capture_output=True, text=True, shell=True, encoding='utf-8', errors='replace'
                )

                if result.returncode != 0:
                    # Command execution failed
                    print(f"Error in command execution: {result.stderr.strip()}")
                    return {
                        'status': 'failed',
                        'message': f'Error executing command for {url}',
                        'error': result.stderr.strip()
                    }

                try:
                    # Parse the JSON output
                    report = json.loads(result.stdout)
                    print("Report generated successfully.")
                    return {
                        'data': report,
                        'status': 'success'
                    }

                except json.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e}")
                    return {
                        'status': 'failed',
                        'message': 'Failed to parse JSON output from Lighthouse',
                        'error': str(e)
                    }

        except Exception as e:
            print(f"Unexpected exception: {e}")
            return {
                'status': 'failed',
                'message': 'Unexpected error occurred',
                'error': str(e)
            }
