## Story 001
* greet
    - utter_greet
	- actions_restart
	
## Story 002
* goodbye
    - utter_goodbye
	- actions_restart
	
## Story 003
* thankyou
	- utter_thankyou	
	- actions_restart


## Null entity
## Story 004 - full positive flow starting from null entity and opt email
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 005 - full positive starting from null entity and opt no email
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 006 - starting from null entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 007 - starting from null entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	
	
	
## Single entity
## Story 008 - full positive flow starting with location and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 009 - full positive flow starting with location and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 010 - starting with location entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 011 - starting with location entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	



## Story 012 - full positive flow starting with cuisine and opt email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location	
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 013 - full positive flow starting with cuisine and opt no email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 014 - starting with cuisine entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 015 - starting with cuisine entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	




## Story 016 - full positive flow starting with budget and opt email
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 017 - full positive flow starting with budget and opt no email
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 018 - starting with budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 019 - starting with budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	



## Story 020 - full positive flow starting with email and opt email
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 021 - starting with email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 022 - starting with email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	
	
	

## Double entity
## Story 023 - full positive flow starting with location and cuisine and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 024 - full positive flow starting with location and cuisine and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 025 - starting with location and cuisine entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget": "300"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 026 - starting with location and cuisine entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine": "chinese"}
	- slot{"location": "delhi"}	
	- slot{"cuisine": "chinese"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	





## Story 027 - full positive flow starting with location and budget and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 028 - full positive flow starting with location and budget and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 029 - starting with location and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 030 - starting with location and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300"}
	- slot{"location": "delhi"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	




## Story 031 - full positive flow starting with location and email and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 032 - starting with location and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 033 - starting with location and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	




## Story 034 - full positive flow starting with cuisine and budget and opt email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 035 - full positive flow starting with cuisine and budget and opt no email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 036 - starting with cuisine and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 037 - starting with cuisine and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	





## Story 038 - full positive flow starting with email and budget and opt email
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","budget":"300"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 039 - starting with email and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","budget":"300"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 040 - starting with email and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","budget":"300"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"budget":"300"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	




## Story 041 - full positive flow starting with email and cuisine and opt email
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","cuisine":"chinese"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"cuisine":"chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 042 - starting with email and cuisine entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","cuisine":"chinese"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"cuisine":"chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 043 - starting with email and cuisine entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"email":"abc@xyz.com","cuisine":"chinese"}
	- slot{"email":"abc@xyz.com"}	
	- slot{"cuisine":"chinese"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location":"delhi"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	



## Triple entities
## Story 044 - full positive flow starting with location, cuisine and budget and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart


## Story 045 - full positive flow starting with location, cuisine and budget and opt no email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- utter_ask_email_needed
* deny
	- utter_goodbye
	- actions_restart


## Story 046 - starting with location, cuisine and budget entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- utter_ask_email_needed
* affirm
	- utter_ask_emailid
* send_email{"email":"abc@xyz.com"}
	- slot{"email": "abc@xyz.com"}
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 047 - starting with location, cuisine and budget entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"budget":"300"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	




## Story 048 - full positive flow starting with location, cuisine and email and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 049 - starting with location, cuisine and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_budget
* restaurant_search{"budget":"300"}
	- slot{"budget":"300"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 050 - starting with location, cuisine and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"cuisine":"chinese"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	





## Story 051 - full positive flow starting with location, budget and email and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 052 - starting with location, budget and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
	- slot{"cuisine":"chinese"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
## Story 053 - starting with location, budget and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","budget":"300","email":"abc@xyz.com"}
	- slot{"location":"delhi"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	




## Story 054 - full positive flow starting with cuisine, budget and email and opt email
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 055 - starting with cuisine, budget and email entity and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	

	
## Story 056 - starting with cuisine, budget and email entity and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- utter_ask_location
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart	



## Four entities
## Story 057 - full positive flow starting with all entities and opt email
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "true"}
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart



## Story 058 - starting with all entities and location not valid in first attempt but valid in the second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"location": "delhi"}
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "true"}	
	- action_search_restaurant
	- action_send_email
	- utter_email_status
	- utter_goodbye
	- actions_restart
	
	
	
## Story 059 - starting with all entities and location not valid in first attempt and second attempt
* greet
    - utter_greet
* restaurant_search{"location":"delhi","cuisine":"chinese","budget":"300","email":"abc@xyz.com"}
	- slot{"location": "delhi"}	
	- slot{"cuisine":"chinese"}
	- slot{"budget":"300"}	
	- slot{"email":"abc@xyz.com"}
	- action_check_location
    - slot{"valid_location": "false"}
	- utter_location_not_valid
* restaurant_search{"location":"delhi"}
	- slot{"location": "delhi"}	
	- action_check_location
    - slot{"valid_location": "false"}	
	- utter_default
	- utter_goodbye
	- actions_restart
	
