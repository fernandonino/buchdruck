# The Printer
This job runs in [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) and its purpose is to pull all pending articles for a given a user, generate the PDF and deliver it. The job can run with the frequency the users chooses (daily, weekly, etc.)

## Internals
It is based on Mozilla's [Readability](https://github.com/mozilla/readability) package.