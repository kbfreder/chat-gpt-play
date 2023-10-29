
const OPEN_API_KEY = ""


async function fetchData() {
    const response = await fetch ("https://api.openai.com/v1/chat/completions", {
        method: "POST",
        headers: {
            Authorization: `Bearer ${OPEN_API_KEY}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{
                role: "user",
                content: "Wassup?!"
            }],
            temperature: 0.7
        })
    })
    const answer = await response.json()
    console.log(answer)
}

fetchData()