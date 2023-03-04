aws xray create-group \
     --group-name "Crudder" \
     --filter-expression "service(\"backend-flask\")"

aws xray update-group \
     --group-name "Crudder" \
     --filter-expression "service(\"crudder-backend-flask\")"

aws xray get-group --group-name Crudder --output json

aws xray update-group \
     --group-name "Crudder" \
     --filter-expression "service(\"crudder-backend-flask\")" \
     --insights-configuration InsightsEnabled=true

aws xray update-group  \    
     --group-name "Crudder"  \    
     --filter-expression "service(\"crudder-backend-flask\")"  \   
     --insights-configuration InsightsEnabled=true,NotificationsEnabled=true