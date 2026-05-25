import requests
import time
import xml.etree.ElementTree as ET

def search_papers(query: str, limit: int = 5) -> str:
    try:
        url = "https://export.arxiv.org/api/query"
        params = {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": limit,
            "sortBy": "relevance",
            "sortOrder": "descending"
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        ns = {"atom": "http://www.w3.org/2005/Atom"}
        root = ET.fromstring(response.text)
        entries = root.findall("atom:entry", ns)

        if not entries:
            return "No papers found for this topic on arXiv."

        lines = []
        for entry in entries[:limit]:
            title      = entry.find("atom:title", ns).text.strip().replace("\n", " ")
            summary    = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
            published  = entry.find("atom:published", ns).text[:4]
            authors    = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
            author_str = ", ".join(authors[:2])
            if len(authors) > 2:
                author_str += " et al."

            lines.append(
                f"Title: {title} ({published})\n"
                f"Authors: {author_str}\n"
                f"Abstract: {summary[:500]}..."
            )

        return "\n\n".join(lines)

    except requests.exceptions.Timeout:
        return "Paper search timed out. Debate will proceed based on general knowledge."
    except Exception as e:
        return f"Could not fetch papers ({str(e)}). Debate will proceed based on general knowledge."