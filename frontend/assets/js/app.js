const API_BASE_URL = "http://127.0.0.1:8001";

console.log("app.js loaded");

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("ask-btn").onclick = askAI;
    document.getElementById("analyze-btn").onclick = analyzeResume;
});

async function askAI() {
    const question = document.getElementById("ai-question").value;
    const box = document.getElementById("ai-response");

    box.innerText = "Thinking...";

    try {
        const res = await fetch(`${API_BASE_URL}/api/ai/ask`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: question })
        });

        const data = await res.json();
        box.innerText = data.response ?? "No response";
    } catch {
        box.innerText = "AI error";
    }
}

async function analyzeResume() {
    const file = document.getElementById("resume-file").files[0];
    const role = document.getElementById("role").value;
    const box = document.getElementById("resume-result");

    if (!file) {
        box.innerText = "Upload resume";
        return;
    }

    const form = new FormData();
    form.append("file", file);
    form.append("role", role);

    box.innerText = "Analyzing...";

    try {
        const res = await fetch(`${API_BASE_URL}/api/resume/analyze`, {
            method: "POST",
            body: form
        });

        const d = await res.json();

        box.innerHTML = `
            <b>Extracted:</b> ${(d.extracted_skills || []).join(", ")}<br>
            <b>Missing:</b> ${(d.missing_skills || []).join(", ")}<br>
            <ul>${(d.recommendations || []).map(r => `<li>${r}</li>`).join("")}</ul>
        `;
    } catch {
        box.innerText = "Resume error";
    }
}
