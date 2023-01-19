from flask import Flask, request
from google.cloud import pubsub_v1

# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path('tranquility-base-hotel', 'contact-form')

app = Flask(__name__)

@app.route('/contact-form', methods=['POST'])
def contact_form():
    import json

    data_str = json.dumps(request.json)
    # Data must be a bytestring
    data = data_str.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

    print(f"Form data published to {topic_path}.")

    return json.dumps({'message': 'ok'})