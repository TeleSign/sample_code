curl -u "$CUSTOMER_ID":"$API_KEY" \
     --url https://rest-ww.telesign.com/v1/messaging \
     --header 'accept: application/x-www-form-urlencoded' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data phone_number="$PHONE_NUMBER" \
     --data message="Your package has shipped! Follow your delivery at https://vero-finto.com/orders/3456" \
     --data message_type="ARN"