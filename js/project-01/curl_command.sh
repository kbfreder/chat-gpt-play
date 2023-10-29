source ../.env

curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPEN_API_KEY" \
-d '{
"model": "text-davinci-003",
"prompt": "Life is a highway. I want to ride it ",
"max_tokens": 10,
"temperature": 0.2
}'
