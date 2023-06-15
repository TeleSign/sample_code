curl -u "$CUSTOMER_ID":"$API_KEY" \
     --url https://rest-ww.telesign.com/v1/score/$PHONE_NUMBER \
     --header 'accept: application/x-www-form-urlencoded' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data account_lifecycle_event="create" \
     --data request_risk_insights="true"