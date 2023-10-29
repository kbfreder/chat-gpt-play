
// require('dotenv').confg()
// import * as dotenv from 'dotenv'
// dotenv.config()
// const OPEN_API_KEY = process.env.OPEN_API_KEY

const OPEN_API_KEY = ""

async function fetchData() {
    const response = await fetch ("https://api.openai.com/v1/completions", {
        method: "POST",
        headers: {
            Authorization: `Bearer ${OPEN_API_KEY}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            model: "text-davinci-003",
            prompt: "Once upon a time, in a land far, far away",
            max_tokens: 256,
            temperature: 0.7
        })
    })
    const answer = await response.json()
    console.log(answer)
}

fetchData()