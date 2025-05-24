import openai
import hashlib
import json
from datetime import datetime
from rich.console import Console
from pathlib import Path

console = Console()
openai.api_key = "YOUR_OPENAI_API_KEY"  # ubaci privremeno

def generate_report(payload, target_url, profile, vector, hits, agent_name="ShadowFox-X"):
    timestamp = datetime.utcnow().isoformat()
    sha_id = hashlib.sha256(payload.encode()).hexdigest()

    from urllib.parse import urlparse

        host = urlparse(target_url).netloc.replace("www.", "").replace(".", "_")
        filename = f"reports/ai_report_{host}_{sha_id[:6]}.md"
    system_prompt = f"""
You are a cybersecurity analyst AI responsible for drafting professional vulnerability disclosure reports for bug bounty platforms (e.g. HackerOne, Bugcrowd).

Your task:
- Explain the payload
- Describe the vulnerability (type: {vector})
- Explain how the issue was discovered
- Mention the number of successful hits: {hits}
- Mention attack profile used: {profile}
- Recommend a fix
- Sign the payload with SHA256
- Include who found it (agent: {agent_name})
"""

    user_prompt = f"""
Payload used: {payload}
Target URL: {target_url}
Discovered by: {agent_name}
Payload SHA256: {sha_id}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        report_text = response['choices'][0]['message']['content']
        Path("reports").mkdir(parents=True, exist_ok=True)
        with open(filename, "w") as f:
            f.write(report_text)

        console.print(f"\n[✓] AI report generated and saved to: [bold green]{filename}[/bold green]")
        return filename

    except Exception as e:
        console.print(f"[X] Error generating AI report: {e}", style="red")
        return None
