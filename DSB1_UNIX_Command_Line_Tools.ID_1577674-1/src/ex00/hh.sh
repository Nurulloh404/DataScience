#!/bin/sh

# Default vacancy if argument is not provided
VACANCY_NAME="data scientist"

# If argument is provided, use it
if [ ! -z "$1" ]; then
    VACANCY_NAME="$1"
fi

# Encode the vacancy name for URL (simple replacement of space with +)
ENCODED_VACANCY=$(echo "$VACANCY_NAME" | sed 's/ /+/g')

# API URL
# per_page=20: fetch first 20 vacancies
# text=$ENCODED_VACANCY: search query
API_URL="https://api.hh.ru/vacancies?text=$ENCODED_VACANCY&per_page=20"

# Fetch data using curl and save to hh.json
# -s: Silent mode
# -H "User-Agent: api-test-agent": HH API requires a User-Agent header
curl -s -H "User-Agent: api-test-agent" "$API_URL" | jq '.' > hh.json
