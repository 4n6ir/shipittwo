#!/usr/bin/env python3
import os

import aws_cdk as cdk

from shipittwo.shipittwo_stack import ShipittwoStack

app = cdk.App()

ShipittwoStack(
    app, 'ShipittwoStackUSE1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

ShipittwoStack(
    app, 'ShipittwoStackUSE2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

ShipittwoStack(
    app, 'ShipittwoStackUSW2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('Alias','ALL')
cdk.Tags.of(app).add('GitHub','https://github.com/jblukach/shipittwo.git')

app.synth()