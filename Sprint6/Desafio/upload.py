import boto3
import os
from botocore.exceptions import NoCredentialsError
from datetime import datetime

def upload_to_s3(local_file, bucket, s3_path):
    s3 = boto3.client(
        's3',
        aws_access_key_id=(''),
        aws_secret_access_key=(''),
        aws_session_token=('')
<<<<<<< HEAD
=======
        # Está sem as chaves por motivos de segurança na hora de mandar pro git
>>>>>>> 6037921c1ed6d08feae917c4ea78bd07efb8e382
    )
    try:
        # Faz o upload do arquivo para o bucket S3
        s3.upload_file(local_file, bucket, s3_path)
        print(f"Upload Successful: {local_file} to {bucket}/{s3_path}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == "_main_":
>>>>>>> 6037921c1ed6d08feae917c4ea78bd07efb8e382
    s3_bucket = "data-lake-da-ana"
    
    storage_layer = "raw"
    data_origin = "local"
    data_format = "csv"
    nome = "movies"
    
    processing_date = datetime.now().strftime("%Y/%m/%d").split('/')
    year, month, day = processing_date

    files_to_upload = ["movies.csv"]

    for filename in files_to_upload:
        local_path = filename  
        if os.path.exists(local_path):
        
            if filename == "movies.csv":
                s3_path = f"{storage_layer}/{data_origin}/{data_format}/{nome}/{year}/{month}/{day}/movies.csv"
    
            # Aqui faz o upload para o S3
            upload_to_s3(local_path, s3_bucket, s3_path)
        else:
<<<<<<< HEAD
            print(f"File not found: {local_path}")

=======
            print(f"File not found: {local_path}")
>>>>>>> 6037921c1ed6d08feae917c4ea78bd07efb8e382
