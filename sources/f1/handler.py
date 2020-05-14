from datadog_lambda.wrapper import datadog_lambda_wrapper

@datadog_lambda_wrapper
def handler(event, _):
    return 1

