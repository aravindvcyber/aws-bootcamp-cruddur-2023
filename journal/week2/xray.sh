aws xray create-group \
     --group-name "Crudder" \
     --filter-expression "service(\"backend-flask\")"