from openai import AzureOpenAI
from typing_extensions import Self
from typing import TypedDict
import requests


class ModelEndpoints:
    def __init__(self: Self, model_type: str) -> str:
        self.model_type = model_type

    class Response(TypedDict):
        query: str
        response: str

    def __call__(self: Self, query: str) -> Response:
        if self.model_type == "o4-mini":
            output = self.call_o4_mini_endpoint(query)
        elif self.model_type == "gpt5":
            output = self.call_gpt5_endpoint(query)
        elif self.model_type == "ministral":
            output = self.call_ministral_endpoint(query)
        elif self.model_type == "grok":
            output = self.call_grok_endpoint(query)
        elif self.model_type == "claude":
            output = self.call_claude_endpoint(query)
        else:
            output = self.call_default_endpoint(query)

        return output

    def query(self: Self, endpoint: str, headers: str, payload: str) -> str:
        response = requests.post(url=endpoint, headers=headers, json=payload)
        return response.json()

    def call_o4_mini_endpoint(self: Self, query: str) -> Response:
        endpoint = "https://vk-2255-resource.cognitiveservices.azure.com/openai/deployments/o4-mini/chat/completions?api-version=2025-01-01-preview" #self.env["o4-mini"]["endpoint"]
        key = "EboWgl2E6kLJNNHJBuK41NbneHUddO6sMGVD7elpZ4xdrlx305ZcJQQJ99BJACHYHv6XJ3w3AAAAACOGYeJW" #self.env["o4-mini"]["key"]

        headers = {"Content-Type": "application/json", "api-key": key}

        payload = {"messages": [{"role": "user", "content": query}], "max_completion_tokens": 800}

        try:
            output = self.query(endpoint=endpoint, headers=headers, payload=payload)
            response = output["choices"][0]["message"]["content"]
            return {"query": query, "response": response}
        except (KeyError, IndexError, TypeError) as e:
            error_msg = f"Error parsing o4-mini response: {str(e)}"
            return {"query": query, "response": error_msg}

    def call_gpt5_endpoint(self: Self, query: str) -> Response:
        key = "EboWgl2E6kLJNNHJBuK41NbneHUddO6sMGVD7elpZ4xdrlx305ZcJQQJ99BJACHYHv6XJ3w3AAAAACOGYeJW"

        endpoint = "https://vk-2255-resource.cognitiveservices.azure.com/"
        deployment = "gpt-5"

        api_version = "2025-01-01-preview"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=key,
        )

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                },
            ],
            model=deployment,
            max_completion_tokens=800,
        )
        return {"query": query, "response": response.choices[0].message.content}

    def call_ministral_endpoint(self: Self, query: str) -> Response:
        endpoint = "https://vk-2255-resource.services.ai.azure.com/"
        key = "EboWgl2E6kLJNNHJBuK41NbneHUddO6sMGVD7elpZ4xdrlx305ZcJQQJ99BJACHYHv6XJ3w3AAAAACOGYeJW"

        api_version = "2024-05-01-preview"
        deployment = "Ministral-3B"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=key,
        )

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                },
            ],
            model=deployment
        )
        return {"query": query, "response": response.choices[0].message.content}

    def call_default_endpoint(self: Self, query: str) -> Response:
        return {"query": query, "response": "Paris"}

    def call_grok_endpoint(self: Self, query: str) -> Response:
        key = "EboWgl2E6kLJNNHJBuK41NbneHUddO6sMGVD7elpZ4xdrlx305ZcJQQJ99BJACHYHv6XJ3w3AAAAACOGYeJW"
        endpoint = "https://vk-2255-resource.cognitiveservices.azure.com/"
        deployment = "grok-4"  # Update this to match your actual deployment name
        api_version = "2024-05-01-preview"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=key,
        )

        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
                model=deployment,
                max_completion_tokens=800,
            )
            return {"query": query, "response": response.choices[0].message.content}
        except Exception as e:
            return {"query": query, "response": f"Error calling grok endpoint: {str(e)}"}

    def call_claude_endpoint(self: Self, query: str) -> Response:
        key = "EboWgl2E6kLJNNHJBuK41NbneHUddO6sMGVD7elpZ4xdrlx305ZcJQQJ99BJACHYHv6XJ3w3AAAAACOGYeJW"
        endpoint = "https://vk-2255-resource.cognitiveservices.azure.com/"
        deployment = "claude-sonnet-4-5"  # Update this to match your actual deployment name
        api_version = "2024-05-01-preview"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=key,
        )

        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
                model=deployment,
                max_completion_tokens=800,
            )
            return {"query": query, "response": response.choices[0].message.content}
        except Exception as e:
            return {"query": query, "response": f"Error calling claude endpoint: {str(e)}"}