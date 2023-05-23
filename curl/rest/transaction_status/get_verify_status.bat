curl --request GET --url https://rest-ww.telesign.com/v1/verify/$1 \
-u "$CUSTOMER_ID":"$API_KEY" \
--header 'accept: application/json'