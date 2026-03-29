function scrollToSection() {
    document.getElementById("how").scrollIntoView({ behavior: "smooth" });
}

async function generateContent() {
    try {
        const text = document.getElementById("inputText")?.value;

        if (!text || text.trim() === "") {
            alert("Please enter some text");
            return;
        }

        document.getElementById("logs").innerHTML = "⏳ Starting agents...";
        document.getElementById("outputContent").innerText = "";

        const API_BASE = window.API_BASE || "http://127.0.0.1:8000";

        const res = await fetch(`${API_BASE}/generate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        if (!res.ok) {
            throw new Error(`Backend error: ${res.status} ${res.statusText}`);
        }

        const data = await res.json();

        if (data.logs) {
            document.getElementById("logs").innerHTML =
                data.logs.map(l => {
                    const div = document.createElement("div");
                    div.textContent = `• ${l}`;
                    return div.outerHTML;
                }).join("");
        } else {
            document.getElementById("logs").innerHTML = "⚠️ No logs received";
        }

        if (data.content) {
            document.getElementById("outputContent").innerText = data.content;
        } else {
            document.getElementById("outputContent").innerText = "⚠️ No content generated";
        }

        document.getElementById("output")?.scrollIntoView({ behavior: "smooth" });

    } catch (error) {
        console.error(error);
        document.getElementById("logs").innerHTML = `❌ Error: ${error.message}`;
        document.getElementById("outputContent").innerText = "";
    }
}