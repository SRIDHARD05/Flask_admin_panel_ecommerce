from src.AmazonS3 import AmazonS3

class SeoReport:
    def generate_report(self,domain_name):
        urls = [
            domain_name
        ]

        name = "LighthouseReport"
        getdate = datetime.now().strftime("%Y-%m-%d")

        try:
            for url in urls:
                command = f'lighthouse {url} --output=json --quiet --chrome-flags="--headless"'

                try:
                    result = subprocess.run(command, capture_output=True, text=True)
                    if result.returncode != 0 : 
                        return str(e)

                    else:
                        try:
                            report = json.loads(result.stdout)
                            # file_path = f"{get_config("s3_aws_bucket_name")}/{user_id}_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json"
                            # amazon_s3_connection.put_object(Body = report, Bucket = get_config("s3_aws_bucket_name"),Key = file_path)
                            return {
                                "data" : report,
                                'status' : 'success'
                            }

                        except json.JSONDecodeError:
                            return str(e)

                except subprocess.CalledProcessError as e:
                    return str(e)

        except Exception as e:
            return str(e)


