curl -u "$CUSTOMER_ID":"$API_KEY" \
     --url https://rest-ww.telesign.com/v1/phoneid/$PHONE_NUMBER \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '{  
        "addons": {
            "contact": {}
        }
     }'