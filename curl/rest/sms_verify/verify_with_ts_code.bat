curl -u "$CUSTOMER_ID":"$API_KEY" \
     --url https://rest-ww.telesign.com/v1/verify/sms \
     --header 'accept: application/x-www-form-urlencoded' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data phone_number="$PHONE_NUMBER"