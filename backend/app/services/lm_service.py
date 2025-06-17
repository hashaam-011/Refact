import requests
import json
from typing import Dict, Any, List

class LMStudioService:
    def __init__(self, base_url: str = "http://localhost:1234/v1"):
        self.base_url = base_url

    async def generate_text(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """Generate text using the LM Studio model."""
        try:
            response = requests.post(
                f"{self.base_url}/completions",
                json={
                    "prompt": prompt,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "stop": None
                }
            )
            response.raise_for_status()
            return response.json()["choices"][0]["text"]
        except Exception as e:
            raise Exception(f"Error generating text: {str(e)}")

    async def analyze_code(self, code: str) -> Dict[str, Any]:
        """Analyze code using the LM Studio model."""
        prompt = f"""Analyze the following code and provide:
1. Code quality assessment
2. Potential improvements
3. Security concerns
4. Performance considerations

Code:
{code}

Analysis:"""

        analysis = await self.generate_text(prompt)
        return {
            "analysis": analysis,
            "code": code
        }

    async def refactor_code(self, code: str, instructions: str) -> Dict[str, Any]:
        """Refactor code based on instructions using the LM Studio model."""
        prompt = f"""Refactor the following code according to these instructions:
{instructions}

Original code:
{code}

Refactored code:"""

        refactored = await self.generate_text(prompt)
        return {
            "original_code": code,
            "refactored_code": refactored,
            "instructions": instructions
        }