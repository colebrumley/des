#!/bin/sh
exec 2>&1
curl -vL -H "X-Consul-Token: $CONSUL_TOKEN" \
	${CONSUL_ADDRESS:-http://127.0.0.1:8500}/v1/agent/service/register \
	-d @- >/dev/stdout <<-EOD
	{
		"Name": "$ACTOR_ATTRIBUTES_NAME",
		"Tags": [
			"$ACTOR_ATTRIBUTES_IMAGE",
			"$ACTOR_ID"
		]
	}
	EOD