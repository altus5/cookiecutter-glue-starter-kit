#!/bin/sh

S3_BUCKET={{ cookiecutter.s3_test_bucket_name }}
S3_URL=s3://$S3_BUCKET

# バケットの作成
awslocal s3 mb $S3_URL

# テストファイルを配置
DATA_DIR=/app/fixtures/data/it
awslocal s3 cp --recursive $DATA_DIR/ $S3_URL/{{ cookiecutter.s3_test_data_path }}/
